import ai21
ai21.api_key = 'GvTsQtC9JLj7HKfE4T4GADWq4N6qF4Yt'

from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
import openai
import os
from flask_cors import CORS


openai.api_key = os.getenv("OPENAI_API_KEY", "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")
app = Flask(__name__)
CORS(app)

def generate_response(extracted_text, prompt):
    full_prompt = f"{extracted_text} {prompt}"

    
    response = ai21.Completion.execute(
  model="j2-grande-instruct",
  prompt="",
  numResults=1,
  maxTokens=200,
  temperature=0.7,
  topKReturn=0,
  topP=1,
  countPenalty={
    "scale": 0,
    "applyToNumbers": False,
    "applyToPunctuations": False,
    "applyToStopwords": False,
    "applyToWhitespaces": False,
    "applyToEmojis": False
  },
  frequencyPenalty={
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  presencePenalty={
      "scale": 0,
      "applyToNumbers": False,
      "applyToPunctuations": False,
      "applyToStopwords": False,
      "applyToWhitespaces": False,
      "applyToEmojis": False
  },
  stopSequences=[]
)

    message = response.choices[0].text.strip()
    return message

@app.route('/ocr', methods=['POST'])
def ocr():
    file = request.files['image']
    img = Image.open(file.stream)
    # pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
    pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/Cellar/tesseract/5.3.1/bin/tesseract'
    extracted_text = pytesseract.image_to_string(img)
    
    prompt = "Can you paraphrase this in a way that is organized, and easy to understand, while mantaining all of the meaning and most of the same wording?"
    gpt_response = generate_response(extracted_text, prompt)

    return jsonify({'extracted_text': gpt_response})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5000)