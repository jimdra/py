import json
from werkzeug.security import generate_password_hash, check_password_hash
import requests
headers = {'content-type': 'application/json'}
ret = requests.post('http://127.0.0.1:5000/users/add', headers=headers, data=json.dumps({'username': 'admin','password': 'admin123','nickname': '管理员'}))
print(ret.json())

