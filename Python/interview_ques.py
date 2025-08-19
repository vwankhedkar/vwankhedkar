Find XPATH ->  https://www.iplt20.com/points-table/men/2024
//div[@class='ih-pt-ic ']/div//following-sibling::h2

Find index number of given integer where it is going to add in sorted array

String='Automation' output should be 'amot'
****************************************************************************

Remove 2 in list list=[1,1,2,2,2,2,3,3,4,5,6,7,8,2]
list=[1,1,2,2,2,2,3,3,4,5,6,7,8,2]
lst = [x for x in list if x!=2]
print(lst)
for x in list[:]:
    if x ==2:
        list.remove(x)
print(list)

while 2 in list:
    list.remove(2)
print(list)
OUTPUT :
[1, 1, 3, 3, 4, 5, 6, 7, 8]
[1, 1, 3, 3, 4, 5, 6, 7, 8]
[1, 1, 3, 3, 4, 5, 6, 7, 8]
lst = [1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 2]
while 2 in lst:
    lst.remove(2)
print(lst)
lst = [1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 2]
lst = [x for x in lst if x!= 2]
print(lst)
[1, 1, 3, 3, 4, 5, 6, 7, 8]
[1, 1, 3, 3, 4, 5, 6, 7, 8]
*************************************************************************
arr = [1, 3, 4, 5, 7, 8]
num = 6
index = 0
for i, val in enumerate(arr):
    if val > num:
        break
    index = i + 1
print(f"The number {num} should be inserted at index {index} to maintain sorted order.")

import bisect
index = bisect.bisect_left(arr, num)
print(print(f"The number {num} should be inserted at index {index} to maintain sorted order."))

arr = [1, 3, 4, 5, 7, 8]
num = 6
index = 0
for i, val in enumerate(arr):
    if val > num:
        break
    index = i + 1
print(f"The number {num} should be inserted at index {index} to maintain sorted order.")

import bisect
index = bisect.bisect_left(arr, num)
print(print(f"The number {num} should be inserted at index {index} to maintain sorted order."))

The number 6 should be inserted at index 4 to maintain sorted order.
The number 6 should be inserted at index 4 to maintain sorted order.

*************************************************************************
# Recursive function to generate combinations
str = ["a", "b", "c"]
str1 = []
for i in range(len(str)):
    print(str[i])
    for j in range(i+1, len(str)):
        print(str[i], str[j])
        for k in range(j+1, len(str)):
            print(str[i],str[j],str[j])
a
a b
a b b
a c
b
b c
c
*************************************************************************
def generate_combinations(elements, current, index):
    if current:
        print(' '.join(current))
    for i in range(index, len(elements)):
        current.append(elements[i])
        generate_combinations(elements, current, i+1)
        current.pop()
str_list = ["a", "b", "c"]
generate_combinations(str_list, [], 0)
*************************************************************************
from itertools import combinations
str_list = ["a", "b", "c"]
for r in range(1,len(str_list)+1):
    for combo in combinations(str_list, r):
        print(' '.join(combo))
*************************************************************************
list1 = [1,2,3]
list2 = [1,2,3]
print(list1 is list2)
print(list1 == list2)
list1 = list2
print(list1 is list2)
False
True
True
*************************************************************************
def mydecor(func):
    def wrapper():
        print("Before func called")
        func()
        print("After func called")
    return wrapper
@mydecor
def say_hello():
    print("Hello")
say_hello()
Before func called
Hello
After func called
*************************************************************************
class InvalidInputError(Exception):
    """Raised when entered value is invalid"""
    pass

def checkException():
    try:
        num = input("Enter a number: ")
        if not num.isdigit():
            raise InvalidInputError("Only numeric values are allowed")
        print(f"You entered: {num}")
        print("This is valid input")
    except InvalidInputError as e:
        print(f"Custom Exception: {e}")
    except ValueError:
        print("ValueError occurred")
    finally:
        print("Reached last stage")
checkException()
Enter a number: vais
Custom Exception: Only numeric values are allowed
Reached last stage
*************************************************************************
str_list = ["a", "b", "c", 1, 2, '1a', '5gg','%^&', '!@#']
digit = []
numeric = []
alphanum = []
for ch in str_list:
    ch_str = str(ch)  # Convert everything to string
    if ch_str.isdigit():
        digit.append(ch)
    elif ch_str.isalpha():
        numeric.append(ch)
    elif ch_str.isalnum():
        alphanum.append(ch)
    else:
        print(f"{ch} is a special character (not digit, alphabetic or alphanumeric)")
print("Digits:", digit)
print("Alphabetic:", numeric)
print("Alphanumeric:", alphanum)
%^& is a special character (not digit, alphabetic or alphanumeric)
!@# is a special character (not digit, alphabetic or alphanumeric)
Digits: [1, 2]
Alphabetic: ['a', 'b', 'c']
Alphanumeric: ['1a', '5gg']
*************************************************************************
import re
def expand_string(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = int(s[i])
            i += 1
            group = ''
            while i < len(s) and not s[i].isdigit():
                group += s[i]
                i += 1
            result.append(group * count)
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)
# Test cases
print(expand_string("2ad3b4c"))   # adadbbbcccc
print(expand_string("2a3b4c"))    # aabbbcccc
print(expand_string("2ab3b4c"))   # ababbbbcccc
*************************************************************************
import re
def expand_string(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = int(s[i])
            i += 1
            group = ''
            while i < len(s) and not s[i].isdigit():
                group += s[i]
                i += 1
            result.append(group * count)
        elif i + 1 < len(s) and s[i+1].isdigit():
            # letter followed by digit (e.g., a2)
            group = s[i]
            count = int(s[i+1])
            result.append(group * count)
            i += 2
        else:
            # Just a literal character
            result.append(s[i])
            i += 1
    return ''.join(result)
print(expand_string("2ad3b4c"))     # adadbbbcccc
print(expand_string("2a3b4c"))      # aabbbcccc
print(expand_string("2ab3b4c"))     # abababbbbcccc
print(expand_string("a2b4c3"))      # aabbbbccc
print(expand_string("bb2ca4de2"))   # bbbbcacacacadede
print(expand_string("n3g2tb2"))     # nnnggtbtb
*************************************************************************
3
This line has junk text.  
121.18.19.20  
2001:0db8:0000:0000:0000:ff00:0042:8329 
import re
_octet = r'(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)'
IPv4   = re.compile(rf'^{_octet}\.{_octet}\.{_octet}\.{_octet}$')
IPv6   = re.compile(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$')

def classify(addr):
    if IPv4.fullmatch(addr):
        return "IPv4"
    if IPv6.fullmatch(addr):
        return "IPv6"
    return "Neither"
    
N = int(input())
for _ in range(N):
    line = input()
    print(classify(line))
	
function main() {
    const regex4ipv4 = /^(((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))\.){3}((25[0-5])|(2[0-4]\d)|(1\d{2})|(\d{1,2}))$/;
    const regex4ipv6 = /^(([0-9a-f]{1,4}):){7}([0-9a-f]{1,4})$/;
    for (let i = 1; i < inputLines.length; i++) {
        const str = inputLines[i];
        if (regex4ipv4.test(str)) {
            console.info('IPv4');
        } else if (regex4ipv6.test(str)) {
            console.info('IPv6');
        } else {
            console.info('Neither');
        }
    }
}

<?php
    $input = stream_get_contents($_fp);
    $lines = preg_split('/\R/', $input, -1, PREG_SPLIT_NO_EMPTY);
    array_shift($lines);
    $ipv4_pattern = '/^(([01]?[0-9]{0,2}|2[0-5]?[0-5]?)\.){3}([01]?[0-9]{0,2}|2[0-5]?[0-5]?)$/';
    $ipv6_pattern = '/^(([a-fA-F0-9]{1,4}):){7}[a-fA-F0-9]{1,4}$/';
    foreach($lines as $line) {
        $result = 'Neither';
        if (preg_match($ipv4_pattern, $line)) {
            $result = 'IPv4';
        } elseif (preg_match($ipv6_pattern, $line)) {
            $result = 'IPv6';
        }
        
        echo $result . PHP_EOL;
    }
*************************************************************************
import re
name = 'Python is 1 and 2'
digitCount = re.sub("[^0-9]", "",name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall(r'[ \s]', name)
print(digitCount, len(digitCount))
print(letterCount, len(letterCount))
print(spaceCount, len(spaceCount))
12 2
Pythonisand 11
[' ', ' ', ' ', ' '] 4
******************************************************************************************
saltmine intv ques Sort = ["1 member", "5 members", "No members", "2 members", "5 members", "30 members"]
import re
lst = ["1 member", "5 members", "No members", "2 members", "5 members", "30 members"]
lst1 = [re.sub(" ","",items) for items in lst]
print(lst1)
lst2 = []
for item in lst1:
    if item.lower().startswith("no"):
        num = 0
    else:
        num = int(re.findall(r"\d+", item)[0])
    lst2.append((num, item))
print(lst2)
result = [x[1].replace("members","members").replace("member","member") for x in lst2]
print(result)
-------------------------------------------------------------------------------
data = ["1 member", "5 members", "No members", "2 members","No members", "5 members", "30 members"]
def extract_number(s):
    if "No" in s:
        return float('inf')
    return int(s.split()[0])
for i in range(len(data)):
    for j in range(0, len(data) - i - 1):
        if extract_number(data[j]) > extract_number(data[j + 1]):
            data[j], data[j + 1] = data[j + 1], data[j]
print(data)
-----------------------------------------------------------------------------------
['1 member', '2 members', '5 members', '5 members', '30 members', 'No members', 'No members']
******************************************************************************************
def pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ", end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*", end="")
        print()
pyramid(5)
     *
    ***
   *****
  *******
 *********
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
          * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
*************************************************************************
num = int(input("Enter odd number: "))
cnt = num // 2
scnt = 1
for i in range(cnt+1):
    print(cnt*" "+"*"*scnt)
    cnt = cnt - 1
    scnt = scnt + 2
scnt = num - 2
cnt = 1
for i in range(num//2):
    print(cnt*" "+"*"*scnt)
    scnt = scnt - 2
    cnt = cnt + 1

   *
  ***
 *****
*******
 *****
  ***
   *
*************************************************************************
Monkey patching
class Test:
    def __init__(self,x):
        self.x = x
    def get_data(self):
        print("Send code to fetch data from database")
    def f1(self):
        self.get_data()
    def f2(self):
        self.get_data()
t1 = Test(4)
print("Before monkey patching")
t1.f1()
t1.f2()
def get_new_data(self):
    print("some to code fetch data from test data")
Test.get_data = get_new_data
print("After monkey patching")
t1.f1()
t1.f2()
Before monkey patching
Send code to fetch data from database
Send code to fetch data from database
After monkey patching
some to code fetch data from test data
some to code fetch data from test data
*************************************************************************
vowels = ['a', 'e', 'i', 'o', 'u']
word = "python programming"
vow_count, const_count = 0, 0
vow_dict = {}
for ch in word:
    if ch in vowels:
        vow_dict[ch] = vow_dict.get(ch, 0)+1
        vow_count += 1
    else:
        const_count += 1
print("Total vowels in string are : ", vow_count)
print("Total consonants in string are : ", const_count)
for k, v in vow_dict.items():
    print(f"Vowel {k} occurred : {v} times")
Total vowels in string are :  4
Total consonants in string are :  14
Vowel o occurred : 2 times
Vowel a occurred : 1 times
Vowel i occurred : 1 times
*************************************************************************
mphasis interview
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts/1"
request=requests.get(url=url)
jsonres = request.json()
print(type(request))
code = request.status_code
assert code in [200,201]
print(json.dumps(jsonres, indent=4))
print(jsonres['id'])
print(jsonres['title'])
<class 'requests.models.Response'>
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
1
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
*************************************************************************
mphasis interview
try:
    count = 0
    with open('input.txt','r') as file:
        lines = file.readlines()
    with open('input.txt','w') as file:
        for line in lines:
            if line.startswith("To:"):
                count += 1
                line = line.replace("To:", "From:")
            file.write(line)
        print(f"Replaced {count} occurrences and saved back to file.")
except FileNotFoundError as e:
    print(e)
*************************************************************************
try:
    count = 0
    fhand = open('input.txt', 'r')
    inp = fhand.readlines()
    print(inp[:20])
    for line in inp:
        if line.startswith("From:"):
            count += 1
            print(line, end = " ")
    print(f"\n{count} number of lines are in file starting with 'From:' ")
except FileNotFoundError:
    print("Enter correct filename")
C:\Users\vwank\PycharmProjects\PytestJuly25\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestJuly25\GeneralPythonScripts\try.py 
['colon: Bangalore is located in India.\n', 'colon: India is big country Bangalore is bigger city.\n', 'Bangalore comes under Karnataka.\n', 'From: stephen.marquard@uct.ac.zq\n', 'From: step.uard@uct.edu\n', 'From: stephen.ma@umich.edu\n', 'From: ste.marquard@iupi.edu\n', 'From: stephen.marquard@uct.ac.zq']
From: stephen.marquard@uct.ac.zq
 From: step.uard@uct.edu
 From: stephen.ma@umich.edu
 From: ste.marquard@iupi.edu
 From: stephen.marquard@uct.ac.zq 
5 number of lines are in file starting with 'From:' 
*************************************************************************
EPAM interview 
lst = ["apple", "apple", "banana", "apple", "orange", "banana", "papaya"]
dct_Items = {}
for fruits in lst:
    if fruits in lst:
        dct_Items[fruits] = dct_Items.get(fruits,0)+1
print(dct_Items)
for key, val in dct_Items.items():
    if val > 1:
        print(f"Item {key} occured more than once that is {val} times")
*************************************************************************
BOSCH interview questions
'''
class A:
    def __init__(self, a):
        self.a = a
    def print_val(self):
        print(self.a)

class B(A):

    def print_val(self):
        print("Hello")

myclass = B(2)
myclass.print_val()
'''
# l = [x*x for x in range(10)]
# print(l)

def func()
d = {1:[6, 25, 36, 49, 'abc', 'xyz'], 2:(3, 4, 2)}
(d[1][1]) = 44
print(d)

import threading
t = threading.Thread(func, *kwargs)
t.start()
t.join()
*************************************************************************
Interview AT&T
https://reqres.in/

package com.api;

import io.restassured.RestAssured;
import io.restassured.http.ContentType;
import io.restassured.response.Response;
import org.testng.annotations.Test;

import static org.testng.Assert.assertEquals;
import static org.testng.Assert.assertNotNull;

import java.util.HashMap;
import java.util.Map;

public class PostAPITest {

    @Test
    public void testCreateUser() {
        // Set base URI
        RestAssured.baseURI = "https://reqres.in/api";

        // Request payload
        Map<String, String> requestBody = new HashMap<>();
        requestBody.put("name", "morpheus");
        requestBody.put("job", "leader");

        // Send POST request
        Response response = RestAssured
                .given()
                .contentType(ContentType.JSON)
                .body(requestBody)
                .when()
                .post("/users")
                .then()
                .statusCode(201)
                .extract().response();

        // Assertions
        String name = response.jsonPath().getString("name");
        String job = response.jsonPath().getString("job");
        String id = response.jsonPath().getString("id");
        String createdAt = response.jsonPath().getString("createdAt");

        assertEquals(name, "morpheus");
        assertEquals(job, "leader");
        assertNotNull(id);
        assertNotNull(createdAt);

        System.out.println("User created with ID: " + id);
    }
}

Mavan pom.xml

<dependencies>
    <dependency>
        <groupId>io.rest-assured</groupId>
        <artifactId>rest-assured</artifactId>
        <version>5.3.1</version>
    </dependency>
    <dependency>
        <groupId>org.testng</groupId>
        <artifactId>testng</artifactId>
        <version>7.7.1</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>com.fasterxml.jackson.core</groupId>
        <artifactId>jackson-databind</artifactId>
        <version>2.15.3</version>
    </dependency>
</dependencies>

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

Brillius (Amazon):
Your function should print the pair numbers from the array that add up to the integer parameter.
def find_sum_pair(arr, sum_val):
    arr = list(set(arr))
    ans = []
    for i in range(len(arr)):
        for j in range(1,len(arr)-1):
            if arr[i] + arr[j] == sum_val:
                ans.append((arr[i], arr[j]))
    return ans
arr = [1, 0, 3, 5, 2, 3, 6]
print(find_sum_pair(arr, 5))
[(0, 5), (2, 3), (3, 2)]
****************************************************************************************
A = (1, 2, 3)
B = (1, 2, 3)
C = A
print(A == B) #- True or False
print(A is B) #- True or False
print(A is C) #- True or False
**************************************************************************************
Find the second largest number in the set of array 
lst = [12, 34, 67, 89, 54, 32, 12, 89, 89, 76, 67]
max_val = 0
sec_max = 0
for no in lst:
    if no > max_val:
        sec_max = max_val
        max_val = no
    elif no > sec_max and no != max_val:
        sec_max = no
print(f"max : {max_val}, Second max : {sec_max}")
max : 89, Second max : 76
******************************************************************************************
s1 = input("Enter s1:") #lazy    # Validate anagram
s2 = input("Enter s2:") #zaly
if sorted(s1) == sorted(s2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")
OUTPUT:
Enter s1:lazy
Enter s2:zaly
Strings are anagram
*************************************************************************
EPAM interview questions
class InvalidInputError(Exception):
    """Raised when entered value is invalid"""
    pass
def checkException():
    try:
        num = input("Enter a number: ")
        if not num.isdigit():
            raise InvalidInputError("Only numeric values are allowed")
        print(f"You entered: {num}")
        print("This is valid input")
    except InvalidInputError as e:
        print(f"Custom Exception: {e}")
    except ValueError:
        print("ValueError occurred")
    finally:
        print("Reached last stage")
checkException()
Enter a number: vais
Custom Exception: Only numeric values are allowed
Reached last stage
**********************************************************************************************
str_list = ["a", "b", "c", 1, 2, '1a', '5gg','%^&', '!@#']
digit = []
numeric = []
alphanum = []
for ch in str_list:
    ch_str = str(ch)  # Convert everything to string
    if ch_str.isdigit():
        digit.append(ch)
    elif ch_str.isalpha():
        numeric.append(ch)
    elif ch_str.isalnum():
        alphanum.append(ch)
    else:
        print(f"{ch} is a special character (not digit, alphabetic or alphanumeric)")
print("Digits:", digit)
print("Alphabetic:", numeric)
print("Alphanumeric:", alphanum)
%^& is a special character (not digit, alphabetic or alphanumeric)
!@# is a special character (not digit, alphabetic or alphanumeric)
Digits: [1, 2]
Alphabetic: ['a', 'b', 'c']
Alphanumeric: ['1a', '5gg']
*************************************************************************
import re
def expand_string(s):
    result = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = int(s[i])
            i += 1
            group = ''
            while i < len(s) and not s[i].isdigit():
                group += s[i]
                i += 1
            result.append(group * count)
        else:
            result.append(s[i])
            i += 1
    return ''.join(result)
# Test cases
print(expand_string("2ad3b4c"))   # adadbbbcccc
print(expand_string("2a3b4c"))    # aabbbcccc
print(expand_string("2ab3b4c"))   # ababbbbcccc
***********************************************************************************************
mphasis interview
-------------------
import requests
import json
url = "https://jsonplaceholder.typicode.com/posts/1"
request=requests.get(url=url)
jsonres = request.json()
print(type(request))
code = request.status_code
assert code in [200,201]
print(json.dumps(jsonres, indent=4))
print(jsonres['id'])
print(jsonres['title'])
<class 'requests.models.Response'>
{
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
1
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
***********************************************************************************************
***********************************************************************************************
***********************************************************************************************
def ispalin(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
s = "malayalam"
ans = ispalin(s)
if (ans):
    print("String is Panildrome")
else:
    print("String is not Panildrome")

def ispalin(str):
    return str == str[::-1]

PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> python.exe .\Hello.py
String is Panildrome

*************************************************************

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s).lower()
        left = 0
        right = len(s) - 1

        while (left < right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True

string = "A man, a plan, a canal: Panama"
b = Solution()
print(b.isPalindrome(string))
**********************************************************
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s).lower()
        rev = ""
        for i in range(len(s)):
            rev += s[i]
            i -= 1
        return rev == s

string = "A man, a plan, a canal: Panama"
b = Solution()
print(b.isPalindrome(string))
****************************************************************
How to import data from an excel (Scenario: while you are writing some code in Python, but you need some date which was located in Excel)
> pip install pandas openpyxl
import pandas as pd
# Read Excel and parse the 'DOB' column as datetime
df = pd.read_excel('Data.xlsx', parse_dates=['DOB'])
print(df)
print(df.dtypes)  # To verify DOB is datetime64
      Name        DOB
0    Alice 1995-04-23
1      Bob 1988-12-01
2  Charlie 1990-07-15
Name            object
DOB     datetime64[ns]
dtype: object
**************************************************************
import pandas as pd
df = pd.read_excel("test_data.xlsx")
for index, row in df.iterrows():
    username = row['Username']
    password = row['Password']
    print(f"Testing login with: {username}, {password}")
**************************************************************
