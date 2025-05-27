user_info.json
{
    "name": "Udemy user1",
    "email": "user1@example.com",
    "phone": "123-456-7890"
}

fileutils.py
import json

def update_user_info(file_name, name=None, email=None, phone=None):
    with open(file_name, 'r') as file:
        user_info = json.load(file)

    if name is not None:
        user_info['name'] = name
    if email is not None:
        user_info['email'] = email
    if phone is not None:
        user_info['phone'] = phone

    return user_info
******************************************************
email,password
auto1@auto,1234
auto2@auto,1234
auto3@auto,1234
auto4@auto,1234
          
fileutils.py    
import csv
import json
from pathlib import Path
import random
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
TEST_DATA_DIR = BASE_DIR.joinpath('TestData')
def getJsonFromFile(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath,'r') as file:
        return json.load(file)

def getCsvDataAsDict(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as file:
        csvFile = csv.DictReader(file)
        dictList = list(csvFile)
    return dictList
print("--------------")
print(getCsvDataAsDict('registerAPIData.csv'))

def getDataAsList(filename):
    filepath = TEST_DATA_DIR.joinpath(filename)
    with open(filepath, 'r') as csvFile:
        reader = csv.reader(csvFile)
        next(reader)
        lines = list(reader)
    return lines
print("--------------")
print(getDataAsList('registerAPIData.csv'))


C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\utils\fileUtils.py 
C:\Users\vwank\PycharmProjects\PytestFramework
--------------
[{'email': 'auto1@auto', 'password': '1234'}, {'email': 'auto2@auto', 'password': '1234'}, {'email': 'auto3@auto', 'password': '1234'}, {'email': 'auto4@auto', 'password': '1234'}]
--------------
[['auto1@auto', '1234'], ['auto2@auto', '1234'], ['auto3@auto', '1234'], ['auto4@auto', '1234']]

