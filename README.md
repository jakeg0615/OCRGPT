# OCRGPT

How to run

Prerequisites:
1. install python3
2. install pip3
3. install virtualenv
4. install tesseract (
    - mac: brew install tesseract
    - linux: sudo apt-get install tesseract-ocr
    - windows:
        - download tesseract from

5. install boto3
6. install flask
7. install pytesseract
8. install pillow
9. install opencv-python
10. install numpy
11. install requests
12. install aws cli
    curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
unzip awscli-bundle.zip
sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

1. replace YOUR_API_KEY with an openAI API key (at https://platform.openai.com/account/api-keys once you have an account)
2. run python app.py to start server
3. open a new terminal and run command below. replace {path_to_image} with the path of your image
curl -X POST -H 'Content-Type: multipart/form-data' -F 'image=@{path_to_image}' http://localhost:5000/ocr
