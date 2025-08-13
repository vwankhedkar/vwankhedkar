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
*******************************************************************************
re.search(): Searches for the pattern anywhere in the string.
 re.match(): Checks for a match at the beginning.
 re.findall(): Returns all matching substrings.
 re.sub(): Replaces substrings matching the pattern.

Regular Expressions (Regex):
import re
stmt = "Python is interpreted language. I love learning python"
match = re.search(r"python", stmt)
print(match)
print(match.group())
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
<re.Match object; span=(48, 54), match='python'>
python

import re
mail = "user@example.com"
pattern = r"^[a-zA-Z0-9_._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, mail):
    print("Valid email")
else:
    print("Invalid email")
OUTPUT -----  Valid email

import re
mail = "user@example.com"
pattern = r"^[a-zA-Z0-9_._-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
email = re.search(pattern, mail)
if email:
    print("Valid email:", email.group())
else:
    print("Invalid email")
OUTPUT    -------------    Valid email: user@example.com

import re
text = "The event is on 10/05/2025."
date = re.search(r"\d{2}/\d{2}/\d{4}", text)
if date:
    print("Found date: ", date.group())
OUTPUT     -------------    Found date:  10/05/2025

import re
phone = "(123)456-7980"
pattern = r"\(\d{3}\)\d{3}-\d{4}"
if re.match(pattern, phone):
    print("Phone number is valid")
else:
    print("Phone number is not valid")
OUTPUT     ---------    Phone number is valid

import re
text = "Hello World This is    India"
modified_text = re.sub(r"\s","_",text)
print("Modified text with - replaced with spaces: ", modified_text)
OUTPUT    ------------    Modified text with - replaced with spaces:  Hello_World_This_is____India

import re
text = "Visit our website at https://www.example.com for more info."
url = re.search(r"https?://[a-zA-Z0-9./]+", text)
if url:
    print("Found URL: ", url.group())
OUTPUT    ------------    Found URL:  https://www.example.com

import re
text = "apple, banana, cherry"
fruits = re.split(r"\s+", text)
print(fruits)
OUTPUT    ------    ['apple,', 'banana,', 'cherry']

import re
text = "I have 3 apples, 7 bananas, and 12 cherries."
numbers = re.search(r"\d+", text)
print(numbers.group())
numbers = re.findall(r"\d+", text)
print(numbers)
pattern = r"\d+ [a-zA-Z]+"
matches = re.findall(pattern, text)
print(matches)  
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
3
['3', '7', '12']
['3 apples', '7 bananas', '12 cherries']

Finding Words That Start with "A" or "a"
import re
text = "Alice and Alex are amazing artists."
words = re.findall(r"\b[Aa]\w+", text)
print("Words found: ", words)
OUTPUT    -------------    Words found:  ['Alice', 'and', 'Alex', 'are', 'amazing', 'artists']
\b → Matches word boundaries (start of a word).
[Aa] → Matches uppercase or lowercase "A".
\w+ → Matches the rest of the word.

Checking if a Password is Strong
● At least 8 characters
● At least one uppercase letter
● At least one lowercase letter
● At least one number
● At least one special character
import re
password = "Secure@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(pattern, password):
    print("Strong password!")
else:
    print("Weak password! Try adding uppercase, lowercase, numbers, and special characters.")
● (?=.*[A-Z]) → At least one uppercase letter
● (?=.*[a-z]) → At least one lowercase letter
● (?=.*\d) → At least one digit
● (?=.*[@$!%*?&]) → At least one special character
● {8,} → At least 8 characters long

Extracting All Words from a Sentenc
import re
text = "Python is fun! Let's learn regex together."
words = re.findall(r"\b\w+\b", text)
print("Words are: ", words)
OUTPUT    -------    Words are:  ['Python', 'is', 'fun', 'Let', 's', 'learn', 'regex', 'together']

import re
text = "Contact us at support@example.com or sales@company.org"
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
print("Emails found:", emails)
OUTPUT    -    Emails found: ['support@example.com', 'sales@company.org']

# Extracting All Hashtags from a Tweet
import re
tweet = "Learning #Python and #Regex is fun! #Coding"
hashtags = re.findall(r"#\w+", tweet)
print("Hashtags Found: ", hashtags)
OUTPUT    ---------    Hashtags Found:  ['#Python', '#Regex', '#Coding']

Extracting All Capitalized Words (Proper Nouns)
import re
text = "Alice and Bob are learning Python in New York."
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b", text)
print("Capitalized_words are: ", capitalized_words)
OUTPUT    ----    Capitalized_words are:  ['Alice', 'Bob', 'Python', 'New', 'York']

# Removing Extra Spaces from a Sentence
import re
text = "Python is awesome!"
clean_text = re.sub(r"\s+", " ", text)
print("Text without spaces are: ", clean_text)
OUTPUT    ---------    Text without spaces are:  Python is awesome!

import re
text = "I have 3 apples, 10 bananas, and 25 oranges."
numbers = re.findall(r"\d+", text)
print("Numbers Found are: ", numbers)
OUTPUT     -----    Numbers Found are:  ['3', '10', '25']

# Checking if a String Contains Only Letters and Numbers
import re
text = "Python123"
if re.fullmatch(r"[A-Za-z0-9]+", text):
    print("Valid input (letters and numbers only)")
else:
    print("Invalid input!")
OUTPUT     -----    Valid input (letters and numbers only)

from _datetime import datetime
# Get current date and time
now = datetime.now()
print(now)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
2025-05-29 22:59:22.244404
2025-05-29 22:59:22                        
*******************************************************************************
import re
regex = re.compile(r'(\d+)(?:-| )(\d+)(?:-| )(\d+)')
n = int(input())
for _ in range(n):
    srch = regex.findall(input())[0]
    print('CountryCode={},LocalAreaCode={},Number={}'.format(*srch))
2
1 877 2638277
91-011-23413627
CountryCode=1,LocalAreaCode=877,Number=2638277
CountryCode=91,LocalAreaCode=011,Number=23413627
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
