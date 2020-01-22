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
                response = requests.post('http://54.80.52.75/get', headers=headers, data=data)
                return response.text
            else:
                return False
        except Exception as e:
            fileObject = fileService()
            fileObject.write_file("gatewayError",str(e))
            return "error"
data = '{"id":"pandi","proof":"1256","data":"he has fever"}'
obj = gatewayService()
print(obj.process(data))
