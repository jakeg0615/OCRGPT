# OCRGPT

How to run

1. run python app.py to start server
2. open a new terminal and run command below. replace {path_to_image} with the path of your image

curl -X POST -H 'Content-Type: multipart/form-data' -F 'image=@{path_to_image}' http://localhost:5000/ocr
