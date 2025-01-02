import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eddr = eaddr
    def display(self):
        print('Eno: {}, Ename: {}, Esal: {}, Eaddr: {}'.format(self.eno, self.ename, self.esal, self.eddr))
e = Employee(100,'Vais',1000,'Bangalore')

# Serialization or pickling
with open('emp.ser','wb') as f:
    pickle.dump(e, f)
print("Pickling of Employee object completed")

#Deserialization or unpickling
with open('emp.ser','rb') as f:
    newobj = pickle.load(f)
print("Unpickling of employee object completed")
print("Printing Employee information...")
newobj.display()
OUTPUT
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
Pickling of Employee object completed
Unpickling of employee object completed
Printing Employee information...
Eno: 100, Ename: Vais, Esal: 1000, Eaddr: Bangalore

Process finished with exit code 0
***********************************************************************************************************
import json
employee={ 'name': 'Vais',
           'age': 42,
           'Salary': 1000.0,
           'ismarried': False,
           'ishavefriend': False
           }
json_string = json.dumps(employee,indent=4)
print(json_string)
with open('emp.json','w') as f:
    json.dump(employee,f,indent=4)

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
{
    "name": "Vais",
    "age": 42,
    "Salary": 1000.0,
    "ismarried": false,
    "ishavefriend": false
}

********************************************************************************************************************
Serilization
import json
json_string = '''{ 
           "name": "Vais",
           "age": 42,
           "salary": 1000.0,
           "ismarried": false,
           "ishavefriend": null
}'''
emp_dict = json.loads(json_string)
print(type(emp_dict))
print('Employee Name: ',emp_dict['name'])
print('Employee Age: ',emp_dict['age'])
print('Employee Salary: ',emp_dict['salary'])
print('Is Employee married: ',emp_dict['ismarried'])
print('Is Employee has Friend: ',emp_dict['ishavefriend'])

for k,v in emp_dict.items():
    print('{} : {}'.format(k,v))

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
<class 'dict'>
Employee Name:  Vais
Employee Age:  42
Employee Salary:  1000.0
Is Employee married:  False
Is Employee has Friend:  None
name : Vais
age : 42
salary : 1000.0
ismarried : False
ishavefriend : None

*******************************************************************************************************************
De-serilization
import json
with open('emp.json','r') as f:
    emp_dict=json.load(f)
print(type(emp_dict))
print('Employee Name: ',emp_dict['name'])
print('Employee Age: ',emp_dict['age'])
print('Employee Salary: ',emp_dict['salary'])
print('Is Employee married: ',emp_dict['ismarried'])
print('Is Employee has Friend: ',emp_dict['ishavefriend'])
for k,v in emp_dict.items():
    print("{} : {}".format(k,v))
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
<class 'dict'>
Employee Name:  Vais
Employee Age:  42
Employee Salary:  1000.0
Is Employee married:  False
Is Employee has Friend:  False
name : Vais
age : 42
salary : 1000.0
ismarried : False
ishavefriend : False
*****************************************************************************************************************
import json
import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
print(type(response))
bitcoininfo=response.json()
print(type(bitcoininfo))
print(bitcoininfo)
print('Bitcoinn price as on:',bitcoininfo['time']['updated'])
print('In USD:',bitcoininfo['bpi']['USD']['rate'])
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
<class 'requests.models.Response'>
<class 'dict'>
{'time': {'updated': 'Jan 2, 2025 10:09:27 UTC', 'updatedISO': '2025-01-02T10:09:27+00:00', 'updateduk': 'Jan 2, 2025 at 10:09 GMT'}, 'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org', 'chartName': 'Bitcoin', 'bpi': {'USD': {'code': 'USD', 'symbol': '&#36;', 'rate': '97,123.068', 'description': 'United States Dollar', 'rate_float': 97123.0681}, 'GBP': {'code': 'GBP', 'symbol': '&pound;', 'rate': '77,453.704', 'description': 'British Pound Sterling', 'rate_float': 77453.7043}, 'EUR': {'code': 'EUR', 'symbol': '&euro;', 'rate': '93,177.055', 'description': 'Euro', 'rate_float': 93177.055}}}
Bitcoinn price as on: Jan 2, 2025 10:09:27 UTC
In USD: 97,123.068
