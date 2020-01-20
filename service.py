import json
from recordService import *
from flask import Flask
from flask import Flask, request
from flask import Response
from flask_cors import CORS
#---uhr---
class uhr:
    def services(self,jsonData,types):
        try:
           data = {}
           fileObject = fileService()
           if types == "get":
              data["result"] = list(map(lambda x:json.loads(x.strip("\n")),fileObject.read_file(str(jsonData["id"]))))
              return json.dumps(data)
           if types == "put":
              if(fileObject.write_file(str(jsonData["id"]),json.dumps(jsonData)) == True):
                 data["result"] = "updated"
                 return json.dumps(data)
              else:
                 data["result"] = "not updated"
                 return json.dumps(data)
           else:
              data["result"] = "error"
              return json.dumps(data)
        except Exception as e:
           data["result"] = "error"
           return json.dumps(data)
#---FLASK---
app = Flask(__name__)
CORS(app)
@app.route('/<types>', methods=['GET','POST'])
def plan_input(types):
    jsonData = request.get_json()
    uhrObject = uhr()
    return str(uhrObject.services(jsonData,str(types)))
if __name__ == '__main__':
    port = int(os.getenv('PORT',80))
    app.run(host='0.0.0.0',port=port,threaded=True)