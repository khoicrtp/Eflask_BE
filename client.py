from io import BytesIO
import requests
import json
import base64
import json

def encodeImage(filename):
    with open(filename, "rb") as image_file:
        byte_string = base64.b64encode(image_file.read())
    f = open(filename.split('.', 1)[0] + '.txt', 'wb')
    f.write(byte_string)
    # return byte_string

#BASE = "http://127.0.0.1:5000/"
BASE = "https://eflask-crypto-image.herokuapp.com/"
#json_data = json.dumps({'username':'suir2', 'password': 'a', 'confirm_password': 'a', 'publickey': '638'})
#response = requests.post(BASE + "users/register/", json=json_data)
#response = requests.get(BASE + "users/login/", json=json_data)
# response = requests.get(BASE + "/blank")
# encodeImage('abc.png')
# json_data = json.dumps({'username':'suir2', 'password': 'a', 'confirm_password': 'a', 'publickey': '638'})
# files = {'file': open('abc.txt', 'rb')}
# response = requests.post(BASE + "suir2/abc.png/", files=files)
#response = requests.get(BASE + "/")
# response = requests.get(BASE + "suir2/images/")
# print(vars(response))
# # if response.json():
# #     print(response.json())
# print(response.files)
#print(response)
# user = [('suir', 'password', 'key')]
# print(user[0][1])