import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
10
<class 'decimal.Decimal'>
12345
<class 'decimal.Decimal'>
************************************************************************************************************
str = "Python Programming"
print(str[::-1])

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
vowel_dict = {}
const_count = 0
const = []
for ch in str:
    if (ch in vowels or ch == ' '):
        vowel_dict[ch] = vowel_dict.get(ch, 0) + 1
        vowel_count += 1
    else:
        const_count += 1
        const.append(ch)

print(vowel_dict, "total vowels :=> ", vowel_count, "total constants :=> ", const_count, const)
gnimmargorP nohtyP
{'o': 2, ' ': 1, 'a': 1, 'i': 1} total vowels :=>  5 total constants :=>  13 ['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
************************************************************************************************************
fib = [0,1]
n = 5
for i in range(n):
    fib.append(fib[-1] + fib[-2])
print(', '.join(str(e) for e in fib))  ===>  0, 1, 1, 2, 3, 5, 8

import re
name = 'Python is 1'
digitCount = re.sub("[^0-9]", "",name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall(r"[ \s]", name)
print(digitCount, len(digitCount))
print(letterCount, len(letterCount))
print(len(spaceCount))
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
1 1
Pythonis 8
2
************************************************************************************************************
def count_sp_char(string):
    sp_char = "!@#$%^&*()?|{}[]:;~`"
    char = []
    count = 0
    for i in string:
        if i in sp_char:
            count += 1
            char.append(i)
    return count, char
text = "Hello! How are you? #specialchars! 123"
result = count_sp_char(text)
print("Special Chars are: ", result)    ===>    Special Chars are:  (4, ['!', '?', '#', '!'])
************************************************************************************************************
ArrayList = ["apple", "apple", "banana", "apple", "orange", "banana", "papaya"]
ArrayDict = {}
print("Size of ArrayList is: ",len(ArrayList))
for ele in ArrayList:
    if ele in ArrayDict:
        ArrayDict[ele] = ArrayDict.get(ele, 0) + 1
    else:
        ArrayDict[ele] = 1
print("Count of all list elements are: ", ArrayDict)
for k, v in ArrayDict.items():
    if v > 1:
        print(k," occured more than 2 times are: ",v)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Size of ArrayList is:  7
Count of all list elements are:  {'apple': 3, 'banana': 2, 'orange': 1, 'papaya': 1}
apple  occured more than 2 times are:  3
banana  occured more than 2 times are:  2
************************************************************************************************************
import re
string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, "", string)
print(result)
str2 = "".join(char for char in string if char!=" ")
print(str2)
print(string.replace(" ",""))
CODE
CODE
CODE
************************************************************************************************************
def pyramid(n):
    for i in range(n):
        for j in range(i,n):
            print(" ",end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")
        print("")
pyramid(5)
     *
    ***
   *****
  *******
 *********
************************************************************************************************************
num = int(input("Enter odd number: "))
cnt = num//2
scnt=1
for i in range(cnt+1):
    print(cnt*" "+"*"*scnt)
    cnt=cnt-1
    scnt=scnt+2
scnt=num-2
cnt=1
for i in range(num//2):
    print(cnt*" "+"*"*scnt)
    scnt=scnt-2
    cnt=cnt+1
  *
 ***
*****
 ***
  *
************************************************************************************************************
fout = open('output.txt', 'w')
print(fout)
line1 = "This is first line\n"
fout.write(line1)
line2 = "This is second line\n"
fout.write(line2)
fout.close()
fout = open('output.txt', 'r')
inp = fout.read()
print(inp)
fout.close()
<_io.TextIOWrapper name='output.txt' mode='w' encoding='cp1252'>
This is first line
This is second line
************************************************************************************************************
fname = input("Enter the filename: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:",fname)
    exit()
count=0
for line in fhand:
    if line.startswith('This'):
        count += 1
print("There were ",count, "This lines in",fname)
Enter the filename: output.txt
There were  2 This lines in output.txt
************************************************************************************************************
fhand = open('output.txt')
for line in fhand:
    line = line.strip()
    if not line.startswith("From:"):
        continue
    print(line)
From: abc@gmail.com
From: abc1@gmail.com
From: abc2@gmail.com
From: vais@gmail.com
From: wan@gmail.com
************************************************************************************************************
try:
    fhand = open('output1.txt')
    for line in fhand:
        line = line.strip()
        if not line.startswith("From: "):
            continue
        print(line)
except FileNotFoundError:
    print("Enter correct filename")        ==> print("Enter correct filename")
************************************************************************************************************
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    def __mul__(self, other):
        if isinstance(other, Point):
            return Point(self.x*other.x, self.y*other.y)
        else:
            return Point(self.x*other, self.y*other)
    def __rmul__(self, other):
        return (self.x*other, self.y*other)
    def __repr__(self):
        return ("{0},{1}".format(self.x,self.y))
p1 = Point(2, 3)
p2 = Point(3, 4)
print(p1 + p2)
print(p1 * p2)
5,7
6,12
************************************************************************************************************
def print_params(x,y,z=3,*pospar,**keypar):
    print(x,y,z)
    print(pospar)
    print(keypar)
print_params(1,2,3,5,6,7, foo=1, bar=2)
print_params(1,2)
print_params(1,2,3,'Testing',foo=1, bar=2)
1 2 3
(5, 6, 7)
{'foo': 1, 'bar': 2}
1 2 3
()
{}
1 2 3
('Testing',)
{'foo': 1, 'bar': 2}
************************************************************************************************************
class Circle:
    def __init__(self,radius):
        self.radius = radius
    @property
    def radius(self):
        """Getter method for radius"""
        return self._radius
    @radius.setter
    def radius(self,value):
        """Setter method for radius"""
        if value < 0:
            raise ValueError("Value cannot be negative")
        self._radius=value
    @property
    def area(self):
        """Methos to calculate the area"""
        return 3.14 * self.radius**2
obj = Circle(radius=5)
print(f"radius : {obj.radius}")
print(f"area : {obj.area}")
radius : 5
area : 78.5
************************************************************************************************************
class Calculator:
    @staticmethod
    def add(x, y):
        return x+y
    @staticmethod
    def substract(x, y):
        return x-y
    @staticmethod
    def multiply(x, y):
        return x * y
    @staticmethod
    def divide(x, y):
        if y != 0:
            return x / y
        else:
            print("Cannot divide by zero.")
            return None
result_add = Calculator.add(5, 3)
print(f"Addition: {result_add}")
result_sub = Calculator.substract(8, 4)
print(f"Subtraction: {result_add}")
result_mul = Calculator.multiply(2, 6)
print(f"Multiplication: {result_add}")
result_div = Calculator.divide(10, 2)
print(f"Division: {result_add}")
Addition: 8
Subtraction: 8
Multiplication: 8
Division: 8
************************************************************************************************************
class MyClass:
    class_variable = "I am class variable"
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable
    @staticmethod
    def static_method():
        print("This is static method.")
        print("It doesn't have access to instance variable or self.")
MyClass.static_method()
This is static method.
It doesn't have access to instance variable or self.
************************************************************************************************************
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))
cal = calendar.month(year, month)
print(cal)
Enter year: 2025
Enter month: 06
     June 2025
Mo Tu We Th Fr Sa Su
                   1
 2  3  4  5  6  7  8
 9 10 11 12 13 14 15
16 17 18 19 20 21 22
23 24 25 26 27 28 29
30
************************************************************************************************************
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{} year is not a leap year".format(year))
Enter a year: 2024
2024 is a leap year
************************************************************************************************************
num = int(input("Enter a number: "))
fact = 1
if (num < 0):
    print("Factorial does not exists for negative numbers")
elif num ==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
    print(f"The facrotial of {num} is factorial")
Enter a number: 5
The facrotial of 5 is factorial
************************************************************************************************************
nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Enter positive integer: ")
elif nterms == 1:
    print(f"Fibbonacci sequence for {nterms} are: ", n1)
else:
    print(f"Fibbonacci sequence for {nterms} are: ", end=" ")
    while (count < nterms):
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
How many terms? 7
Fibbonacci sequence for 7 are:  0 1 1 2 3 5 8 
************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

************************************************************************************************************

