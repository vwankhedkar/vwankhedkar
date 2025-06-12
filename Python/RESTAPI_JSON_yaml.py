Link to learn - https://www.youtube.com/watch?v=T7kJUzMKqo0&list=PLrCERssHtW-iOPTrBkqy3QfkWU3ozgPGL&index=21


import requests
import json
url = "https://jsonplaceholder.typicode.com/posts/1"
request=requests.get(url=url)
print(type(request))
print(request.status_code)
<class 'requests.models.Response'>
200
**********************************************************
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts/1"
request=requests.get(url=url)
jsonres = request.json()
print(type(request))
code = request.status_code
assert code in [200,201]
print(json.dumps(jsonres, indent=4))
print(jsonres['id'])
print(jsonres['title'])
<class 'requests.models.Response'>
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
1
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
*********************************************************************************
import json
json_data = '[ {"studentid": 1, "name": "ABC", \
"subjects": ["Python", "Data Structures"]}, \
                {"studentid": 2, "name": "PQR",\
                "subjects": ["Java", "Operating System"]} ]'
obj = json.loads(json_data)
json_format = json.dumps(obj, indent=4)
print(json_format)
[
    {
        "studentid": 1,
        "name": "ABC",
        "subjects": [
            "Python",
            "Data Structures"
        ]
    },
    {
        "studentid": 2,
        "name": "PQR",
        "subjects": [
            "Java",
            "Operating System"
        ]
    }
]
***********************************************************
import requests
import json
url1 = "https://jsonplaceholder.typicode.com/posts/"
response = requests.get(url=url1,)
code=response.status_code
assert code == 200
print(type(response.json()))
list = response.json()
for i in range(0,len(list)):
    id=list[i]['id']
    if id==10:
        title = list[i]['title']
        print(title)
assert title=='optio molestias id quia eum',f"Title actual and title expected do not matches '{title}'"
<class 'list'>
optio molestias id quia eum
********************************************************************
import requests
import json
url1 = "https://httpbin.org/get"
response = requests.get(url=url1,)
assert response.status_code==200
jsonObject=response.json()
print(jsonObject['origin'])
host=jsonObject['headers']['Host']
host1="httpbin.org"
assert host==host1,f"Expected hostname '{host1}' is not matching with actual '{host}'"
OUTPUT --- 49.207.224.196
************************************************************
POST
import requests
import json
urlpost = "https://jsonplaceholder.typicode.com/posts/"
bodypost = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
headerpost = {'Content-type': 'application/json; charset=UTF-8'}
response = requests.post(url=urlpost,headers=headerpost,json=bodypost,)
status=response.status_code
print(status)
assert status==201
jsonObject=response.json()
print(jsonObject['id'])
201
101
*****************************************************************8
PUT
import requests
import json
urlpost = "https://jsonplaceholder.typicode.com/posts/"
bodypost = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
headerpost = {'Content-type': 'application/json; charset=UTF-8'}
response = requests.post(url=urlpost,headers=headerpost,json=bodypost,)
status=response.status_code
print(status)
assert status==201
jsonObject=response.json()
print(jsonObject['id'])
print(jsonObject)

urlpost = "https://jsonplaceholder.typicode.com/posts/1"
responseput = requests.put(url=urlpost,headers=headerpost,json=jsonObject,)
statusput = response.status_code
print(statusput)
print(responseput.json()['id'])
print(response.json())
201
101
{'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
201
1
{'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
****************************************************
import requests
import json
urlpost = "https://jsonplaceholder.typicode.com/posts/"
bodypost = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
headerpost = {'Content-type': 'application/json; charset=UTF-8'}
responsepost = requests.post(url=urlpost,headers=headerpost,json=bodypost,)
status=responsepost.status_code
print(status)
assert status==201
jsonObject=responsepost.json()
print(jsonObject['id'])
print(jsonObject)

urlpost = "https://jsonplaceholder.typicode.com/posts/1"
responseput = requests.put(url=urlpost,headers=headerpost,json=jsonObject,)
statusput = responseput.status_code
print(statusput)
print(responseput.json()['id'])
print(responseput.json())

urldelete = "https://jsonplaceholder.typicode.com/posts/1"
responsedelete = requests.delete(url=urldelete,)
print(responsedelete.status_code)
assert responsedelete.status_code==200
201
101
{'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 101}
200
1
{'title': 'foo', 'body': 'bar', 'userId': 1, 'id': 1}
200
*********************************************************
from textwrap import indent

import requests
import json
urlget = "https://httpbin.org/get"
responseget = requests.get(url=urlget,)
getjson=responseget.json()
codeget = responseget.status_code
print(codeget)
print(json.dumps(getjson,indent=2))

urlpost = "https://httpbin.org/post"
headerpost={'Content-Type': 'application/json'}
responsepost=requests.post(url=urlpost,headers=headerpost,)
statuspost=responsepost.status_code
print(statuspost)
assert statuspost==200
jsonObject=responsepost.json()
print(jsonObject['headers']['User-Agent'])

urlput = "https://httpbin.org/put"
changejson = {
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-6826f1bc-46bfdee36148da057a2769d4"
  },
  "origin": "49.49.49.196",
  "url": "https://httpbin.org/get"
}
responseput = requests.put(url=urlput,headers=headerpost,json=changejson,)
statusput = responseput.status_code
print(statusput)
print(responseput.json())

urldelete = "https://httpbin.org/delete"
headerdelete={'Content-Type': 'application/json'}
responsedelete=requests.delete(url=urldelete,headers=headerdelete,)
statusdelete=responsedelete.status_code
print(statusdelete)
assert statusdelete==200
jsonObject = responsedelete.json()
print(jsonObject['headers']['User-Agent'])

C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\RESTapi.py 
200
{
  "args": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.32.3",
    "X-Amzn-Trace-Id": "Root=1-6826f67f-3f03c45d77b864bc05536cf1"
  },
  "origin": "49.207.224.196",
  "url": "https://httpbin.org/get"
}
200
python-requests/2.32.3
200
{'args': {}, 'data': '{"args": {}, "headers": {"Accept": "*/*", "Accept-Encoding": "gzip, deflate", "Host": "httpbin.org", "User-Agent": "python-requests/2.32.3", "X-Amzn-Trace-Id": "Root=1-6826f1bc-46bfdee36148da057a2769d4"}, "origin": "49.49.49.196", "url": "https://httpbin.org/get"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '264', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-6826f682-5c0b26c04a03e9fe35a3c3dc'}, 'json': {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-6826f1bc-46bfdee36148da057a2769d4'}, 'origin': '49.49.49.196', 'url': 'https://httpbin.org/get'}, 'origin': '49.207.224.196', 'url': 'https://httpbin.org/put'}
200
python-requests/2.32.3
**********************************************************************
import requests
import json
token = 'abc'
url1 = "https://api.github.com/user"
headers={"Authorization": f"Bearer {token}"}
response = requests.get(url=url1, verify=False, headers=headers)
responseCode = response.status_code
print(responseCode)
assert responseCode==401
print(response.json())
C:\Python313\Lib\site-packages\urllib3\connectionpool.py:1097: InsecureRequestWarning: Unverified HTTPS request is being made to host 'api.github.com'. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#tls-warnings
  warnings.warn(
401
{'message': 'Bad credentials', 'documentation_url': 'https://docs.github.com/rest', 'status': '401'}
*************************************************************************
import requests
def monitor_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url} is UP")
        else:
            print(f"{url} might be DOWN")
    except requests.RequestException:
        print(f"{url} is unreachable")
url = "https://petstore.swagger.io/#/pet/getPetById"
monitor_website(url)
OUTPUT - https://petstore.swagger.io/#/pet/getPetById is UP
***********************************************************************
import json
with open("config.json") as f:
    data = json.load(f)
    print(data.get("app_name"))

config.json
{
  "app_name": "MyApplication",
  "version": "1.0.0",
  "author": "Vaishali",
  "debug": true
}
OUTPUT ------- MyApplication
***********************************************************************
import yaml
with open("config.yaml") as f:
    config = yaml.safe_load(f)
    print(config.get("version"))
    
config.yaml
app_name: MyApplication
version: 1.0.0
author: Vaishali
debug: true
OUTPUT    -------->    1.0.0
