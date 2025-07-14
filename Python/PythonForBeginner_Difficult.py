Advanced String Formatting (f-strings
name = "Vaishali"
age = 25
print(f"{name} will get {age+5} old in more years")

width = 5
height = 10
print(f"The area of rectangle is {width * height}")

pi = 3.14156
print(f"Pi rounded to decimal places is: {pi:.2f}")
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Vaishali will get 30 old in more years
The area of rectangle is 50
Pi rounded to decimal places is: 3.14
*******************************************************************************
Command-Line Interfaces (argparse)
import argparse
parser = argparse.ArgumentParser(description="A Simple CLI Tool")
parser.add_argument("--name", type=str, help="Enter your name.")
args = parser.parse_args()
print(f"Hello, {args.name}!")
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes> python try.py --name John
Hello, John!
*******************************************************************************
py.ini
[DEFAULT]
Setting = Enabled
Tests: [smoke, sanity, regression]

ConfigParser
import configparser
config = configparser.ConfigParser()
config.read("py.ini")
print(config["DEFAULT"]["Setting"])
print(config["DEFAULT"]["Tests"])
*******************************************************************************
Type Hinting
def add(a:int, b:int) -> int:
    return a+b
print(add(5,6))  ---- 11
*******************************************************************************
YAML Files
import yaml
data = {"name":"Vaishali", "age":25}
yaml_string=yaml.dump(data)
print(yaml_string)
age: 25
name: Vaishali
*******************************************************************************
Custom Exceptions
class CustomError(Exception):
    pass
try:
    raise CustomError("An custom error occurred!")
except CustomError as e:
    print(e)      ------   An custom error occurred!
*******************************************************************************
Asyncio (Asynchronous Programming)
The asyncio module allows you to write code that can perform tasks while waiting for something else to finish (like reading a file or 
making a network request). This makes your program more efficient because it can do other work instead of waiting.
import asyncio
# Asynchronous function that sleeps for 1 second and then prints a message
async def greet():
    await asyncio.sleep(1)
    print("Hello, Async!")
# Run the asynchronous function
asyncio.run(greet())
OITPUT -------  Hello, Async!
*******************************************************************************
Multiprocessing
from multiprocessing import Process
def print_numbers():
    for i in range(5):
        print(i, end=' ')
if __name__ == "__main__":
    process = Process(target=print_numbers)
    process.start()
    process.join()
OUTPUT --------  0 1 2 3 4 
*******************************************************************************
Working with HTML and Web Scraping (BeautifulSoup)
from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.gmail.com")
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
/signin/usernamerecovery?continue=https://mail.google.com/mail/u/0/&dsh=S1778719601:1748432930485946&emr=1&flowEntry=ServiceLogin&flowName=WebLiteSignIn&followup=https://mail.google.com/mail/u/0/&ifkv=AdBytiOLZT_mucq_xNXeA-SdAUxo_xfXDxfZIwjqauhlnmPNxcD-omi7lGR-4kHTE8NgZdn1xOuJiA&osid=1&service=mail
https://support.google.com/accounts?p=signin_privatebrowsing&hl=en-US
/lifecycle/flows/signup?continue=https://mail.google.com/mail/u/0/&dsh=S1778719601:1748432930485946&emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&ifkv=AdBytiOLZT_mucq_xNXeA-SdAUxo_xfXDxfZIwjqauhlnmPNxcD-omi7lGR-4kHTE8NgZdn1xOuJiA&osid=1&service=mail
https://support.google.com/accounts?hl=en-US&p=account_iph
https://accounts.google.com/TOS?loc=IN&hl=en-US&privacy=true
https://accounts.google.com/TOS?loc=IN&hl=en-US
*******************************************************************************
Working with APIs (Requests Library
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
data={"name":"Vais","age":35}
response1 = requests.post("https://api.github.com",json=data)
print(response1.status_code)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
200
{'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}', 'notifications_url': 'https://api.github.com/notifications', 'organization_url': 'https://api.github.com/orgs/{org}', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_teams_url': 'https://api.github.com/orgs/{org}/teams', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'topic_search_url': 'https://api.github.com/search/topics?q={query}{&page,per_page}', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}
404
*******************************************************************************
Working with SQLite (Database)
import sqlite3
# Connect to the database (or create if it doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()
# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# Insert a record
cursor.execute("INSERT INTO users(name, age) VALUES('VAIS', 35)")
# Commit the changes
conn.commit()
# Fetch and print all records
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())  # ← call the method here
cursor.execute("DROP TABLE users")
# Close the connection
conn.close()
OUTPUT   ---------------  [(1, 'VAIS', 35)]
*******************************************************************************
Handling Large Data with Panda
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
print(df['name'])
print(df[df["age"]>30])
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35
0      Alice
1        Bob
2    Charlie
Name: name, dtype: object
      name  age
2  Charlie   35
*******************************************************************************
Working with CSV Files
data.csv
['name', 'age']
['Alice', '25']
['Bob', '30']

csv.py
import csv
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
["['name'", " 'age']"]
["['Alice'", " '25']"]
["['Bob'", " '30']"]
---------------------------------------------------
import csv
data = [["name", "age"],["Vais", 30],["Sumit", 20]]
with open('output.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    file.close()
with open('output.csv','r') as file:
    reader = csv.reader(file)
    for rows in reader:
        print(rows)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
['name', 'age']
['Vais', '30']
['Sumit', '20']
*******************************************************************************
Handling JSON Data
#Convert Python objects to JSON
import json
person = {"name":"Vais", "age":30}
json_data = json.dumps(person)
print(json_data)

# Convert JSON to Python objects
json_data1 = '{"name":"Vais", "age":30}'
json_string = json.loads(json_data1)
print(json_string)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
{"name": "Vais", "age": 30}
{'name': 'Vais', 'age': 30}
*******************************************************************************
Multi-threading
import threading
def print_num():
    for i in range(5):
        print(i, end=' ')
# Create two threads
thread1 = threading.Thread(target=print_num())
print("\n")
thread2 = threading.Thread(target=print_num())
# Start the threads
thread1.start()
thread2.start()
# Wait for both threads to finish
thread1.join()
thread2.join()
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
0 1 2 3 4 

0 1 2 3 4 
*******************************************************************************
monkey patching
import math
math.sqrt = lambda x: "Patched!"
print(math.sqrt(4))        ---->         Patched!

Python data classes

from dataclasses import dataclass
@dataclass()
class Employee:
    name: str
    age: int
    role: str = "Analyst"
emp = Employee
print(emp.role)        ------>    Analyst

Magic methods (or dunder methods) 
class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"
b = Book("Python Basics")
print(b)    ------>        Book: Python Basics

super() function
class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")
Child().greet()
Hello from Parent
Hello from Child
*******************************************************************************
Method Overloading
class Math:
    def add(self,a,b=0):
        return a+b
m = Math()
print(m.add(5))
print(m.add(5,10))
5
15

Method Overriding
class Parent:
    def greet(self):
        print("Hello from Parent")
class Child(Parent):
    def greet(self):
        print("Hello from Child")
c = Child()
c.greet()        -------->    Hello from Child

generator expression and a list comprehension
gen = (x**2 for x in range(10))
lst = [x**2 for x in range(10)]
print("gen : ", list(gen))
print("lst : ", lst)
gen :  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
lst :  [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
*******************************************************************************
weak references - allows one object to refer to another object without increasing its reference count. When the original object
is no longer needed elsewhere, it can be garbage collected—even if a weak reference to it still exists.

import weakref
class MyClass:
    pass
obj = MyClass()
weak_obj = weakref.ref(obj)
print(weak_obj())
del obj
print(weak_obj())
<__main__.MyClass object at 0x0000019251329E20>
None
*******************************************************************************
n = int(input("Enter input: "))
is_prime=True
if (n<1):
    print("It's not prime number")
for i in range(2,n):
    if (n%i == 0):
        is_prime = False
        break
if is_prime == True:
    print("It's prime number")
else:
    print("It's not prime number")
    
OUTPUT:
------
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
Enter input: 5
It's prime number
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
Enter input: 6
************************************************************************************************************
n = int(input("Enter Input: "))
n1 = 2
while (n1 <= n):
    is_prime = True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime = False
            break
    if is_prime==True:
        print(n1, end =' ')
    n1 = n1 + 1
    
 Enter Input: 5
 2 3 5 
************************************************************************************************************
def is_prime(num):
    # check is number is less than 2
    if num<2:
        return False
    # check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    # if no factors are found number is prime
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} Number is prime")
else:
    print(f"{num} Number is not prime")

OUTPUT - Enter a number: 5
5 Number is prime
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
