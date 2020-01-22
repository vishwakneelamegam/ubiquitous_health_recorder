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
