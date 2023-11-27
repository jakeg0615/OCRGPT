# OCRGPT

How to run

1. replace YOUR_API_KEY with an openAI API key (at https://platform.openai.com/account/api-keys once you have an account)
2. run python app.py to start server
3. open a new terminal and run command below. replace {path_to_image} with the path of your image
curl -X POST -H 'Content-Type: multipart/form-data' -F 'image=@{path_to_image}' http://localhost:5000/ocr

Sample file to work with: 
[phirefly_07-12-2023.pdf](https://github.com/jakeg0615/OCRGPT/files/13481401/phirefly_07-12-2023.pdf)
