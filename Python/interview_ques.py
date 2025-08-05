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
