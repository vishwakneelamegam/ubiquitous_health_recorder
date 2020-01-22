import requests
import json
import os
from flask import Flask
from flask import Flask, request
from flask import Response
from flask_cors import CORS
from recordService import *
#-----GATEWAY-----
class gatewayService:
    def process(self,data):
        try:
            fileObject = fileService()
            headers = {'Content-Type': 'application/json',}
            listsOfKey = ["id","proof","data"]
            k = data.keys()
            if len(set(k) & set(listsOfKey)) == len(listsOfKey):
                response = requests.post('http://your_ip/get', headers=headers, data=data)
                fileObject.write_file("gatewayLogs","Data : " + str(data))
                return response.text
            else:
                fileObject.write_file("gatewayError","(1) Error : " + str(data) + " Exception : wrong keys")
                return False
        except Exception as e:
            fileObject = fileService()
            fileObject.write_file("gatewayError","(2) Error : " + str(data) + " Exception : "  + str(e))
            return "error"
#---FLASK---
app = Flask(__name__)
CORS(app)
@app.route('/<types>', methods=['GET','POST'])
def plan_input(types):
    jsonData = request.get_json()
    if types == "gateway":
        obj = gatewayService()
        return obj.process(jsonData)
    else:
        fileObject = fileService()
        fileObject.write_file("gatewayError","(3) Error : " + str(types) + " Data : "  + str(jsonData))
        return "error"
if __name__ == '__main__':
    port = int(os.getenv('PORT',80))
    app.run(host='0.0.0.0',port=port,threaded=True)
