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
13. install openAI python library
    pip install --upgrade openai
14. install tensorflow
    pip install tensorflow
15. install mysql
    pip install Flask-MySQLdb
16. install mysql server
    - mac: brew install mysql
    - linux: sudo apt-get install mysql-server
    - windows: https://dev.mysql.com/downloads/installer/
17. install mysql workbench
    - mac: brew install mysqlworkbench
    - linux: sudo apt-get install mysql-workbench
    - windows: https://dev.mysql.com/downloads/workbench/
18. install mysql connector
    pip install mysql-connector-python
19. install mysql client
    pip install mysqlclient


1. replace YOUR_API_KEY with an openAI API key (at https://platform.openai.com/account/api-keys once you have an account)
2. replace YOUR_BUCKET_NAME with the name of your s3 bucket
3. run aws configure and enter your aws access key and secret key
4. run python app.py to start server
5. open a new terminal and run command below. replace {path_to_image} with the path of your image
curl -X POST -H 'Content-Type: multipart/form-data' -F 'image=@{path_to_image}' http://localhost:5000/ocr
