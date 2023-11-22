from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import openai
import os
from flask_cors import CORS
from pdf2image import convert_from_path


openai.api_key = os.environ["OPENAI_API_KEY"]
# openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)
CORS(app)

def generate_response(extracted_text, prompt):
    full_prompt = f"{extracted_text} {prompt}"

    ### OCR --> 
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

def pdf_to_image(filename):
    # convert the pdf to an image; out.jpg is the output image file
    pages = convert_from_path(filename, 500)
    for page in pages:
        page.save('out.jpg', 'JPEG')
    

@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['image']
    pdf_to_image(file)
    #get absolute path of the image
    img = Image.open('out.jpg')
    # img = Image.open(file.stream)
    extracted_text = pytesseract.image_to_string(img)
    
    prompt = "Can you paraphrase this in a way that is organized, and easy to understand, while mantaining all of the meaning and most of the same wording?"
    gpt_response = generate_response(extracted_text, prompt)

    return jsonify({'extracted_text': gpt_response})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)
