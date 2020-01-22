import requests
import time
s = time.time()
headers = {
    'Content-Type': 'application/json',
}
data = '{"id":"your_id","proof":"your_proof","data":"data"}'
response = requests.post('http://localhost/gateway', headers=headers, data=data)
print (response.text)
e = time.time() - s
print(str(e))
