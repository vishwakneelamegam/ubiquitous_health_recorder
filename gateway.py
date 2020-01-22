import requests
import json
import time
from workmateFileService import *
#-----GATEWAY-----
class gatewayService:
    def process(self,data):
        try:
            headers = {'Content-Type': 'application/json',}
            listsOfKey = ["id","proof","data"]
            dictionary = json.loads(data)
            k = dictionary.keys()
            if len(set(k) & set(listsOfKey)) == len(listsOfKey):
                response = requests.post('http://"your_ip"/get', headers=headers, data=data)
                return response.text
            else:
                return False
        except Exception as e:
            fileObject = fileService()
            fileObject.write_file("gatewayError",str(e))
            return "error"
data = '{"id":"your_id","proof":"your_proof","data":"data"}'
obj = gatewayService()
print(obj.process(data))
