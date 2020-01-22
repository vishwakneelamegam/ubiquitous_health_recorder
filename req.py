import requests
import time
s = time.time()
headers = {
    'Content-Type': 'application/json',
}
#data ='{"name":"asdf"}'
data = '{"id":"pandi","proof":"1256","data":"he has fever"}'
#data = '{"id":"abc","phone":"67890","key":"3d1ef8aedb2bc4c0239e3652e64e287b"}'
#data = "hello"
response = requests.post('http://localhost/gateway', headers=headers, data=data)
print (response.text)
e = time.time() - s
print(str(e))
