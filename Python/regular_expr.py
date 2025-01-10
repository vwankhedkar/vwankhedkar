import re

str = "Iam an indian stay in bangalore india"
b = re.match("Iam",str)
print(b)
b = re.search("india",str)
print(b)
b = re.findall("india",str)
print(b)
b = re.split("india",str)
print(b)
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
<re.Match object; span=(0, 3), match='Iam'>
<re.Match object; span=(7, 12), match='india'>
['india', 'india']
['Iam an ', 'n stay in bangalore ', '']

***********************************************************

