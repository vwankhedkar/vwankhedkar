import requests
url = "https://www.google.com/search?q=pytest"
r = requests.get(url)
print(r.status_code)

url = "https://httpbin.org/get"
r = requests.get(url)
print(r.status_code)
print(r.headers)
print(r.request.headers)
print(r.text)
print(r.json())
print(r.headers['Content-Type'])
200
200
{'Date': 'Thu, 22 May 2025 11:28:18 GMT', 'Content-Type': 'application/json', 'Content-Length': '307', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.3", 
    "X-Amzn-Trace-Id": "Root=1-682f0a51-0ce36699055b25fb5a3ce67a"
  }, 
  "origin": "49.207.217.28", 
  "url": "https://httpbin.org/get"
}

{'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-682f0a51-0ce36699055b25fb5a3ce67a'}, 'origin': '49.207.217.28', 'url': 'https://httpbin.org/get'}
application/json
**************************************************************************************
import requests
URL = "https://httpbin.org/get"
myparams = {"key1":"value1", "key2":"value2"}
r = requests.get(URL, params=myparams)
print(r.url)
for key, value in r.json().items():
    print(key, ":", value)
print(r.json()["headers"]["Host"])
https://httpbin.org/get?key1=value1&key2=value2
args : {'key1': 'value1', 'key2': 'value2'}
headers : {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-682f10f9-3d9679f3606737d50703c82f'}
origin : 49.207.217.28
url : https://httpbin.org/get?key1=value1&key2=value2
httpbin.org
***************************************************************************************
import json

import requests
URL = "https://httpbin.org/get"
myparams = {"key1":"value1", "key2":"value2"}
r = requests.get(URL, params=myparams)
print(r.url)
for key, value in r.json().items():
    print(key, ":", value)
print(r.json()["headers"]["Host"])
print("**********************************************")

URL = "https://httpbin.org/post"
payload = {"key1":"value1", "key2":"value2"}
r = requests.post(URL, json=payload)
print(r.url)
print(r.status_code)
print(r.text)
print("**********************************************")

URL = "https://httpbin.org/post"
payload = {"key1":"value1", "key2":"value2"}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
r = requests.post(URL, data=json.dumps(payload), headers=headers)
# requests.post(URL, json=payload, headers=headers)
print(r.url)
print(r.status_code)
print(r.text)
print(r.request.headers)
print(r.headers)

https://httpbin.org/get?key1=value1&key2=value2
args : {'key1': 'value1', 'key2': 'value2'}
headers : {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.32.3', 'X-Amzn-Trace-Id': 'Root=1-682f1566-3d4be3ce719921250f5994a7'}
origin : 49.207.217.28
url : https://httpbin.org/get?key1=value1&key2=value2
httpbin.org
**********************************************
https://httpbin.org/post
200
{
  "args": {}, 
  "data": "{\"key1\": \"value1\", \"key2\": \"value2\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "36", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.3", 
    "X-Amzn-Trace-Id": "Root=1-682f1568-36415ba35b628a5548cc24d9"
  }, 
  "json": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "origin": "49.207.217.28", 
  "url": "https://httpbin.org/post"
}

**********************************************
https://httpbin.org/post
200
{
  "args": {}, 
  "data": "{\"key1\": \"value1\", \"key2\": \"value2\"}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "application/json", 
    "Accept-Encoding": "gzip, deflate", 
    "Content-Length": "36", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.32.3", 
    "X-Amzn-Trace-Id": "Root=1-682f1568-13c0de5e537d39e6179d0106"
  }, 
  "json": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "origin": "49.207.217.28", 
  "url": "https://httpbin.org/post"
}

{'User-Agent': 'python-requests/2.32.3', 'Accept-Encoding': 'gzip, deflate', 'accept': 'application/json', 'Connection': 'keep-alive', 'Content-Type': 'application/json', 'Content-Length': '36'}
{'Date': 'Thu, 22 May 2025 12:15:36 GMT', 'Content-Type': 'application/json', 'Content-Length': '543', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
