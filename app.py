from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import openai
import os
from flask_cors import CORS
from pdf2image import convert_from_path
from werkzeug.utils import secure_filename
import tempfile
import shutil
import boto3

app = Flask(__name__)
CORS(app)
def setup():
    # Set up AWS
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"],
        region_name='us-east-1'
    )

    openai.api_key = os.environ["OPENAI_API_KEY"]
    # openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_response(extracted_text, prompt):
    full_prompt = f"{extracted_text} {prompt}"

    ### OCR --> 
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = response.choices[0].text.strip()
        return message
    except openai.error.RateLimitError:
        # Handle the rate limit error appropriately
        return "API request limit exceeded. Please try again later."

    message = response.choices[0].text.strip()
    return message

def upload_to_s3(file):
    bucket_name = 'phirefly-health-bucket-by-user-id'
    s3 = boto3.client('s3')
    s3.upload_fileobj(file, bucket_name, file.filename)

    print(f"{file} has been uploaded to {bucket_name}")

def pdf_to_image(file_storage):
    filename = secure_filename(file_storage.filename)
    temp_dir = tempfile.mkdtemp()  # Create a temporary directory
    temp_pdf_path = os.path.join(temp_dir, filename)
    file_storage.save(temp_pdf_path)

    pages = convert_from_path(temp_pdf_path, 500)
    for page in pages:
        image_filename = os.path.join(temp_dir, os.path.splitext(filename)[0] + '.jpg')
        page.save(image_filename, 'JPEG')
        return image_filename, temp_dir  # Return the image path and the temporary directory


    

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    file = request.files['image']
    upload_to_s3(file)
    img_path, temp_dir = pdf_to_image(file)  # Receive the image path and temporary directory
    
    with Image.open(img_path) as img:
        extracted_text = pytesseract.image_to_string(img)
    
    prompt = "Can you paraphrase this in a way that is organized, and easy to understand, while maintaining all of the meaning and most of the same wording? Please make this comprehensible at the sixth to eighth grade reading level"
    gpt_response = generate_response(extracted_text, prompt)

    # Clean up: remove the temporary image file and directory
    os.remove(img_path)
    shutil.rmtree(temp_dir)  # Remove the temporary directory
    # return gpt_response
    # return jsonify({'extracted_text': gpt_response}) 
    return jsonify(gpt_response)

if __name__ == '__main__':
    setup()
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
