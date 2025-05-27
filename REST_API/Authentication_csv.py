
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

url = 'https://httpbin.org/digest-auth/abc/123/123/MD5'
auth = HTTPDigestAuth('123', '123')
def test_basicAuth():
    headers = {'Accept': 'application/json'}
    r = requests.get(url, auth=auth, verify=False)
    print(r.status_code)
(.venv) PS C:\Users\vwank\PycharmProjects\PytestFramework\AppPetsStoreTests> pytest -v -s .\test_authentics.py
=============================================================== test session starts ===============================================================
platform win32 -- Python 3.13.1, pytest-8.3.5, pluggy-1.5.0 -- C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\vwank\PycharmProjects\PytestFramework
configfile: pytest.ini
collected 1 item                                                                                                                                   

test_authentics.py::test_basicAuth 200
PASSED

================================================================ 1 passed in 2.02s ================================================================ 
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
*********************************************************
registerAPIData.csv
email,password
auto1@auto,1234
auto2@auto,1234
auto3@auto,1234
auto4@auto,1234
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\utils\fileUtils.py 
C:\Users\vwank\PycharmProjects\PytestFramework
--------------
[{'email': 'auto1@auto', 'password': '1234'}, {'email': 'auto2@auto', 'password': '1234'}, {'email': 'auto3@auto', 'password': '1234'}, {'email': 'auto4@auto', 'password': '1234'}]

Different approach to read file
-----------------------------
from utils.fileUtils import getCsvDataAsDict
datafile = 'registerAPIData.csv'
def getDataDrivenApi():
    payloadList = getCsvDataAsDict()
    for dataLines in payloadList:
        print(dataLines)
      

