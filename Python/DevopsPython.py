def memoize(fn):
    cache = {}
    def helper(x):
        if x not in cache:
            # The @memoize decorator is used to cache the results of the factorial function. 
            cache[x] = fn(x)
        return cache[x]
    return helper
@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(3)
print(result)    ===>  6
***********************************************************************
def caesar_cipher(text, shift) :
    result = ""
    for char in text:
        if char.isalpha() :
            # Determine if the character is uppercase or lowercase
            is_upper = char. isupper()
            char = char.lower() # Convert to lowercase for shifting
            shifted = chr(((ord(char) - ord('a' ) + shift) % 26) + ord( 'a' ))
            if is_upper:
                shifted = shifted.upper() # Convert back to uppercase
                result += shifted
            else:
                result += char # Non-alphabet characters remain unchanged
    return result
# Example usage:
text = "Hello, World! "
shift = 3
encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, -shift)
print("Original: " , text)
# Original: Hello, World!
print("Encrypted: " , encrypted)
print("Decrypted: ", decrypted) # Decrypted: Hello, World!
C:\Users\vwank\PycharmProjects\Python_Cucumber\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\Python_Cucumber\.venv\Scripts\tryPyProgs.py 
Original:  Hello, World! 
Encrypted:  KelloZorld
Decrypted:  HelloWorld
************************************************************************************************
class Singleton:
    _instance = None  # Use _instance consistently
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
singleton_1 = Singleton()
singleton_2 = Singleton()
print(singleton_1 is singleton_2)  # ✅ Output: True
************************************************************************************************
# public variable
class MyClass1:
    def __init__(self):
        self.public_variable = "This is public."
obj = MyClass1()
print(obj.public_variable)
# Protected variable
class Myclass2:
    def __init__(self):
        self._protected_variable = "This is protected variable"
class subClass(Myclass2):
    def print_protected(self):
        print(self._protected_variable)
obj = subClass()
obj.print_protected()
# Private
class MyClass3:
    def __init__(self):
        self.__private_variable = "This is private variable"
    def get_private_variable(self):
        return self.__private_variable
obj = MyClass3()
print(obj.get_private_variable())
This is public.
This is protected variable
This is private variable
************************************************************************************************
def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high  and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else -1
        pos = low + (target - arr[low]) * (high - low) // (arr[high] - arr[low])
        if arr[pos] == target:
            return pos
        low = pos+1 if arr[pos] < target else low
        high = pos-1 if arr[pos] > target else high
    return -1
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12
result = interpolation_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
Element 12 found at index 5
************************************************************************************************
file_path = "output.txt"
file_path1 = "logfile.txt"
buffer_size = 8192
with open(file_path, 'rb') as file:
    while True:
        data = file.read(buffer_size)
        if not data:
            break
        print(data)
        with open(file_path1, 'wb') as file1:
            file1.write(data)
b'From: abc@gmail.com\r\nFrom: abc1@gmail.com\r\nFrom: abc2@gmail.com\r\nFrom: vais@gmail.com\r\nFrom: wan@gmail.com\r\nThis is first line\r\nThis is second line\r\n'
*************************************************************************
def build_pyramid(height):
    for i in range(1, height+1):
        spaces = ' ' * (height-i)
        stars = '*' * (2 * i -1)
        print(spaces + stars)
pyramid_height = 5
build_pyramid(pyramid_height)
    *
   ***
  *****
 *******
*********
*************************************************************************
import time
class TimerContext:
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_val, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f'Time elapsed : {elapsed_time} seconds')
with TimerContext():
    for _ in range(10000):
        pass
Time elapsed : 0.00024127960205078125 seconds
*************************************************************************
import requests
import os
# URL of the image to download
image_url = "https://example.com/image.jpg"
response = requests.get(image_url)
if (response.status_code == 200):
    image_data = response.content
    local_image_path = "img.jpg"
    with open(local_image_path, 'wb') as local_file:
        local_file.write(image_data)
else:
    print(f"Failed to download image. status code {response. status_code}")
*************************************************************************
import os
def custom_walk(top) :
    for root, dirs, files in os.walk(top):
        yield root, dirs, files
# Example usage:
directory = "C:\\Users\\vwank\\PycharmProjects\\PytestFramework\\Python_Codes\\"
for root, dirs, files in custom_walk(directory) :
    print(f"Directory: {root}")
    print(f"Subdirectories: {dirs}")
    print(f"Files: {files}")
    print()
Directory: C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\
Subdirectories: ['log', '__pycache__']
Files: ['config.json', 'config.yaml', 'data.csv', 'example.db', 'example.txt', 'file.py', 'iterables.py', 'logfile.txt', 'output.csv', 'output.txt', 'py.ini', 'try.py']

Directory: C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\log
Subdirectories: []
Files: ['pytesting.log']

Directory: C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\__pycache__
Subdirectories: []
Files: ['try.cpython-312.pyc', 'try.cpython-313-pytest-8.3.5.pyc']
************************************************************************************************
file = open('example.txt','a')
file.write("Hello World !")
# file.close()
file = open('example.txt','r')
content = file.read()
print(content)
# file.close()
with open('example.txt','r'):
    content = file.read()
    print(content)
************************************************************************************************
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/createJira', methods=['POST'])
def create_jira():
    # Replace with your real JIRA info — but NEVER hardcode API tokens in code
    jira_url = "https://mdsajid020.atlassian.net/rest/api/3/issue"
    api_token = "YOUR_API_TOKEN_HERE"  # 🔒 Use environment variable instead
    auth = HTTPBasicAuth("mdsajid020@gmail.com", api_token)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = {
        "fields": {
            "project": {"id": "10000"},
            "summary": "Main order flow broken",
            "issuetype": {"id": "10001"},
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {"type": "text", "text": "Order entry fails when selecting supplier."}
                        ]
                    }
                ]
            }
        }
    }
    response = requests.post(
        jira_url,
        data=json.dumps(payload),
        headers=headers,
        auth=auth
    )
    # Return JSON response
    try:
        return jsonify(response.json()), response.status_code
    except Exception:
        return jsonify({"error": "Invalid response from JIRA", "details": response.text}), 500
if __name__ == '__main__':
    # Run Flask on port 5000
    app.run(host='0.0.0.0', port=5000)
************************************************************************************************

************************************************************************************************
************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************
