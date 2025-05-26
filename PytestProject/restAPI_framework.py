test_basics.py

import requests, json
baseURL = 'https://petstore.swagger.io/v2/pet/'
petID = '151'

def test_addNewPet():
    url = baseURL
    header = {'Content-Type': 'application/json'}
    payload = {"id":petID, "name":"doggie", "status":"available"}
    response = requests.post(url, verify=False, json=payload,headers=header)
    data = response.json()
    assert data["id"] == 151
    assert len(data) > 0, 'Failed to push new data'
    print(data)

def test_getPetById_response():
    url = baseURL+petID
    header = {'Content-Type': 'application/json'}
    print("RequestURL :", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    print(json.dumps(data, indent=3))
    assert len(data) > 0, 'empty response'

def test_getPetById_id():
    url = baseURL + petID
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.get(url, verify=False, headers=header)
    data = response.json()
    assert data["id"] == 151, 'No Id present'
---------------------------------------------------------------------------
pytest.ini
[pytest]
filterwarnings =
    ignore:Unverified HTTPS request is being made:urllib3.exceptions.InsecureRequestWarning
-----------------------------------------------------------------------------
myutils.py

import json, requests


def getAPIData(url):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    response = requests.get(url, verify=False, headers=header)

    print("Raw Response:", response.text)
    data = response.json()
    assert len(data) > 0, 'empty response!'
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

def putData(url, payload):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    print("ReqBody: ", json.dumps(payload))
    response = requests.put(url, json=payload, headers=header)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken

def deleteData(url, opHeader=None):
    header = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)
    header = (header | opHeader) if isinstance(opHeader, dict) else header
    response = requests.delete(url, verify=False, headers=header)
    print(response.request.headers)
    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response, timeTaken
  --------------------------------------------------------------------------------
test_pets.py

from utils.myutils import *
from utils.myconfigparser import *

# baseURL = 'https://petstore.swagger.io/v2/pet/'
petID = "191"
baseURL = getPetAPIURL()

def test_getPetById_response():
    url = baseURL + petID
    data, rep_status, timeTaken = getAPIData(url)
    assert data['id'] == int(petID)
    assert rep_status == 200
    print("Time Taken: ", timeTaken)

def test_updatingPet():
    payload = {
        "id": int(petID),
        "name": "Cutie",
        "status": "pending",
        "photoUrls": ["http://example.com/photo1.jpg"]  # required field
    }
    data, resp_status, timeTaken = putData(baseURL, payload)
    print("Response data:", data)
    print("Response status:", resp_status)
    print("Time taken:", timeTaken)
    assert resp_status == 200
    assert 'id' in data, f"'id' not in response. Got: {data}"
    assert data['id'] == int(petID)

def test_deletePetById():
    url = baseURL + petID
    apiKey = {'apikey': 'apiKeys123'}
    data, resp_status, timeTaken = deleteData(url, apiKey)
    print(data)
    assert data['message'] == petID
    assert data['code'] == 200
  ---------------------------------------------------------------------------
myconfigparser.py

import configparser
from pathlib import Path

cfgFile = 'petsaqa.ini'
cfgFileDir = 'config'

# Instantiate ConfigParser
config = configparser.ConfigParser()

# Resolve full path
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)

# Read the config file
config.read(CONFIG_FILE)

def getPetAPIURL():
    return config['pet']['url']

def getStoreAPIUrl():
    return config['store']['url']
---------------------------------------------------------------------------
petsqa.ini

[pet]
url=https://petstore.swagger.io/v2/pet/
port=
username=

[store]
url=https://petstore.swagger.io/order/order



