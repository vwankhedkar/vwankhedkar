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




*********************************************************
          Output
*********************************************************
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
The original string  is : Geeksforgeeks
The reversed string(using stack) is : skeegrofskeeG

*********************************************************



