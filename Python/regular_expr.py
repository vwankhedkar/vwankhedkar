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
import re

text_to_search = '''
Statement Coverage or Code Coverage or Line Coverage is a metric used in 
Statement Coverage or Code Coverage or Line Coverage is a metric used in 
White Box Testing where we can identify the statements executed and where the 
code is not executed cause of blockage. In this process each and every line of the 
code needs to be checked and executed
321-555-4321
123.555.1234
321*555*4321
123.555.1234
cat     mat     pat         bat
Mr. ABC Mrs. PRQ   Mr XYZ
Ms DEF
Mr. T
vaisWan@gmail.com
vais123@university.edu
wan3005@my-work.net
'''
sent = 'Statement Coverage or Code Coverage'
pattern = re.compile(r'Coverage$')
matches = pattern.finditer(sent)
for match in matches:
    print(match)
pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = pattern.findall(text_to_search)
for match in matches:
    print(match)
with open('data.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    matches = pattern.finditer(contents)
    for match in matches:
        print("Matches in file are: ", match)
pattern = re.compile(r'[^b]at')
matches = pattern.finditer(text_to_search)
for match in matches:
    print("Matches except bat are: ", match)
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)
for match in matches:
    print("Matches with Mr are: ", match)
pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.findall(text_to_search)
for match in matches:
    print("Matches with Mr are: ", match)
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches = pattern.finditer(text_to_search)
for match in matches:
    print("Email Matches are: ", match)
sent = 'Statement Coverage or Code Coverage'
pattern = re.compile(r'coverage',re.I)
matches = pattern.search(sent)
print(matches)
matches = pattern.match(sent)
print(matches)
matches = pattern.findall(sent)
for match in matches:
    print(matches)
urls = '''
https://www.google.com
https://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_url = pattern.sub(r'\2\3',urls)
print(subbed_url)
matches = pattern.finditer(urls)
for match in matches:
    print(match.group())

C:\Trainings\RobotFramework\RobotFramework\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\try1.py 
<re.Match object; span=(27, 35), match='Coverage'>
<re.Match object; span=(350, 362), match='321-555-4321'>
<re.Match object; span=(363, 375), match='123.555.1234'>
<re.Match object; span=(389, 401), match='123.555.1234'>
321-555-4321
123.555.1234
321*555*4321
123.555.1234
Matches in file are:  <re.Match object; span=(272, 284), match='321-555-4321'>
Matches in file are:  <re.Match object; span=(285, 297), match='123.555.1234'>
Matches except bat are:  <re.Match object; span=(2, 5), match='tat'>
Matches except bat are:  <re.Match object; span=(76, 79), match='tat'>
Matches except bat are:  <re.Match object; span=(194, 197), match='tat'>
Matches except bat are:  <re.Match object; span=(402, 405), match='cat'>
Matches except bat are:  <re.Match object; span=(410, 413), match='mat'>
Matches except bat are:  <re.Match object; span=(418, 421), match='pat'>
Matches with Mr are:  <re.Match object; span=(434, 441), match='Mr. ABC'>
Matches with Mr are:  <re.Match object; span=(442, 450), match='Mrs. PRQ'>
Matches with Mr are:  <re.Match object; span=(453, 459), match='Mr XYZ'>
Matches with Mr are:  <re.Match object; span=(460, 466), match='Ms DEF'>
Matches with Mr are:  <re.Match object; span=(467, 472), match='Mr. T'>
Matches with Mr are:  Mr
Matches with Mr are:  Mrs
Matches with Mr are:  Mr
Matches with Mr are:  Ms
Matches with Mr are:  Mr
Email Matches are:  <re.Match object; span=(473, 490), match='vaisWan@gmail.com'>
Email Matches are:  <re.Match object; span=(491, 513), match='vais123@university.edu'>
Email Matches are:  <re.Match object; span=(514, 533), match='wan3005@my-work.net'>
<re.Match object; span=(10, 18), match='Coverage'>
None
['Coverage', 'Coverage']
['Coverage', 'Coverage']

google.com
coreyms.com
youtube.com
nasa.gov

https://www.google.com
https://coreyms.com
https://youtube.com
https://www.nasa.gov

Process finished with exit code 0



