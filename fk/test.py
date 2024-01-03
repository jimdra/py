import requests

ret = requests.post('http://127.0.0.1:5000/users/login', data={'username': 'admin'})
print(ret)
