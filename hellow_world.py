import requests
from requests.structures import CaseInsensitiveDict
print("*"*30)
url = "https://hooks.slack.com/services/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"
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
data ='{"from":"pycharm"}'
req_post_response = requests.post(url,headers=headers,data=data)
print(req_post_response.status_code)
print("*"*30)



print("Hello World")
from datetime import datetime
print("Hello Again ",datetime.now())
print(str(datetime.now()))
#for func in list(dir(datetime)):
    #print(func)