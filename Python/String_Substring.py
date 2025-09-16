s='VMWABCABCABA'
i=s.find('ABC') #find first occurance of ABC
print(i)
i=s.find('ABC',4,10) #from index 4th to 9th
print(i)
i=s.find('ABC',9,11) #from index 9th
print(i)
OUTPUT - 3
6
-1
**********************************************************
s='VMWABCABCABCAB'
subs='ABC'
i = s.find(subs)
if i == -1:
    print('Substring not found')
while i != -1:
    print('{} substring present at index {} '.format(subs, i))
    i = s.find(subs,i+len(subs),len(s))
OUTPUT
ABC substring present at index 3 
ABC substring present at index 6 
ABC substring present at index 9 
***********************************************************
s='VMWABCABCABCAB'
subs=input('Enter substring to search: ')
i=s.find(subs)
if i==-1:
    print('Specified substring not found')
count=0
while i != -1:
    count += 1
    print('{} Present at index {}'.format(subs, i))
    i = s.find(subs,i+len(subs),len(s))
print('No of occurances :',count)
OUTPUT
Enter substring to search: ABC
ABC Present at index 3
ABC Present at index 6
ABC Present at index 9
No of occurances : 3

Enter substring to search: PQR
Specified substring not found
No of occurances : 0
********************************************************************
def find_latest_version(versions):
    def version_key(v):
        return list(map(int, v.lstrip('v').split('.')))
    return max(versions, key=version_key)
# Example usage
versions = ["v1.2.3.4.112", "v2.3.6.7.111"]
latest = find_latest_version(versions)
print("Latest version:", latest)
OUPUT ---- Latest version: v2.3.6.7.111
*************************************************************************
import re
def find_latest_version(versions):
    version_pattern = r'v(\d+(?:\.\d+)*)'
    def version_key(version):
        match = re.search(version_pattern, version)
        if match:
            return list(map(int, match.group(1).split('.')))
        return []
    return max(versions, key=version_key)
versions = ["v1.2.3.4.112", "v2.3.6.7.111"]
latest = find_latest_version(versions)
print("Latest version:", latest)    ----------->    Latest version: v2.3.6.7.111
*************************************************************************
import re

def find_latest_version(versions):
    version_pat = r'v(\d+(?:\.\d+)*)'
    extracted_versions = []

    for v in versions:
        match = re.match(version_pat, v)
        if match:
            # Convert "1.2.3.4.112" → (1,2,3,4,112)
            version_tuple = tuple(map(int, match.group(1).split(".")))
            extracted_versions.append((version_tuple, v))

    if extracted_versions:
        latest = max(extracted_versions, key=lambda x: x[0])
        return latest[1]   # return original string (e.g. "v2.3.6.7.111")
    return None

versions = ["v1.2.3.4.112", "v2.3.6.7.111"]
latest = find_latest_version(versions)
print("Latest version:", latest)
Latest version: v2.3.6.7.111
*********************************************************
str = "python"
rev_str = ""
cnt = len(str)
for ch in str:
    while cnt > 0:
        rev_str += str[cnt - 1]
        cnt = cnt - 1
print("Reversed string is :=> ", rev_str)

*********************************************************

str = "python"
print(str[::-1])

*********************************************************

str = "python"
rev = ""
for i in str:
    rev = i + rev
print(rev)

*********************************************************

# Python code to reverse a string 
# using stack
  
# Function to create an empty stack. It 
# initializes size of stack as 0
def createStack():
    stack=[]
    return stack
   
# Function to determine the size of the stack
def size(stack):
    return len(stack)
   
# Stack is empty if the size is 0
def isEmpty(stack):
    if size(stack) == 0:
        return true
   
# Function to add an item to stack . It
# increases size by 1    
def push(stack,item):
    stack.append(item)
# Function to remove an item from stack. 
# It decreases size by 1
def pop(stack):
    if isEmpty(stack): return
    return stack.pop()
# A stack based function to reverse a string
def reverse(string):
    n = len(string)
    # Create a empty stack
    stack = createStack()
    # Push all characters of string to stack
    for i in range(0,n,1):
        push(stack,string[i])
    # Making the string empty since all
    # characters are saved in stack    
    string=""   
    # Pop all characters of string and put
    # them back to string
    for i in range(0,n,1):
        string+=pop(stack)
           
    return string
  
# Driver code
s = "Geeksforgeeks"
print ("The original string  is : ",end="")
print (s)
print ("The reversed string(using stack) is : ",end="")
print (reverse(s))
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
The original string  is : Geeksforgeeks
The reversed string(using stack) is : skeegrofskeeG
*************************************************************************
for i in range(ord('D'), ord('A') - 1, -1):
    print(chr(i), end=" ")
for i in range(4, 0, -1):
    print(i, end=" ")
OUTPUT - D C B A 4 3 2 1 
*************************************************************************
str = input("Enter a string: ")
result = ""
new_word = True
for char in str:
    if new_word and char.isalpha():
        result += char.upper()
        new_word = False
    else:
        result += char
    if char == " ":
        new_word = True
print("Capitalized:", result)
Enter a string: phthon program is easy
Capitalized: Phthon Program Is Easy
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
*************************************************************************
