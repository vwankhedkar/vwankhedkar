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
********************************************************************
Execute file IO on https://www.programiz.com/python-programming/online-compiler/
import io
fh = io.StringIO()
fh = io.StringIO()
fh.write("This is line1")
fh.seek(0)
dat = fh.readline()
print(dat)
This is line1
************************************************************************
no_word=0
no_char=0
no_line=0
no_space = 0
with open("input.txt",'r') as file:
    for line in file:
        no_line += 1
        no_char = len(line)
        words = line.split()
        no_word += len(words)
        no_space += len(words)-1
    print("File analysis summary:")
    print("Character count:", no_char)
    print("Word count:", no_word)
    print("Space count:", no_space)
    print("Line count:", no_line)
File analysis summary:
Character count: 22
Word count: 33
Space count: 25
Line count: 8
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
chars = ['A','B','C','D','E','f','g','h','i','j','k']
print("The ASCII values are: ")
chardct = {}
for char in chars:
    chardct[char] = ord(char)
print(chardct)
The ASCII values are: 
{'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107}
************************************************************************************************************
dec_num = int(input("Enter decimal number: "))
print("The decimal value of: ", dec_num, "is: ")
print(bin(dec_num), "in binary")
print(oct(dec_num), "in octal")
print(hex(dec_num), "in hexadecimal")
Enter decimal number: 27
The decimal value of:  27 is: 
0b11011 in binary
0o33 in octal
0x1b in hexadecimal
************************************************************************************************************
my_str = input("Enter a string: ")
words = [word.capitalize() for word in my_str.split()]
words.sort()
print("The sorted words are: ")
for word in words:
    print(word,end=" ")
Enter a string:  suresh ramesh vibhuti gulgule raji ram shyam ajay
The sorted words are: 
Ajay Gulgule Raji Ram Ramesh Shyam Suresh Vibhuti 
************************************************************************************************************
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
my_str = input("Enter a string: ")
no_punc = ""
for char in my_str:
    if char not in punctuations:
        no_punc = no_punc + char
print(no_punc)
Enter a string:  Hello!!!, he said ---and wen
 Hello he said and wen
************************************************************************************************************
def find_words(words, k):
    result = []
    for i in words:
        if len(i) > k:
            result.append(i)
    return result
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragon"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")
Words longer than 5 characters: ['banana', 'cherry', 'elderberry', 'dragon']
************************************************************************************************************
def remove_char(input_str, i):
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}, The string remains unchanged")
    result_str = input_str[:i] + input_str[i+1:]
    return result_str
input_str = "Hello World!"
i = 7
new_str = remove_char(input_str, i)
print(f"Original string: {input_str}")
print(f"String after removing {i}th character: {new_str}")
Original string: Hello World!
String after removing 7th character: Hello Wrld!
************************************************************************************************************
def find_duplicates(input_str):
    char_count = {}
    duplicates = []
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates
input_string = "vaishali wankhedkar"
duplicates_char = find_duplicates(input_string)
print("Duplicate characters: ", duplicates_char)    -->    Duplicate characters:  ['a', 'i', 'h', 'k']
************************************************************************************************************
def add(a, b):
    """This function adds 2 numbers"""
    sum = a + b
    return sum
sum = add(10, 20)
print("Accessing docstring method1: ", add.__doc__)
print("Accessing docstring method2:", end="")
help(add)
OUTPUT:
Accessing docstring method1:  This function adds 2 numbers
Accessing docstring method2:Help on function add in module __main__:

add(a, b)
    This function adds 2 numbers

var = 'Red,Blue,Green,Orange,yellow'
lst = var.split(",",2)
print(lst)   --->    ['Red', 'Blue', 'Green,Orange,yellow']
************************************************************************************************************
import re
from datetime import datetime
def transform_date(date):
    return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1',date)
date_input = "2025-14-06"
print(transform_date(date_input))

new_date = datetime.strptime("2025-06-14","%Y-%m-%d").strftime("%d.%m.%Y")
print(new_date)
06-14-2025
14.06.2025
************************************************************************************************************
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

x = 5
print(type(x))
print(isinstance(x,int))
<class 'int'>
True
************************************************************************************************************
import csv
import json
with open("output.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

person = {"name":"Vais", "age":35}
json_data = json.dumps(person)
print(json_data)
['name', 'age']
['Vais', '30']
['Sumit', '20']
{"name": "Vais", "age": 35}
************************************************************************************************************
class MyClass:
    @staticmethod
    def say_hello():
        print("Hi!")
    @classmethod
    def show_class(cls):
        print(cls)
MyClass.say_hello()
MyClass.show_class()
Hi!
<class '__main__.MyClass'>
************************************************************************************************************
import requests
from bs4 import BeautifulSoup
res = requests.get('https://reqres.in/')
soup = BeautifulSoup(res.text,'html.parser')
print(soup.title.text)
OUTPUT --> Reqres - A hosted REST-API ready to respond to your AJAX requests
************************************************************************************************************
import unittest
def add(x, y):
    return x + y
class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
unittest.main()
************************************************************************************************************
import pandas as pd
import matplotlib.pyplot as plt
data = [1,2,3,4]
plt.plot(data)
plt.show()
************************************************************************************************************
import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts")
print(response.json())
data = {"title":"Hello","body":"World"}
response=requests.post("https://jsonplaceholder.typicode.com/posts",json=data)
print(response.status_code)
data = response.json()
print(data)
print(data["title"])
[{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}, {'userId': 1, 'id': 2, 'title': 'qui est esse', 'body': 'est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla'}, {'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'}, {'userId': 1, 'id': 4, 'title': 'eum et est occaecati', 'body': 'ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit'}, {'userId': 1, 'id': 5, 'title': 'nesciunt quas odio', 'body': 'repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque'}, {'userId': 1, 'id': 6, 'title': 'dolorem eum magni eos aperiam quia', 'body': 'ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae'}, {'userId': 1, 'id': 7, 'title': 'magnam facilis autem', 'body': 'dolore placeat quibusdam ea quo vitae\nmagni quis enim qui quis quo nemo aut saepe\nquidem repellat excepturi ut quia\nsunt ut sequi eos ea sed quas'}, {'userId': 1, 'id': 8, 'title': 'dolorem dolore est ipsam', 'body': 'dignissimos aperiam dolorem qui eum\nfacilis quibusdam animi sint suscipit qui sint possimus cum\nquaerat magni maiores excepturi\nipsam ut commodi dolor voluptatum modi aut vitae'}, {'userId': 1, 'id': 9, 'title': 'nesciunt iure omnis dolorem tempora et accusantium', 'body': 'consectetur animi nesciunt iure dolore\nenim quia ad\nveniam autem ut quam aut nobis\net est aut quod aut provident voluptas autem voluptas'}, {'userId': 1, 'id': 10, 'title': 'optio molestias id quia eum', 'body': 'quo et expedita modi cum officia vel magni\ndoloribus qui repudiandae\nvero nisi sit\nquos veniam quod sed accusamus veritatis error'}, {'userId': 2, 'id': 11, 'title': 'et ea vero quia laudantium autem', 'body': 'delectus reiciendis molestiae occaecati non minima eveniet qui voluptatibus\naccusamus in eum beatae sit\nvel qui neque voluptates ut commodi qui incidunt\nut animi commodi'}, {'userId': 2, 'id': 12, 'title': 'in quibusdam tempore odit est dolorem', 'body': 'itaque id aut magnam\npraesentium quia et ea odit et ea voluptas et\nsapiente quia nihil amet occaecati quia id voluptatem\nincidunt ea est distinctio odio'}, {'userId': 2, 'id': 13, 'title': 'dolorum ut in voluptas mollitia et saepe quo animi', 'body': 'aut dicta possimus sint mollitia voluptas commodi quo doloremque\niste corrupti reiciendis voluptatem eius rerum\nsit cumque quod eligendi laborum minima\nperferendis recusandae assumenda consectetur porro architecto ipsum ipsam'}, {'userId': 2, 'id': 14, 'title': 'voluptatem eligendi optio', 'body': 'fuga et accusamus dolorum perferendis illo voluptas\nnon doloremque neque facere\nad qui dolorum molestiae beatae\nsed aut voluptas totam sit illum'}, {'userId': 2, 'id': 15, 'title': 'eveniet quod temporibus', 'body': 'reprehenderit quos placeat\nvelit minima officia dolores impedit repudiandae molestiae nam\nvoluptas recusandae quis delectus\nofficiis harum fugiat vitae'}, {'userId': 2, 'id': 16, 'title': 'sint suscipit perspiciatis velit dolorum rerum ipsa laboriosam odio', 'body': 'suscipit nam nisi quo aperiam aut\nasperiores eos fugit maiores voluptatibus quia\nvoluptatem quis ullam qui in alias quia est\nconsequatur magni mollitia accusamus ea nisi voluptate dicta'}, {'userId': 2, 'id': 17, 'title': 'fugit voluptas sed molestias voluptatem provident', 'body': 'eos voluptas et aut odit natus earum\naspernatur fuga molestiae ullam\ndeserunt ratione qui eos\nqui nihil ratione nemo velit ut aut id quo'}, {'userId': 2, 'id': 18, 'title': 'voluptate et itaque vero tempora molestiae', 'body': 'eveniet quo quis\nlaborum totam consequatur non dolor\nut et est repudiandae\nest voluptatem vel debitis et magnam'}, {'userId': 2, 'id': 19, 'title': 'adipisci placeat illum aut reiciendis qui', 'body': 'illum quis cupiditate provident sit magnam\nea sed aut omnis\nveniam maiores ullam consequatur atque\nadipisci quo iste expedita sit quos voluptas'}, {'userId': 2, 'id': 20, 'title': 'doloribus ad provident suscipit at', 'body': 'qui consequuntur ducimus possimus quisquam amet similique\nsuscipit porro ipsam amet\neos veritatis officiis exercitationem vel fugit aut necessitatibus totam\nomnis rerum consequatur expedita quidem cumque explicabo'}, {'userId': 3, 'id': 21, 'title': 'asperiores ea ipsam voluptatibus modi minima quia sint', 'body': 'repellat aliquid praesentium dolorem quo\nsed totam minus non itaque\nnihil labore molestiae sunt dolor eveniet hic recusandae veniam\ntempora et tenetur expedita sunt'}, {'userId': 3, 'id': 22, 'title': 'dolor sint quo a velit explicabo quia nam', 'body': 'eos qui et ipsum ipsam suscipit aut\nsed omnis non odio\nexpedita earum mollitia molestiae aut atque rem suscipit\nnam impedit esse'}, {'userId': 3, 'id': 23, 'title': 'maxime id vitae nihil numquam', 'body': 'veritatis unde neque eligendi\nquae quod architecto quo neque vitae\nest illo sit tempora doloremque fugit quod\net et vel beatae sequi ullam sed tenetur perspiciatis'}, {'userId': 3, 'id': 24, 'title': 'autem hic labore sunt dolores incidunt', 'body': 'enim et ex nulla\nomnis voluptas quia qui\nvoluptatem consequatur numquam aliquam sunt\ntotam recusandae id dignissimos aut sed asperiores deserunt'}, {'userId': 3, 'id': 25, 'title': 'rem alias distinctio quo quis', 'body': 'ullam consequatur ut\nomnis quis sit vel consequuntur\nipsa eligendi ipsum molestiae et omnis error nostrum\nmolestiae illo tempore quia et distinctio'}, {'userId': 3, 'id': 26, 'title': 'est et quae odit qui non', 'body': 'similique esse doloribus nihil accusamus\nomnis dolorem fuga consequuntur reprehenderit fugit recusandae temporibus\nperspiciatis cum ut laudantium\nomnis aut molestiae vel vero'}, {'userId': 3, 'id': 27, 'title': 'quasi id et eos tenetur aut quo autem', 'body': 'eum sed dolores ipsam sint possimus debitis occaecati\ndebitis qui qui et\nut placeat enim earum aut odit facilis\nconsequatur suscipit necessitatibus rerum sed inventore temporibus consequatur'}, {'userId': 3, 'id': 28, 'title': 'delectus ullam et corporis nulla voluptas sequi', 'body': 'non et quaerat ex quae ad maiores\nmaiores recusandae totam aut blanditiis mollitia quas illo\nut voluptatibus voluptatem\nsimilique nostrum eum'}, {'userId': 3, 'id': 29, 'title': 'iusto eius quod necessitatibus culpa ea', 'body': 'odit magnam ut saepe sed non qui\ntempora atque nihil\naccusamus illum doloribus illo dolor\neligendi repudiandae odit magni similique sed cum maiores'}, {'userId': 3, 'id': 30, 'title': 'a quo magni similique perferendis', 'body': 'alias dolor cumque\nimpedit blanditiis non eveniet odio maxime\nblanditiis amet eius quis tempora quia autem rem\na provident perspiciatis quia'}, {'userId': 4, 'id': 31, 'title': 'ullam ut quidem id aut vel consequuntur', 'body': 'debitis eius sed quibusdam non quis consectetur vitae\nimpedit ut qui consequatur sed aut in\nquidem sit nostrum et maiores adipisci atque\nquaerat voluptatem adipisci repudiandae'}, {'userId': 4, 'id': 32, 'title': 'doloremque illum aliquid sunt', 'body': 'deserunt eos nobis asperiores et hic\nest debitis repellat molestiae optio\nnihil ratione ut eos beatae quibusdam distinctio maiores\nearum voluptates et aut adipisci ea maiores voluptas maxime'}, {'userId': 4, 'id': 33, 'title': 'qui explicabo molestiae dolorem', 'body': 'rerum ut et numquam laborum odit est sit\nid qui sint in\nquasi tenetur tempore aperiam et quaerat qui in\nrerum officiis sequi cumque quod'}, {'userId': 4, 'id': 34, 'title': 'magnam ut rerum iure', 'body': 'ea velit perferendis earum ut voluptatem voluptate itaque iusto\ntotam pariatur in\nnemo voluptatem voluptatem autem magni tempora minima in\nest distinctio qui assumenda accusamus dignissimos officia nesciunt nobis'}, {'userId': 4, 'id': 35, 'title': 'id nihil consequatur molestias animi provident', 'body': 'nisi error delectus possimus ut eligendi vitae\nplaceat eos harum cupiditate facilis reprehenderit voluptatem beatae\nmodi ducimus quo illum voluptas eligendi\net nobis quia fugit'}, {'userId': 4, 'id': 36, 'title': 'fuga nam accusamus voluptas reiciendis itaque', 'body': 'ad mollitia et omnis minus architecto odit\nvoluptas doloremque maxime aut non ipsa qui alias veniam\nblanditiis culpa aut quia nihil cumque facere et occaecati\nqui aspernatur quia eaque ut aperiam inventore'}, {'userId': 4, 'id': 37, 'title': 'provident vel ut sit ratione est', 'body': 'debitis et eaque non officia sed nesciunt pariatur vel\nvoluptatem iste vero et ea\nnumquam aut expedita ipsum nulla in\nvoluptates omnis consequatur aut enim officiis in quam qui'}, {'userId': 4, 'id': 38, 'title': 'explicabo et eos deleniti nostrum ab id repellendus', 'body': 'animi esse sit aut sit nesciunt assumenda eum voluptas\nquia voluptatibus provident quia necessitatibus ea\nrerum repudiandae quia voluptatem delectus fugit aut id quia\nratione optio eos iusto veniam iure'}, {'userId': 4, 'id': 39, 'title': 'eos dolorem iste accusantium est eaque quam', 'body': 'corporis rerum ducimus vel eum accusantium\nmaxime aspernatur a porro possimus iste omnis\nest in deleniti asperiores fuga aut\nvoluptas sapiente vel dolore minus voluptatem incidunt ex'}, {'userId': 4, 'id': 40, 'title': 'enim quo cumque', 'body': 'ut voluptatum aliquid illo tenetur nemo sequi quo facilis\nipsum rem optio mollitia quas\nvoluptatem eum voluptas qui\nunde omnis voluptatem iure quasi maxime voluptas nam'}, {'userId': 5, 'id': 41, 'title': 'non est facere', 'body': 'molestias id nostrum\nexcepturi molestiae dolore omnis repellendus quaerat saepe\nconsectetur iste quaerat tenetur asperiores accusamus ex ut\nnam quidem est ducimus sunt debitis saepe'}, {'userId': 5, 'id': 42, 'title': 'commodi ullam sint et excepturi error explicabo praesentium voluptas', 'body': 'odio fugit voluptatum ducimus earum autem est incidunt voluptatem\nodit reiciendis aliquam sunt sequi nulla dolorem\nnon facere repellendus voluptates quia\nratione harum vitae ut'}, {'userId': 5, 'id': 43, 'title': 'eligendi iste nostrum consequuntur adipisci praesentium sit beatae perferendis', 'body': 'similique fugit est\nillum et dolorum harum et voluptate eaque quidem\nexercitationem quos nam commodi possimus cum odio nihil nulla\ndolorum exercitationem magnam ex et a et distinctio debitis'}, {'userId': 5, 'id': 44, 'title': 'optio dolor molestias sit', 'body': 'temporibus est consectetur dolore\net libero debitis vel velit laboriosam quia\nipsum quibusdam qui itaque fuga rem aut\nea et iure quam sed maxime ut distinctio quae'}, {'userId': 5, 'id': 45, 'title': 'ut numquam possimus omnis eius suscipit laudantium iure', 'body': 'est natus reiciendis nihil possimus aut provident\nex et dolor\nrepellat pariatur est\nnobis rerum repellendus dolorem autem'}, {'userId': 5, 'id': 46, 'title': 'aut quo modi neque nostrum ducimus', 'body': 'voluptatem quisquam iste\nvoluptatibus natus officiis facilis dolorem\nquis quas ipsam\nvel et voluptatum in aliquid'}, {'userId': 5, 'id': 47, 'title': 'quibusdam cumque rem aut deserunt', 'body': 'voluptatem assumenda ut qui ut cupiditate aut impedit veniam\noccaecati nemo illum voluptatem laudantium\nmolestiae beatae rerum ea iure soluta nostrum\neligendi et voluptate'}, {'userId': 5, 'id': 48, 'title': 'ut voluptatem illum ea doloribus itaque eos', 'body': 'voluptates quo voluptatem facilis iure occaecati\nvel assumenda rerum officia et\nillum perspiciatis ab deleniti\nlaudantium repellat ad ut et autem reprehenderit'}, {'userId': 5, 'id': 49, 'title': 'laborum non sunt aut ut assumenda perspiciatis voluptas', 'body': 'inventore ab sint\nnatus fugit id nulla sequi architecto nihil quaerat\neos tenetur in in eum veritatis non\nquibusdam officiis aspernatur cumque aut commodi aut'}, {'userId': 5, 'id': 50, 'title': 'repellendus qui recusandae incidunt voluptates tenetur qui omnis exercitationem', 'body': 'error suscipit maxime adipisci consequuntur recusandae\nvoluptas eligendi et est et voluptates\nquia distinctio ab amet quaerat molestiae et vitae\nadipisci impedit sequi nesciunt quis consectetur'}, {'userId': 6, 'id': 51, 'title': 'soluta aliquam aperiam consequatur illo quis voluptas', 'body': 'sunt dolores aut doloribus\ndolore doloribus voluptates tempora et\ndoloremque et quo\ncum asperiores sit consectetur dolorem'}, {'userId': 6, 'id': 52, 'title': 'qui enim et consequuntur quia animi quis voluptate quibusdam', 'body': 'iusto est quibusdam fuga quas quaerat molestias\na enim ut sit accusamus enim\ntemporibus iusto accusantium provident architecto\nsoluta esse reprehenderit qui laborum'}, {'userId': 6, 'id': 53, 'title': 'ut quo aut ducimus alias', 'body': 'minima harum praesentium eum rerum illo dolore\nquasi exercitationem rerum nam\nporro quis neque quo\nconsequatur minus dolor quidem veritatis sunt non explicabo similique'}, {'userId': 6, 'id': 54, 'title': 'sit asperiores ipsam eveniet odio non quia', 'body': 'totam corporis dignissimos\nvitae dolorem ut occaecati accusamus\nex velit deserunt\net exercitationem vero incidunt corrupti mollitia'}, {'userId': 6, 'id': 55, 'title': 'sit vel voluptatem et non libero', 'body': 'debitis excepturi ea perferendis harum libero optio\neos accusamus cum fuga ut sapiente repudiandae\net ut incidunt omnis molestiae\nnihil ut eum odit'}, {'userId': 6, 'id': 56, 'title': 'qui et at rerum necessitatibus', 'body': 'aut est omnis dolores\nneque rerum quod ea rerum velit pariatur beatae excepturi\net provident voluptas corrupti\ncorporis harum reprehenderit dolores eligendi'}, {'userId': 6, 'id': 57, 'title': 'sed ab est est', 'body': 'at pariatur consequuntur earum quidem\nquo est laudantium soluta voluptatem\nqui ullam et est\net cum voluptas voluptatum repellat est'}, {'userId': 6, 'id': 58, 'title': 'voluptatum itaque dolores nisi et quasi', 'body': 'veniam voluptatum quae adipisci id\net id quia eos ad et dolorem\naliquam quo nisi sunt eos impedit error\nad similique veniam'}, {'userId': 6, 'id': 59, 'title': 'qui commodi dolor at maiores et quis id accusantium', 'body': 'perspiciatis et quam ea autem temporibus non voluptatibus qui\nbeatae a earum officia nesciunt dolores suscipit voluptas et\nanimi doloribus cum rerum quas et magni\net hic ut ut commodi expedita sunt'}, {'userId': 6, 'id': 60, 'title': 'consequatur placeat omnis quisquam quia reprehenderit fugit veritatis facere', 'body': 'asperiores sunt ab assumenda cumque modi velit\nqui esse omnis\nvoluptate et fuga perferendis voluptas\nillo ratione amet aut et omnis'}, {'userId': 7, 'id': 61, 'title': 'voluptatem doloribus consectetur est ut ducimus', 'body': 'ab nemo optio odio\ndelectus tenetur corporis similique nobis repellendus rerum omnis facilis\nvero blanditiis debitis in nesciunt doloribus dicta dolores\nmagnam minus velit'}, {'userId': 7, 'id': 62, 'title': 'beatae enim quia vel', 'body': 'enim aspernatur illo distinctio quae praesentium\nbeatae alias amet delectus qui voluptate distinctio\nodit sint accusantium autem omnis\nquo molestiae omnis ea eveniet optio'}, {'userId': 7, 'id': 63, 'title': 'voluptas blanditiis repellendus animi ducimus error sapiente et suscipit', 'body': 'enim adipisci aspernatur nemo\nnumquam omnis facere dolorem dolor ex quis temporibus incidunt\nab delectus culpa quo reprehenderit blanditiis asperiores\naccusantium ut quam in voluptatibus voluptas ipsam dicta'}, {'userId': 7, 'id': 64, 'title': 'et fugit quas eum in in aperiam quod', 'body': 'id velit blanditiis\neum ea voluptatem\nmolestiae sint occaecati est eos perspiciatis\nincidunt a error provident eaque aut aut qui'}, {'userId': 7, 'id': 65, 'title': 'consequatur id enim sunt et et', 'body': 'voluptatibus ex esse\nsint explicabo est aliquid cumque adipisci fuga repellat labore\nmolestiae corrupti ex saepe at asperiores et perferendis\nnatus id esse incidunt pariatur'}, {'userId': 7, 'id': 66, 'title': 'repudiandae ea animi iusto', 'body': 'officia veritatis tenetur vero qui itaque\nsint non ratione\nsed et ut asperiores iusto eos molestiae nostrum\nveritatis quibusdam et nemo iusto saepe'}, {'userId': 7, 'id': 67, 'title': 'aliquid eos sed fuga est maxime repellendus', 'body': 'reprehenderit id nostrum\nvoluptas doloremque pariatur sint et accusantium quia quod aspernatur\net fugiat amet\nnon sapiente et consequatur necessitatibus molestiae'}, {'userId': 7, 'id': 68, 'title': 'odio quis facere architecto reiciendis optio', 'body': 'magnam molestiae perferendis quisquam\nqui cum reiciendis\nquaerat animi amet hic inventore\nea quia deleniti quidem saepe porro velit'}, {'userId': 7, 'id': 69, 'title': 'fugiat quod pariatur odit minima', 'body': 'officiis error culpa consequatur modi asperiores et\ndolorum assumenda voluptas et vel qui aut vel rerum\nvoluptatum quisquam perspiciatis quia rerum consequatur totam quas\nsequi commodi repudiandae asperiores et saepe a'}, {'userId': 7, 'id': 70, 'title': 'voluptatem laborum magni', 'body': 'sunt repellendus quae\nest asperiores aut deleniti esse accusamus repellendus quia aut\nquia dolorem unde\neum tempora esse dolore'}, {'userId': 8, 'id': 71, 'title': 'et iusto veniam et illum aut fuga', 'body': 'occaecati a doloribus\niste saepe consectetur placeat eum voluptate dolorem et\nqui quo quia voluptas\nrerum ut id enim velit est perferendis'}, {'userId': 8, 'id': 72, 'title': 'sint hic doloribus consequatur eos non id', 'body': 'quam occaecati qui deleniti consectetur\nconsequatur aut facere quas exercitationem aliquam hic voluptas\nneque id sunt ut aut accusamus\nsunt consectetur expedita inventore velit'}, {'userId': 8, 'id': 73, 'title': 'consequuntur deleniti eos quia temporibus ab aliquid at', 'body': 'voluptatem cumque tenetur consequatur expedita ipsum nemo quia explicabo\naut eum minima consequatur\ntempore cumque quae est et\net in consequuntur voluptatem voluptates aut'}, {'userId': 8, 'id': 74, 'title': 'enim unde ratione doloribus quas enim ut sit sapiente', 'body': 'odit qui et et necessitatibus sint veniam\nmollitia amet doloremque molestiae commodi similique magnam et quam\nblanditiis est itaque\nquo et tenetur ratione occaecati molestiae tempora'}, {'userId': 8, 'id': 75, 'title': 'dignissimos eum dolor ut enim et delectus in', 'body': 'commodi non non omnis et voluptas sit\nautem aut nobis magnam et sapiente voluptatem\net laborum repellat qui delectus facilis temporibus\nrerum amet et nemo voluptate expedita adipisci error dolorem'}, {'userId': 8, 'id': 76, 'title': 'doloremque officiis ad et non perferendis', 'body': 'ut animi facere\ntotam iusto tempore\nmolestiae eum aut et dolorem aperiam\nquaerat recusandae totam odio'}, {'userId': 8, 'id': 77, 'title': 'necessitatibus quasi exercitationem odio', 'body': 'modi ut in nulla repudiandae dolorum nostrum eos\naut consequatur omnis\nut incidunt est omnis iste et quam\nvoluptates sapiente aliquam asperiores nobis amet corrupti repudiandae provident'}, {'userId': 8, 'id': 78, 'title': 'quam voluptatibus rerum veritatis', 'body': 'nobis facilis odit tempore cupiditate quia\nassumenda doloribus rerum qui ea\nillum et qui totam\naut veniam repellendus'}, {'userId': 8, 'id': 79, 'title': 'pariatur consequatur quia magnam autem omnis non amet', 'body': 'libero accusantium et et facere incidunt sit dolorem\nnon excepturi qui quia sed laudantium\nquisquam molestiae ducimus est\nofficiis esse molestiae iste et quos'}, {'userId': 8, 'id': 80, 'title': 'labore in ex et explicabo corporis aut quas', 'body': 'ex quod dolorem ea eum iure qui provident amet\nquia qui facere excepturi et repudiandae\nasperiores molestias provident\nminus incidunt vero fugit rerum sint sunt excepturi provident'}, {'userId': 9, 'id': 81, 'title': 'tempora rem veritatis voluptas quo dolores vero', 'body': 'facere qui nesciunt est voluptatum voluptatem nisi\nsequi eligendi necessitatibus ea at rerum itaque\nharum non ratione velit laboriosam quis consequuntur\nex officiis minima doloremque voluptas ut aut'}, {'userId': 9, 'id': 82, 'title': 'laudantium voluptate suscipit sunt enim enim', 'body': 'ut libero sit aut totam inventore sunt\nporro sint qui sunt molestiae\nconsequatur cupiditate qui iste ducimus adipisci\ndolor enim assumenda soluta laboriosam amet iste delectus hic'}, {'userId': 9, 'id': 83, 'title': 'odit et voluptates doloribus alias odio et', 'body': 'est molestiae facilis quis tempora numquam nihil qui\nvoluptate sapiente consequatur est qui\nnecessitatibus autem aut ipsa aperiam modi dolore numquam\nreprehenderit eius rem quibusdam'}, {'userId': 9, 'id': 84, 'title': 'optio ipsam molestias necessitatibus occaecati facilis veritatis dolores aut', 'body': 'sint molestiae magni a et quos\neaque et quasi\nut rerum debitis similique veniam\nrecusandae dignissimos dolor incidunt consequatur odio'}, {'userId': 9, 'id': 85, 'title': 'dolore veritatis porro provident adipisci blanditiis et sunt', 'body': 'similique sed nisi voluptas iusto omnis\nmollitia et quo\nassumenda suscipit officia magnam sint sed tempora\nenim provident pariatur praesentium atque animi amet ratione'}, {'userId': 9, 'id': 86, 'title': 'placeat quia et porro iste', 'body': 'quasi excepturi consequatur iste autem temporibus sed molestiae beatae\net quaerat et esse ut\nvoluptatem occaecati et vel explicabo autem\nasperiores pariatur deserunt optio'}, {'userId': 9, 'id': 87, 'title': 'nostrum quis quasi placeat', 'body': 'eos et molestiae\nnesciunt ut a\ndolores perspiciatis repellendus repellat aliquid\nmagnam sint rem ipsum est'}, {'userId': 9, 'id': 88, 'title': 'sapiente omnis fugit eos', 'body': 'consequatur omnis est praesentium\nducimus non iste\nneque hic deserunt\nvoluptatibus veniam cum et rerum sed'}, {'userId': 9, 'id': 89, 'title': 'sint soluta et vel magnam aut ut sed qui', 'body': 'repellat aut aperiam totam temporibus autem et\narchitecto magnam ut\nconsequatur qui cupiditate rerum quia soluta dignissimos nihil iure\ntempore quas est'}, {'userId': 9, 'id': 90, 'title': 'ad iusto omnis odit dolor voluptatibus', 'body': 'minus omnis soluta quia\nqui sed adipisci voluptates illum ipsam voluptatem\neligendi officia ut in\neos soluta similique molestias praesentium blanditiis'}, {'userId': 10, 'id': 91, 'title': 'aut amet sed', 'body': 'libero voluptate eveniet aperiam sed\nsunt placeat suscipit molestias\nsimilique fugit nam natus\nexpedita consequatur consequatur dolores quia eos et placeat'}, {'userId': 10, 'id': 92, 'title': 'ratione ex tenetur perferendis', 'body': 'aut et excepturi dicta laudantium sint rerum nihil\nlaudantium et at\na neque minima officia et similique libero et\ncommodi voluptate qui'}, {'userId': 10, 'id': 93, 'title': 'beatae soluta recusandae', 'body': 'dolorem quibusdam ducimus consequuntur dicta aut quo laboriosam\nvoluptatem quis enim recusandae ut sed sunt\nnostrum est odit totam\nsit error sed sunt eveniet provident qui nulla'}, {'userId': 10, 'id': 94, 'title': 'qui qui voluptates illo iste minima', 'body': 'aspernatur expedita soluta quo ab ut similique\nexpedita dolores amet\nsed temporibus distinctio magnam saepe deleniti\nomnis facilis nam ipsum natus sint similique omnis'}, {'userId': 10, 'id': 95, 'title': 'id minus libero illum nam ad officiis', 'body': 'earum voluptatem facere provident blanditiis velit laboriosam\npariatur accusamus odio saepe\ncumque dolor qui a dicta ab doloribus consequatur omnis\ncorporis cupiditate eaque assumenda ad nesciunt'}, {'userId': 10, 'id': 96, 'title': 'quaerat velit veniam amet cupiditate aut numquam ut sequi', 'body': 'in non odio excepturi sint eum\nlabore voluptates vitae quia qui et\ninventore itaque rerum\nveniam non exercitationem delectus aut'}, {'userId': 10, 'id': 97, 'title': 'quas fugiat ut perspiciatis vero provident', 'body': 'eum non blanditiis soluta porro quibusdam voluptas\nvel voluptatem qui placeat dolores qui velit aut\nvel inventore aut cumque culpa explicabo aliquid at\nperspiciatis est et voluptatem dignissimos dolor itaque sit nam'}, {'userId': 10, 'id': 98, 'title': 'laboriosam dolor voluptates', 'body': 'doloremque ex facilis sit sint culpa\nsoluta assumenda eligendi non ut eius\nsequi ducimus vel quasi\nveritatis est dolores'}, {'userId': 10, 'id': 99, 'title': 'temporibus sit alias delectus eligendi possimus magni', 'body': 'quo deleniti praesentium dicta non quod\naut est molestias\nmolestias et officia quis nihil\nitaque dolorem quia'}, {'userId': 10, 'id': 100, 'title': 'at nam consequatur ea labore ea harum', 'body': 'cupiditate quo est a modi nesciunt soluta\nipsa voluptas error itaque dicta in\nautem qui minus magnam et distinctio eum\naccusamus ratione error aut'}]
201
{'title': 'Hello', 'body': 'World', 'id': 101}
Hello
************************************************************************************************************
import re
text = "My name is Vais"
match = re.search("Vais",text)
print(match.group())

pattern = r"\w+@\w+\.\w+"
str = re.findall(pattern,"Email me at: test12@example.com")
print(str)
Vais
['test12@example.com']
************************************************************************************************************
import statistics
data = [10, 20, 30, 40]
print(statistics.mean(data))
print(statistics.median(data))
print(statistics.stdev(data))
25
25.0
12.909944487358056
************************************************************************************************************
from datetime import datetime
now = datetime.now()
print(now)
bday = datetime(2025, 6, 14)
print(bday)
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%B %d %Y"))
print(now.strftime("%I:%M %p"))
2025-06-15 00:16:36.989018
2025-06-14 00:00:00
15/06/2025
June 15 2025
12:16 AM
Format codes example:
 %d → Day
 %m → Month (number)
 %B → Month name
 %Y → Year
 %I:%M %p → Hour:Minute AM/PM
************************************************************************************************************
squares = [x**2 for x in range(5)]
print(squares)
unique = {x for x in [1, 1, 2, 3, 3]}
print(unique)
names = {i: f"User{i}" for i in range(3)}
print(names)

for i, val in enumerate(["a","b"]):
    print(i, val)
name = ['A', 'B']
score = [90, 80]
for n,s in zip(name, score):
    print(n, s)
[0, 1, 4, 9, 16]
{1, 2, 3}
{0: 'User0', 1: 'User1', 2: 'User2'}
0 a
1 b
A 90
B 80
************************************************************************************************************
 pip freeze -  This command lists all installed Python packages and their versions
 pip freeze > requirements.txt
 pip install -r requirements.txt - to install all libs
 Activate venv module
 python -m venv myenv  # create environment
 myenv\Scripts\activate
 source myenv/bin/activate
************************************************************************************************************
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
print(flatten([1,[2,[3]],[4,5]]))    --->    [1, 2, 3, 4, 5]
******************************************************************************************************
import pandas as pd
df = pd.DataFrame({
    'Region': ['North', 'South', 'North', 'South'],
    'Product': ['A', 'A', 'B', 'B'],
    'Sales': [100, 150, 200, 250]
})
pivot = df.pivot_table(index='Region', columns='Product', values='Sales', aggfunc='sum')
print(pivot)
Product    A    B
Region           
North    100  200
South    150  250
*********************************************************
Prime:
n = int(input("Enter Input: "))
n1 = 2
while (n1 <= n):
    is_prime = True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime = False
            break
    if is_prime==True:
        print(n1)
    n1 = n1 + 1
Enter Input: 5
2 3 5 
*************************************************************************************************
************************************************************************************************************
************************************************************************************************************
************************************************************************************************************
s = {1, 2, 3, 3, 2, 4, 5, 5} 
print(s) 
# Remove will raise an error if the element is not in the set 
s.remove(4) 
print(s) 
# Discard doesn't raise any errors 
s.discard(1) 
print(s) 
Output: 
{1, 2, 3, 4, 5} 
{1, 2, 3, 5} 
{2, 3, 5}
**************************************************************************************************************
arr = [1, 2, 3, 2, 3, 4]
target_sum = 6
pairs = []
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target_sum:
            pairs.append((arr[i], arr[j]))
print("Pairs with sum = 6:")
for pair in pairs:
    print(pair)
OUTPUT:
Pairs with sum = 6:
(2, 4)
(3, 3)
(2, 4)
***********************************************************************
lst = [1,2,1,3,3,2,1]
dct = {}
for num in lst:
    dct[num] = dct.get(num,0)+1
print(dct)
{1: 3, 2: 2, 3: 2}
***********************************************************************
str = "Vaishali"
str_dct = {}
for ch in str:
    str_dct[ch] = str_dct.get(ch,0)+1
print(f"All Char count is : {str_dct}")
for k, v in str_dct.items():
    if v == 1:
        print(f"first unique character is -> {k} : {v}")
        break
All Char count is : {'V': 1, 'a': 2, 'i': 2, 's': 1, 'h': 1, 'l': 1}
first unique character is -> V : 1
***********************************************************************
str = "Vaishali"
str_dct = {}
for ch in str:
    str_dct[ch] = str_dct.get(ch,0)+1
for k, v in str_dct.items():
    print(f"Unique character {k} appeared {v} times")
Unique character V appeared 1 times
Unique character a appeared 2 times
Unique character i appeared 2 times
Unique character s appeared 1 times
Unique character h appeared 1 times
Unique character l appeared 1 times
***********************************************************************
word = "Kundan Kumar Pandey Kundan Kumar"
words = word.split(" ")
wrd_cnt = {}
for str in words:
    wrd_cnt[str] = wrd_cnt.get(str,0)+1
print("Words count are : ", wrd_cnt)
Words count are :  {'Kundan': 2, 'Kumar': 2, 'Pandey': 1}
***********************************************************************
# Convert from word to digit

words_upto_19 = ['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT',
                 'NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN',
                 'SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
words_upto_tens = ['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY',
                  'SEVENTY','EIGHTY','NINETY']

n = int(input("Enter a digit from 0-99: "))
output=''
if n==0:
    output='ZERO'
elif n<=19:
    output=words_upto_19[n]
elif n<=99:
    output = words_upto_tens[n//10]+" "+words_upto_19[n%10]
else:
    print("Please enter value from 0-99 only...")
print(output)
Enter a digit from 0-99: 45
FOURTY FIVE
***********************************************************************
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
***********************************************************************
str_1 = input("Enter first string: ").replace(" ", "").lower()
str_2 = input("Enter second string: ").replace(" ", "").lower()
if len(str_1) != len(str_2):
    print("No, the strings are not anagrams.")
else:
    freq = {}
    for ch in str_1:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in str_2:
        if ch in freq:
            freq[ch] -= 1
        else:
            freq[ch] = 1
    
    if all(value == 0 for value in freq.values()):
        print("Yes, the given strings are anagrams.")
    else:
        print("No, the given strings are not anagrams.")
Enter first string: lazy
Enter second string: zaly
Yes, the given strings are anagrams.
****************************************************************
def count_to(n):    # Generator
    i = 0
    while i<=n:
        yield i
        i += 1
counter = count_to(3)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
0
1
2
3
Traceback (most recent call last):
  File "/home/main.py", line 11, in <module>
    print(next(counter))
          ~~~~^^^^^^^^^
StopIteration
************************************************************
# list vs generator
import sys
num_list = [x for x in range(100)]
num_gen = (x for x in range(100))
print(sys.getsizeof(num_list))  # large memory
print(sys.getsizeof(num_gen))   # small memory footprint
************************************************************

************************************************************

************************************************************

************************************************************
---------------------------------------------------
		Python
---------------------------------------------------
with open('file.txt','r') as file:
    for line in file:
        print(line.strip())

---------------------------------------------------
with open('file.txt','w') as file:
    file.write("Hello")
with open('file.txt','r') as file:
    print(file.read())
---------------------------------------------------
import re
text = "I love learning Python!"
match = re.search(r"Python", text)
if match:
    print(match.group())
----------------
import re
text = "I love Python learning Python!"
match = re.search(r"Python", text)
if match:
    print(match)
---------------------------------------------------
import re
text = "My favorite number is 42."
match = re.search(r"\d+",text)
if match:
    print("Found Number : ", match.group())
Found Number :  42
---------------------------------------------------
import re
email = "user@example.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if (re.match(pattern,email)):
    print("Valid mail !")
else:
    print("Invalid mail !")
Valid mail !
---------------------------------------------------
import re
text = "The event is on 15/08/2025."
date = re.search(r"\d{2}/\d{2}/\d{4}", text)
if date:
    print("Found date : ", date.group())
Found date :  15/08/2025
---------------------------------------------------
import re
phone_number = "(123) 456-7890"
pattern = r"\(\d{3}\) \d{3}-\d{4}"
if re.match(pattern, phone_number):
    print("Valid phone number !")
else:
    print("Invalid phone number!")
Valid phone number !
---------------------------------------------------
import re
text = "Hello World!"
modified_text = re.sub(r"\s","_",text)
print(modified_text)
Hello_World!
---------------------------------------------------
import re
text = "Visit our website at https://www.example.com for more info."
url = re.search(r"https?://[a-zA-Z0-9./]+",text)
if url:
    print("Found URL...", url.group())
Found URL... https://www.example.com
---------------------------------------------------
import re
text = "apple, banana, cherry"
fruits = re.split(r",\s*",text)
print(fruits)
['apple', 'banana', 'cherry']
---------------------------------------------------
import re
text = "I have 3 apples, 7 bananas, and 12 cherries."
numbers = re.findall(r"\d+",text)
print("Numbers found !", numbers)
Numbers found ! ['3', '7', '12']
---------------------------------------------------
import re
text = "Alice and Alex are amazing artists."
words = re.findall(r"\b[Aa]\w+",text)
print("Words found - ",words)
Words found -  ['Alice', 'and', 'Alex', 'are', 'amazing', 'artists']
---------------------------------------------------
import re
password = "Secure@123"
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
if re.match(pattern, password):
    print("Strong password!")
else:
    print("Weak password!Try adding uppercase, lowercase, numbers, and special characters.")
Strong password!
---------------------------------------------------
import re
text = "Python is fun! Let's learn regex together."
words = re.findall(r"\b\w+\b",text)
print("Words : ", words)
Words :  ['Python', 'is', 'fun', 'Let', 's', 'learn', 'regex', 'together']
---------------------------------------------------
import re
tweet = "Learning #Python and #Regex is fun! #Coding"
hashtags = re.findall(r"#\w+",tweet)
print("Hashtags found - ", hashtags)
Hashtags found -  ['#Python', '#Regex', '#Coding']
---------------------------------------------------
import re
text = "Alice and Bob are learning Python in New York."
capitalized_words = re.findall(r"\b[A-Z][a-z]*\b",text)
print("capitalized Words : ", capitalized_words)
capitalized Words :  ['Alice', 'Bob', 'Python', 'New', 'York']
---------------------------------------------------
import re
text = "Python is awesome!"
cleaned_text = re.sub(r"\s+"," ",text)
print(cleaned_text)
Python is awesome!
---------------------------------------------------
import re
text = "I have 3 apples, 10 bananas, and 25 oranges."
numbers = re.findall(r"\d+",text)
print("Numbers found : ",numbers)
Numbers found :  ['3', '10', '25']
---------------------------------------------------
import re
text = "The tiger and the turtle are in the zoo."
words = re.findall(r"\b[Tt]\w+",text)
print("Words found : ", words)
Words found :  ['The', 'tiger', 'the', 'turtle', 'the']
---------------------------------------------------
import re
text = "Python123"
if re.fullmatch(r"[A-Za-z0-9]+",text):
    print("Valid input (letters and numbers only)")
else:
    print("Invalid input")
Valid input (letters and numbers only)
---------------------------------------------------
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!")
dog = Dog("Buddy", "Golden Retriever")
dog.bark()
Buddy says Woof!
---------------------------------------------------
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
dog = Dog()
dog.speak()
Dog barks
---------------------------------------------------
class Car:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    def accelerate(self,increment):
        if increment > 0:
            self.__speed+=increment
    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement > 0:
            self.__speed -= decrement
    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand
---------------------------------------------------
class Car:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    def accelerate(self,increment):
        if increment > 0:
            self.__speed+=increment
    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement > 0:
            self.__speed -= decrement
    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand
my_car = Car("Toyota",50)
print(my_car.get_speed())
my_car.accelerate(30)
print(my_car.get_speed())
my_car.brake(20)
print(my_car.get_speed())
50
80
60
---------------------------------------------------
class Cat:
    def speak(self):
        print("Meow")
class Dog:
    def speak(self):
        print("Woof")
animals = [Cat(), Dog()]
for animal in animals:
    animal.speak()
Meow
Woof
---------------------------------------------------
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("Woof")
dog = Dog()
dog.speak()
Woof
---------------------------------------------------
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper
@decorator
def say_hello():
    print("Hello")
say_hello()
Before function call
Hello
After function call
---------------------------------------------------
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(3)
for num in counter:
    print(num)
1
2
3
---------------------------------------------------
numbers = [1, 2, 3, 4, 5]
sq = [x**2 for x in numbers]
print(sq)
[1, 4, 9, 16, 25]
---------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
age_dict = {name:age for name, age in zip(names, ages)}
print(age_dict)
{'Alice': 25, 'Bob': 30, 'Charlie': 35}
---------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit}")
0 : apple
1 : banana
2 : cherry
---------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combine = zip(names,scores)
print(list(combine))
[('Alice', 85), ('Bob', 90), ('Charlie', 95)]
---------------------------------------------------
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))	==>		1
---------------------------------------------------
import threading
def print_num():
    for i in range(5):
        print(i)
thread1 = threading.Thread(target=print_num)
thread2 = threading.Thread(target=print_num)
thread1.start()
thread2.start()
0
1
2
3
4
0
1
2
3
4
---------------------------------------------------
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return decorator
@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
Hello, Alice!
Hello, Alice!
Hello, Alice!
---------------------------------------------------
import json
person = {"name":"Alice", "age":25}
json_data = json.dumps(person)
print(json_data)
{"name": "Alice", "age": 25}
---------------------------------------------------
import json
json_string = '{"name":"Alice", "age":25}'
person = json.loads(json_string)
print(person)
{'name': 'Alice', 'age': 25}
---------------------------------------------------
import csv
data = [["name", "age"], ["Alice", 25], ["Bob", 30]]
with open('output.csv','w',newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
with open('output.csv','r') as file:
    header = csv.reader(file)
    for row in header:
        print(row)
['name', 'age']
['Alice', '25']
['Bob', '30']
---------------------------------------------------
import pandas as pd
data = {"name": ["Alice", "Bob", "Charlie"], "age": [25, 30, 35]}
df = pd.DataFrame(data)
print(df)
print()
print(df["name"])
print()
print(df[df["age"]>=30])
      name  age
0    Alice   25
1      Bob   30
2  Charlie   35

0      Alice
1        Bob
2    Charlie
Name: name, dtype: object

      name  age
1      Bob   30
2  Charlie   35
---------------------------------------------------
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
200
---------------------------------------------------
import requests
response = requests.get("https://api.github.com")
print(response.status_code)
print(response.json())
data = {"name":"Alice","age":25}
response = requests.post("https://api.example.com", json=data)
print(response.status_code)
200
{'current_user_url': 'https://api.github.com/user', 'current_user_authorizations_html_url': 'https://github.com/settings/connections/applications{/client_id}', 'authorizations_url': 'https://api.github.com/authorizations', 'code_search_url': 'https://api.github.com/search/code?q={query}{&page,per_page,sort,order}', 'commit_search_url': 'https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}', 'emails_url': 'https://api.github.com/user/emails', 'emojis_url': 'https://api.github.com/emojis', 'events_url': 'https://api.github.com/events', 'feeds_url': 'https://api.github.com/feeds', 'followers_url': 'https://api.github.com/user/followers', 'following_url': 'https://api.github.com/user/following{/target}', 'gists_url': 'https://api.github.com/gists{/gist_id}', 'hub_url': 'https://api.github.com/hub', 'issue_search_url': 'https://api.github.com/search/issues?q={query}{&page,per_page,sort,order}', 'issues_url': 'https://api.github.com/issues', 'keys_url': 'https://api.github.com/user/keys', 'label_search_url': 'https://api.github.com/search/labels?q={query}&repository_id={repository_id}{&page,per_page}', 'notifications_url': 'https://api.github.com/notifications', 'organization_url': 'https://api.github.com/orgs/{org}', 'organization_repositories_url': 'https://api.github.com/orgs/{org}/repos{?type,page,per_page,sort}', 'organization_teams_url': 'https://api.github.com/orgs/{org}/teams', 'public_gists_url': 'https://api.github.com/gists/public', 'rate_limit_url': 'https://api.github.com/rate_limit', 'repository_url': 'https://api.github.com/repos/{owner}/{repo}', 'repository_search_url': 'https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}', 'current_user_repositories_url': 'https://api.github.com/user/repos{?type,page,per_page,sort}', 'starred_url': 'https://api.github.com/user/starred{/owner}{/repo}', 'starred_gists_url': 'https://api.github.com/gists/starred', 'topic_search_url': 'https://api.github.com/search/topics?q={query}{&page,per_page}', 'user_url': 'https://api.github.com/users/{user}', 'user_organizations_url': 'https://api.github.com/user/orgs', 'user_repositories_url': 'https://api.github.com/users/{user}/repos{?type,page,per_page,sort}', 'user_search_url': 'https://api.github.com/search/users?q={query}{&page,per_page,sort,order}'}
201
---------------------------------------------------
import requests
from bs4 import BeautifulSoup
response = requests.get("https://example.com")
soup = BeautifulSoup(response.text, 'html.parser')
for link in soup.find_all('a'):
    print(link.get('href'))
https://iana.org/domains/example
---------------------------------------------------
from multiprocessing import Process
def print_num():
    for i in range(5):
        print(i)
process = Process(target = print_num)
process.start()
process.join()
0
1
2
3
4
---------------------------------------------------
import asyncio
async def greet():
    await asyncio.sleep(1)
    print("Hello, Async!")
asyncio.run(greet())
Hello, Async!
---------------------------------------------------
class CustomError(Exception):
    pass
try:
    raise CustomError("A Custom error occured")
except CustomError as e:
    print(e)
A Custom error occured
---------------------------------------------------
import yaml
data = {"name":"Alice", "age":25}
yaml_str = yaml.dump(data)
print(yaml_str)
age: 25
name: Alice
---------------------------------------------------
import configparser
config = configparser.ConfigParser()
config.read("config.ini")
print(config["DEFAULT"][Setting])
---------------------------------------------------
import calendar
year = int(input("Enter year : "))
month = int(input("Enter month : "))
cal = calendar.month(year, month)
print(cal)
Enter year : 2026
Enter month : 4
     April 2026
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28 29 30
---------------------------------------------------
year = int(input("Enter a year : "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 == 0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year")
Enter a year : 2024
2024 is a leap year
---------------------------------------------------
num = int(input("Enter a number : "))
flag = False
if num == 1:
    print(f"{num}, is not a prime number")
elif num > 1:
    for i in range (2, num):
        if (num % i == 0):
            flag = True
            break
if flag:
    print(f"{num}, is not prime number")
else:
    print(f"{num}, is prime number")
Enter a number : 11
11, is prime number
---------------------------------------------------
lower = int(input("Enter lower number : "))
upper = int(input("Enter upper number : "))
print("Prime numbers between {lower} and {upper} are : ")
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i == 0):
                break
        else:
            print(num, end = " ")
Enter lower number : 1
Enter upper number : 10
Prime numbers between {lower} and {upper} are : 
2 3 5 7 
---------------------------------------------------
num = int(input("Enter a number : "))
fact = 1
if num < 0:
    print("Factirial does not exist for negative numbers")
elif num == 0:
    print("Factirial of 0 is 1")
else:
    for i in range(1, num+1):
        fact = fact * i
    print(f"Factirial of number {num} is {fact}")
Enter a number : 4
Factirial of number 4 is 24
---------------------------------------------------
nterms = int(input("How many terms? : "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Enter positive integer...")
elif nterms == 1:
    print("Fibbonacci series upto ",nterms," : ")
    print(n1, end = " ")
else:
    print("Fibbonacci series : ")
    while count < nterms:
        print(n1, end = " ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
How many terms? : 10
Fibbonacci series : 
0 1 1 2 3 5 8 13 21 34 
---------------------------------------------------
num = int(input("Enter a number : "))
num_str = str(num)
num_digits = len(num_str)
sum_of_power = 0
temp_num = num
while (temp_num > 0):
    digit = temp_num % 10
    sum_of_power += digit ** num_digits
    temp_num //= 10
if sum_of_power == num:
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
Enter a number : 153
153 is Armstrong number
---------------------------------------------------
lower = int(input("Enter the lower limit of the interval: "))
upper = int(input("Enter the upper limit of the interval: "))
for num in range(lower, upper+1):
    order = len(str(num))
    temp_num = num
    sum = 0
    while (temp_num > 0):
        digit = temp_num % 10
        sum += digit ** order
        temp_num //= 10
    if num == sum:
        print(num)
Enter the lower limit of the interval: 10
Enter the upper limit of the interval: 10000
153
370
371
407
1634
8208
9474
---------------------------------------------------
def compute_lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The L.C.M. is", compute_lcm(num1, num2))
Enter the number: 54
Enter the number: 24
The L.C.M. is 216
---------------------------------------------------
def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf
num1 = int(input('Enter the number: '))
num2 = int(input('Enter the number: '))
print("The H.C.F. is", compute_hcf(num1, num2))
Enter the number: 54
Enter the number: 24
The H.C.F. is 6
---------------------------------------------------
dec_num = int(input('Enter a decimal number: '))
print("The decimal value of", dec_num, "is:")
print(bin(dec_num), "in binary.")
print(oct(dec_num), "in octal.")
print(hex(dec_num), "in hexadecimal.")
Enter a decimal number: 27
The decimal value of 27 is:
0b11011 in binary.
0o33 in octal.
0x1b in hexadecimal.
---------------------------------------------------
char = str(input("Enter the character : "))
print("The ASCII value of {char} is : ", ord(char))
Enter the character : V
The ASCII value of {char} is :  86
---------------------------------------------------
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
print("Select opearation : ")
print("1. Add ")
print("2. Subtract ")
print("3. Multiply ")
print("4. Divide ")
while True:
    choice = input("Enter choice(1/2/3/4) : ")
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input, please enter number.")
            continue
        if choice == '1':
            print(num1,"+",num2,'=',add(num1, num2))
        elif choice == '2':
            print(num1,"-",num2,'=',sub(num1, num2))
        if choice == '3':
            print(num1,"*",num2,'=',multiply(num1, num2))
        if choice == '4':
            print(num1,"/",num2,'=',divide(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/No) : ")    
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
Select opearation : 
1. Add 
2. Subtract 
3. Multiply 
4. Divide 
Enter choice(1/2/3/4) : 1
Enter first number: 3
Enter second number: 4
3.0 + 4.0 = 7.0
Let's do next calculation? (yes/No) : yes
Enter choice(1/2/3/4) : 2
Enter first number: 6
Enter second number: 1
6.0 - 1.0 = 5.0
Let's do next calculation? (yes/No) : yes
Enter choice(1/2/3/4) : 3
Enter first number: 6
Enter second number: 2
6.0 * 2.0 = 12.0
Let's do next calculation? (yes/No) : yes
Enter choice(1/2/3/4) : 90
Enter first number: 90
Enter second number: 3
90.0 / 3.0 = 30.0
Let's do next calculation? (yes/No) : no
---------------------------------------------------
def recur_fibbo(n):
    if n <= 1:
        return n
    else:
        return (recur_fibbo(n-1) + recur_fibbo(n-2))
nterms = int(input("Enter number of the terms greater than 0 : "))
if nterms <= 0:
    print("Please enter positive integer ")
else:
    print("Fibbonacci sequence : ")
    for i in range(nterms):
        print(recur_fibbo(i), end=" ")
Enter number of the terms greater than 0 : 8
Fibbonacci sequence : 
0 1 1 2 3 5 8 13 
---------------------------------------------------
def recur_facto(n):
    if n == 1:
        return n
    else:
        return n * recur_facto(n-1)
num = int(input("Enter the number : "))
if num < 0:
    print("Please enter positive integer factorial is not for negative num")
elif num == 0:
    print("The Factorial of 0 is 1")
else:
    print(f"The Factorial is : ", recur_facto(num))
Enter the number : 7
The Factorial is :  5040
---------------------------------------------------
def rotated_arr(arr, d):
    n = len(arr)
    if d < 0 or d >= n:
        return "Invalid rotation value"
    rotated_arr = [0] * n
    for i in range(n):
        rotated_arr[i] = arr[(i+d) % n]
    return rotated_arr
arr = [1, 2, 3, 4, 5]
d = 2
result = rotated_arr(arr, d)
print("Original array : ", arr)
print("Rotated array : ", result)
Original array :  [1, 2, 3, 4, 5]
Rotated array :  [3, 4, 5, 1, 2]
---------------------------------------------------
def split_and_arr(arr, k):
    if k <= 0 or k >= len(arr):
        return arr
    first_part = arr[:k]
    second_part = arr[k:]
    result = second_part + first_part
    return result
arr = [1, 2, 3, 4, 5]
k = 3
result = split_and_arr(arr, k)
print("Original array : ", arr)
print("Array after splitting and adding : ", result)
Original array :  [1, 2, 3, 4, 5]
Array after splitting and adding :  [4, 5, 1, 2, 3]
---------------------------------------------------
A monotonic array is one that is entirely non-increasing or non-decreasing
def is_monotonic(arr):
    increasing = decreasing = True
    for i in range(1, len(arr)):
        if (arr[i] > arr[i-1]):
            decreasing = False
        elif (arr[i] < arr[i-1]):
            increasing = False
    return increasing or decreasing
arr1 = [1, 2, 2, 3]
arr2 = [3, 2, 1]
arr3 = [1, 3, 2, 4]
print("arr1 is monotonic:", is_monotonic(arr1))
print("arr2 is monotonic:", is_monotonic(arr2))
print("arr3 is monotonic:", is_monotonic(arr3))
arr1 is monotonic: True
arr2 is monotonic: True
arr3 is monotonic: False
---------------------------------------------------
def add_matrices(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return "Matrices must have the same dimensions for addition"
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result
matrix1 = [
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]
]
matrix2 = [
 [9, 8, 7],
 [6, 5, 4],
 [3, 2, 1]
]
result_matrix = add_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(row)
Sum of matrices:
[10, 10, 10]
[10, 10, 10]
[10, 10, 10]
---------------------------------------------------
def multiply_matrices(mat1, mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    if cols1 != rows2:
        return "Matrix multiplication is not possible. Number of columns mismatch"
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += mat1[i][k] * mat2[k][j]
    return result
matrix1 = [
 [1, 2, 3],
 [4, 5, 6]
]
matrix2 = [
 [7, 8],
 [9, 10],
 [11, 12]
]
result_matrix = multiply_matrices(matrix1, matrix2)
if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Result of matrics multiplication :")
    for row in result_matrix:
        print(row)
Result of matrics multiplication :
[58, 64]
[139, 154]
---------------------------------------------------
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result
matrix = [
 [1, 2, 3],
 [4, 5, 6]
]
transposed_matrix = transpose_matrix(matrix)
for row in transposed_matrix:
    print(row)
[1, 4]
[2, 5]
[3, 6]
---------------------------------------------------
my_str = input("Enter a string : ")
words = [word.capitalize() for word in my_str.split()]
words.sort()
print("The sorted words are : ")
for word in words:
    print(word)
Enter a string : vaishali mangulal wankhedkar sandip vishal shiv shambhu chiku
The sorted words are : 
Chiku
Mangulal
Sandip
Shambhu
Shiv
Vaishali
Vishal
Wankhedkar
---------------------------------------------------
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
my_str = input("Enter a string : ")
no_punct = ""
for char in my_str:
    if char not in punctuations:
        no_punct = no_punct + char
print(no_punct)
/home/main.py:1: SyntaxWarning: invalid escape sequence '\,'
  punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
Enter a string : Hello!!!, he said ---and went
Hello he said and went
---------------------------------------------------
A Disarium number is a number that is equal to the sum of its digits each raised to the
power of its respective position. For example, 89 is a Disarium number because 8 + = 8 + 81 = 89.
def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return digit_sum == number
try:
    num = int(input("Enter a number : "))
    if is_disarium(num):
        print(f"{num} is a Disarium number")
    else:
        print(f"{num} is not a Disarium number")
except ValueError:
    print("Invalid input. Please enter a valid number")
Enter a number : 89
89 is a Disarium number
---------------------------------------------------
def is_disarium(number):
    num_str = str(number)
    digit_sum = sum(int(i) ** (index + 1) for index, i in enumerate(num_str))
    return digit_sum == number
disarium_num = [num for num in range(1, 101) if is_disarium(num)]
print("Disarium numbers between 1 to 100 : ")
for num in disarium_num:
    print(num, end = " | ")
Disarium numbers between 1 to 100 : 
1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 89 | 
---------------------------------------------------
19 is a Happy Number because:
The process reaches 1, so 19 is a Happy Number.
1 + = 82
2 9
2
8 + = 68
2 2
2
6 + = 100
2 8
2
1 + + = 1

def is_happy_num(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1
num = int(input("Enter a number : "))
if is_happy_num(num):
    print(f"{num} is a happy number.")
else:
    print(f"{num} is a not a happy number.")
Enter a number : 23
23 is a happy number.
---------------------------------------------------
def is_happy_num(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(i) ** 2 for i in str(num))
    return num == 1
happy_num = []
for num in range(1, 101):
    if is_happy_num(num):
        happy_num.append(num)
print("Happy numbers between 1 and 100.")
print(happy_num)
Happy numbers between 1 and 100.
[1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
---------------------------------------------------
A Harshad number (or Niven number) is an integer that is divisible by the sum of its digits.
18 is a Harshad number because , and 18 is divisible by 9
42 is not a Harshad number because , and 42 is not divisible by 6.
def is_harshad_num(num):
    digit_sum = sum(int(i) for i in str(num))
    return num % digit_sum == 0
num = int(input("Enter a number : "))
if is_harshad_num(num):
    print(f"{num} is a Harshad number.")
else:
    print(f"{num} is not a Harshad number.")
Enter a number : 18
18 is a Harshad number.
---------------------------------------------------
A pronic number, also known as an oblong number or rectangular number, is a type of
figurate number that represents a rectangle. It is the product of two consecutive integers, n
and (n + 1). Mathematically, a pronic number can be expressed as:
For example, the first few pronic numbers are:
𝑃 = 𝑛 ∗ (𝑛 + 1) 𝑛
𝑃1 = 1 ∗ (1 + 1) = 2
𝑃2 = 2 ∗ (2 + 1) = 6
𝑃3 = 3 ∗ (3 + 1) = 12
𝑃4 = 4 ∗ (4 + 1) = 20
def is_pronic_num(num):
    for n in range(1, int(num ** 0.5)+1):
        if n * (n + 1) == num:
            return True
    return False
print("Pronic numbers between 1 and 100 are : ")
for i in range(1, 101):
    if is_pronic_num(i):
        print(i, end = " | ")
Pronic numbers between 1 and 100 are : 
2 | 6 | 12 | 20 | 30 | 42 | 56 | 72 | 90 | 
---------------------------------------------------
numbers = [30, 10, 45, 5, 20]
numbers.sort(reverse = True)
if len(numbers) >= 2:
    second_largest = numbers[1]
    print("The second largest number in the list is:", second_largest)
else:
    print("The list does not contain a second largest number.")
The second largest number in the list is: 30
---------------------------------------------------
def find_n_largest_ele(lst, n):
    sorted_lst = sorted(lst, reverse=True)
    largest_ele = sorted_lst[:n]
    return largest_ele
numbers = [30, 10, 45, 5, 20, 50, 15, 3, 345, 54, 67, 87, 98, 100, 34]
N = int(input("N = "))
result = find_n_largest_ele(numbers, N)
print(f"The {N} largest number in the list are :", result)
N = 3
The 3 largest number in the list are : [345, 100, 98]
---------------------------------------------------
list_of_lists = [[1, 2, 3], [], [4, 5], [], [6, 7, 8], []]
filtered_list = [i for i in list_of_lists if i]
print("List after removing empty lists:", filtered_list)
List after removing empty lists: [[1, 2, 3], [4, 5], [6, 7, 8]]
---------------------------------------------------
def count_occurance(l, element):
    count = l.count(element)
    return count
my_list = [1, 2, 3, 4, 2, 5, 2, 3, 4, 6, 5]
element_to_count = 2
occurances = count_occurance(my_list, element_to_count)
print(f"The element {element_to_count} appears {occurances} times in list")
The element 2 appears 3 times in list
---------------------------------------------------
def find_words(words, k):
    result = []
    for i in words:
        if len(i) > k:
            result.append(i)
    return result
word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = 5
long_words = find_words(word_list, k)
print(f"Words longer than {k} characters: {long_words}")
Words longer than 5 characters: ['banana', 'cherry', 'elderberry', 'dragonfruit']
---------------------------------------------------
def remove_char(input_str, i):
    if i < 0 or i >= len(input_str):
        print(f"Invalid index {i}. The string remains unchanged.")
        return input_str
input_str = "Hello, wWorld!"
i = 7
new_str = remove_char(input_str, i)
print(f"Original String : {input_str}")
print(f"String after removing {i}th character: {new_str}")
Original String : Hello, wWorld!
String after removing 7th character: None
---------------------------------------------------
input_str = "Python program to split and join a string"
word_list = input_str.split()
separator = " "
output_str = separator.join(word_list)
print("Original String:", input_str)
print("List of split Words:", word_list)
print("Joined String:", output_str)
Original String: Python program to split and join a string
List of split Words: ['Python', 'program', 'to', 'split', 'and', 'join', 'a', 'string']
Joined String: Python program to split and join a string
---------------------------------------------------
def is_binary_str(input_str):
    for i in input_str:
        if i not in '01':
            return False
    return True
input_str = "1001110"
if is_binary_str(input_str):
    print(f"'{input_str}' is a binary string.")
else:
    print(f"'{input_str}' is not a binary string.")
'1001110' is a binary string.
---------------------------------------------------
def uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())
    uncommon_words_set = words1.symmetric_difference(words2)
    uncommon_words_list = list(uncommon_words_set) 
    return uncommon_words_list
string1 = "This is first string"
string2 = "This is second string"
uncommon = uncommon_words(string1, string2)
print("Uncommon words : ", uncommon)
Uncommon words :  ['second', 'first']
---------------------------------------------------
def find_duplicates(input_str):
    char_count = {}
    duplicates = []
    for i in input_str:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    for i, count in char_count.items():
        if count > 1:
            duplicates.append(i)
    return duplicates
input_string = "piyush sharma"
duplicate_chars = find_duplicates(input_string)
print("Duplicate characters : ", duplicate_chars)
Duplicate characters :  ['s', 'h', 'a']
---------------------------------------------------
import re
def check_special_char(in_str):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\'"\-=]'  
    if re.search(pattern, in_str):
        return True
    else:
        return False
input_string = str(input("Enter a string : "))
contains_special = check_special_char(input_string)
if contains_special:
    print("The string contains special characters. ")
else:
    print("The string does not contains special characters. ")
Enter a string : "Hello, World $!"
The string contains special characters. 
---------------------------------------------------
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}
uni_val = set()
for i in my_dict.values():
    uni_val.add(i)
unique_values_list = list(uni_val)
print("Uniques values in the dictionary : ", unique_values_list)
Uniques values in the dictionary :  [10, 20, 30]
---------------------------------------------------
my_dict = {
 'a': 10,
 'b': 20,
 'c': 10,
 'd': 30,
 'e': 20
}
total_sum = 0 
for i in my_dict.values():
    total_sum += i
print("sum of all the items dictionary : ", total_sum)
sum of all the items dictionary :  90
---------------------------------------------------
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print("Merged dictionary (using dictionary unpacking) is : ", merged_dict)
Merged dictionary (using dictionary unpacking) is :  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
---------------------------------------------------
key_values_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
flat_dict = {}
for key, value in key_values_list:
    flat_dict[key] = value
print("Flat dictionary : ", flat_dict)
Flat dictionary :  {'a': 1, 'b': 2, 'c': 3, 'd': 4}
---------------------------------------------------
from collections import OrderedDict
ordered_dict = OrderedDict([('b', 2), ('c', 3), ('d', 4)])
new_item = ('a',1)
new_ordered_dict = OrderedDict([new_item])
new_ordered_dict.update(ordered_dict)
print("Updated Ordered Dict : ", new_ordered_dict)
Updated Ordered Dict :  OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})
---------------------------------------------------
from collections import OrderedDict
def check_order(string, reference):
    string_dict = OrderedDict.fromkeys(string)
    reference_dict = OrderedDict.fromkeys(reference)
    return string_dict == reference_dict
input_string = "hello world"
reference_string = "helo wrd"
if check_order(input_string, reference_string):
    print("The order of characters in the input string matches the reference string")
else:
    print("The order of characters in the input string does not matche the reference string")
The order of characters in the input string matches the reference string
---------------------------------------------------
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_keys = dict(sorted(sample_dict.items()))
print("Sorted by Keys : ")
for key, value in sorted_dict_by_keys.items():
    print(f"{key} : {value}")
Sorted by Keys : 
apple : 3
banana : 1
cherry : 2
date : 4
---------------------------------------------------
sample_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict_by_values = dict(
    sorted(sample_dict.items(), key=lambda item: item[1]))
print("Sorted by values:")
for key, value in sorted_dict_by_values.items():
    print(f"{key}: {value}")
Sorted by values:
banana: 1
cherry: 2
apple: 3
date: 4
---------------------------------------------------
import math
C = 50
H = 30
def calculate_Q(D):
    return int(math.sqrt((2 * C * D) / H))
input_seq = input("Enter comma seperated values of D: ")
D_values = input_seq.split(',')
result = [calculate_Q(int(D)) for D in D_values]
print(','.join(map(str, result)))
Enter comma seperated values of D: 100,150,180
18,22,24
---------------------------------------------------
X,Y = map(int, input("Enter two digits (X, Y): ").split(','))
array = [[0 for j in range(Y)] for i in range(X)]
for i in range(X):
    for j in range(Y):
        array[i][j] = i * j
for row in array:
    print(row)
Enter two digits (X, Y): 3,5
[0, 0, 0, 0, 0]
[0, 1, 2, 3, 4]
[0, 2, 4, 6, 8]
---------------------------------------------------
input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split()
sorted_words = sorted(words)
sorted_sequence = ','.join(sorted_words)
print("Sorted words : ", sorted_sequence)
Enter a comma-separated sequence of words: without, hello, bag, world
Sorted words :  bag,,hello,,without,,world
---------------------------------------------------
input_sequence = input("Enter a comma-separated sequence of words: ")
words = input_sequence.split()
sorted_words = sorted(words)
result = ' '.join(sorted_words)
print("Result : ", result)
Enter a comma-separated sequence of words: hello world and practice makes perfect and hello world again
Result :  again and and hello hello makes perfect practice world world
---------------------------------------------------
sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char in sentence:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1
print("LETTERS", letter_count)
print("DIGITS", digit_count)
Enter a sentence: hello world! 123
LETTERS 10
DIGITS 3
---------------------------------------------------
import re
def is_valid_password(password):
    if 6 <= len(password) <= 12:
        if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])", password):
            return True
        return False
password = input("Enter passwords separated by commas: ").split(',')
valid_passwords = []
for psw in password:
    if is_valid_password(psw):
        valid_passwords.append(psw)
print(','.join(valid_passwords))
Enter passwords separated by commas: ABd1234@1,a F1#,2w3E*,2We3345
ABd1234@1
---------------------------------------------------
input_sentence = input("Enter a sentence: ")
words = input_sentence.split()
word_freq = {}
for word in words:
    word = word.strip('.,?')
    word = word.lower()
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
sorted_words = sorted(word_freq.items())
for word, frequency in sorted_words:
    print(f"{word}:{frequency}")
Enter a sentence: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
2:2
3:1
3?read:1
and:1
between:1
choosing:1
new:1
or:2
python:5
to:1
---------------------------------------------------
subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Hockey", "Football"]
sentences = []
for sub in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{sub} {verb} {obj}"
            sentences.append(sentence)
for sentence in sentences:
    print(sentence)
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football
---------------------------------------------------
import zlib
string = "hello world!hello world!hello world!hello world!"
compressed_string = zlib.compress(string.encode())
decompressed_string = zlib.decompress(compressed_string).decode()
print("Original String:", string)
print("Compressed String:", compressed_string)
print("Decompressed String:", decompressed_string)
Original String: hello world!hello world!hello world!hello world!
Compressed String: b'x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82\r\x00\xbd[\x11\xf5'
Decompressed String: hello world!hello world!hello world!hello world!
---------------------------------------------------
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 4
result = binary_search(sorted_list, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}")
else:
    print(f"Element {target_element} not found in the list")
Element 4 found at index 3
---------------------------------------------------
def divisible_by_5_and_7(n):
    for num in range(n + 1):
        if num % 5 == 0 and num % 7 == 0:
            yield num
try:
    n = int(input("Enter a value for n: "))
    result = divisible_by_5_and_7(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
Enter a value for n: 100
0,35,70
---------------------------------------------------
def fibbonacci(n):
    sequence = [0, 1]
    [sequence.append(sequence[-1] + sequence[-2]) for _ in range(2, n)]
    return sequence
try:
    n = int(input("Enter a value for n: "))
    result = fibbonacci(n)
    print(','.join(map(str, result)))
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
Enter a value for n: 8
0,1,1,2,3,5,8,13
---------------------------------------------------
def extract_username(email):
    parts = email.split('@')
    if len(parts) == 2:
        return parts[0]
    else:
        return "Invalid email format"
try:
    email = input("Enter an email address: ")
    username = extract_username(email)
    print(username)
except ValueError:
    print("Invalid input. Please enter a valid integer for n.")
Enter an email address: john@google.com
john
---------------------------------------------------
class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length ** 2
shape = Shape()
square = Square(float(input("Enter the shape of the square : ")))
print("Shape's area by default:", shape.area()) 
print("Area of the square:", square.area()) 
Enter the shape of the square : 5
Shape's area by default: 0
Area of the square: 25.0
---------------------------------------------------
def stutter(word):
    if len(word) < 2:
        return "Word must be at least two characters long."
    stutter_word = f"{word[:2]} ... {word[:2]} ... {word}?"
    return stutter_word
print(stutter("incredible")) 
print(stutter("enthusiastic")) 
print(stutter("outstanding")) 
in ... in ... incredible?
en ... en ... enthusiastic?
ou ... ou ... outstanding?
---------------------------------------------------
import math
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return round(degrees, 1)
print(radians_to_degrees(1))
print(radians_to_degrees(20))
print(radians_to_degrees(50))
57.3
1145.9
2864.8
---------------------------------------------------
def is_curzon(num):
    numerator = 2 ** num + 1
    denominator = 2 * num + 1
    return numerator % denominator == 0
print(is_curzon(5)) 
print(is_curzon(10)) 
print(is_curzon(14))
True
False
True
---------------------------------------------------
import math
def area_of_hexagon(x):
    area = (3 * math.sqrt(3) * x**2) / 2
    return round(area, 1)
print(area_of_hexagon(1)) 
print(area_of_hexagon(2)) 
print(area_of_hexagon(3))
2.6
10.4
23.4
---------------------------------------------------
import math
def binary(decimal):
    binary_str = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_str = str(remainder) + binary_str
        decimal = decimal // 2
    return binary_str if binary_str else "0"
print(binary(1)) 
print(binary(5)) 
print(binary(10))
1
101
1010
---------------------------------------------------
def evenly_divisible(a, b, c):
    total = 0
    for num in range(a, b+1):
        if num % c == 0:
            total += num
    return total
print(evenly_divisible(1, 10, 20)) 
print(evenly_divisible(1, 10, 2)) 
print(evenly_divisible(1, 10, 3))
0
30
18
---------------------------------------------------
def correct_signs(expression):
    try:
        return eval(expression)
    except:
        return False
print(correct_signs("3 < 7 < 11"))
print(correct_signs("13 > 44 > 33 < 1"))
print(correct_signs("1 < 2 < 6 < 9 > 3"))
True
False
True
---------------------------------------------------
def replace_vowels(string, char):
    vowels = "AEIOUaeiou"
    for vowel in vowels:
        string = string.replace(vowel, char)
    return string
print(replace_vowels("the aardvark", "#"))
print(replace_vowels("minnie mouse", "?"))
print(replace_vowels("shakespeare", "*"))
th# ##rdv#rk
m?nn?? m??s?
sh*k*sp**r*
---------------------------------------------------
def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("Input string must have same length")
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance
print(hamming_distance("abcde", "bcdef"))
print(hamming_distance("abcde", "abcde"))
print(hamming_distance("strong", "strung"))
5
0
1
---------------------------------------------------
def filter_list(lst):
    result = []
    for element in lst:
        if isinstance(element, int) and element >= 0:
            result.append(element)
    return result
print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
print(filter_list([1, "a", "b", 0, 15]))
[1, 2]
[1, 2, 123]
[1, 0, 15]
---------------------------------------------------
num = int(input("Enter number : "))
fact = 1
if num in (0, 1):
    fact = 1
else:
    for i in range(1, num+1):
        fact = fact * i
print(f"Factorial of {num} is : {fact}")
Enter number : 5
Factorial of 5 is : 120
---------------------------------------------------
text = input("Enter string to check if it is palindrome or not : ")
rev = ""
tempstr = ""
for i in text:
    if i.isalnum():
        rev = i + rev
        tempstr += i
if tempstr == rev:
    print("Given string is palindrome")
else:
    print(f"Given string is not palindrome")
Enter string to check if it is palindrome or not : madam
Given string is palindrome
---------------------------------------------------
text = input("Enter a string to find palindrome or not: ").lower()
rev = ""
tempstr = ""
for i in text:
    if i.isalnum(): 
        rev = i + rev
        tempstr += i
if tempstr == rev:
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
Enter a string to find palindrome or not: Was it a car or a cat I saw?
Given string is palindrome
---------------------------------------------------
text = str(input("Enter string to count vowels and consonents : ")).lower()
vowels = 'aeiou'
vowels_cnt = 0
consonents_cnt = 0
for i in text:
    if i.isalpha():
        if i in vowels:
            vowels_cnt += 1
        else:
            consonents_cnt += 1
print(f"Vowels : {vowels_cnt}, Consonents : {consonents_cnt}")
Enter string to count vowels and consonents : Ashish Sunil Zope
Vowels : 6, Consonents : 9
---------------------------------------------------
num = int(input("Enter num : "))
sum = 0
temp = abs(num)
while temp > 0:
    sum += temp % 10
    temp //= 10
print(f"All digits if {num} : {sum}")
Enter num : 17121996
All digits if 17121996 : 36
---------------------------------------------------
def srt(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
    return array #(return sorted(array))

if __name__ == "__main__":
    array = [1, 5, 2, 6, 7, 9, 2]
    print(srt(array))
[1, 2, 2, 5, 6, 7, 9]
---------------------------------------------------
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
Enter temperature in Celsius: 37
37.0°C is equal to 98.60°F
---------------------------------------------------
num = int(input("Enter a number to check prime or not: "))
if num <= 1:
    print(f"{num} is neither Prime nor Composite number")
else:
    isPrime=True
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        print("Given number is a Prime number")
    else:
        print("Given number is a Composite number")
Enter a number to check prime or not: 17
Given number is a Composite number
---------------------------------------------------
nth_term = int(input("Enter number of terms to generate "))
a, b = 0, 1
print("Fibonacci series upto Nth term:")
for i in range(nth_term):
    print(a, end = " ")
    a, b = b, a+b
Enter number of terms to generate 15
Fibonacci series upto Nth term:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 
---------------------------------------------------
year = int(input("Enter year in YYYY format to check if a year is a leap year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
Enter year in YYYY format to check if a year is a leap year: 2024
2024 is a leap year
---------------------------------------------------
sentence = str(input("Enter a sentences :"))
wordcount = 1 if len(sentence.strip()) > 0 else 0
for i in sentence:
    if i == " ":
        wordcount += 1
print(f"Total number of words in given sentence is {wordcount}")
Enter a sentences :Ashish Sunil Zope Senior Data engineer
Total number of words in given sentence is 6
---------------------------------------------------
list = list(map(int, input("Enter name seperated by space : ").split()))
if len(list) < 2:
    print("List should have at least 2 numbers.")
else:
    first = second = float('-inf')
    for num in list:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        print("No second largest number (all elements might be equal).")
    else:
        print(f"Second largest number is {second}.")
Enter name seperated by space : 8 3 9 3 5 0 3
Second largest number is 8.
---------------------------------------------------
list = list(map(int, input("Enter numbers seperated by space : ").split()))
uniq_list = []
for i in list:
    if i not in uniq_list:
        uniq_list.append(i)
print("List with duplicate elements : ", uniq_list)
Enter numbers seperated by space : 4 2 4 6 2 5 8 0 3 3
List with duplicate elements :  [4, 2, 6, 5, 8, 0, 3]
---------------------------------------------------
num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))
def fn_find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
gcd = fn_find_gcd(num_1, num_2)
print(f"GCD of {num_1} and {num_2} is : {gcd}")
Enter the first number : 56
Enter the second number : 98
GCD of 56 and 98 is : 14
---------------------------------------------------
list = list(map(int, input("Enter numbers seperated by space : ").split()))
for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i] > list[j]:
            list[i], list[j] = list[j], list[i]
print("Sorted list is : ", list)
Enter numbers seperated by space : 34 23 567 23 678 89
Sorted list is :  [23, 23, 34, 89, 567, 678]
---------------------------------------------------
list_1 = list(map(int, input("Enter first list (space seperated) : ").split()))
list_2 = list(map(int, input("Enter second list (space seperated) : ").split()))
common_ele = []
for i in list_1:
    if i in list_2 and i not in common_ele:
        common_ele.append(i)
print("Common elements in list are : ", common_ele)
Enter first list (space seperated) : 7 4 6 3 8 9 1 2 5 7 8 2
Enter second list (space seperated) : 1 2 5 9 5 6 2 3 7 0 1 2
Common elements in list are :  [7, 6, 3, 9, 1, 2, 5]
---------------------------------------------------
(.venv) PS C:\Users\vwank\PycharmProjects\Python_Aug25\Pytest> 
---------------------------------------------------
list_1 = list(map(int, input("Enter first list (space seperated) : ").split()))
list_2 = list(map(int, input("Enter second list (space seperated) : ").split()))
merged_list = []
i, j = 0, 0
while i < len(list_1) and j < len(list_2):
    if list_1[i] < list_2[j]:
        merged_list.append(list_1[i])
        i += 1
    else:
        merged_list.append(list_2[i])
        j += 1
merged_list += list_1[i:]
merged_list += list_2[j:]
print("Merged list is : ", merged_list)
Enter first list (space seperated) : 4 433 344 34 7
Enter second list (space seperated) : 45 23 56 78
Merged list is :  [4, 23, 23, 23, 23, 433, 344, 34, 7]
---------------------------------------------------
list = list(map(str, input("Enter second sorted list : ").split()))
isDigit = True
for i in list:
    if not i.isdigit():
        isDigit = False
        break
print("List contains only digit. "if isDigit else "List contain non-digit elements")
Enter second sorted list : Ashish Sunil Zope 28-10-1996 28 7744046830
List contain non-digit elements
---------------------------------------------------
import string
sentence = input("Enter string : ")
sent_no_punc = ""
for i in sentence:
    if i not in string.punctuation:
        sent_no_punc += i
print("Without punctuation : ", sent_no_punc)
Enter string : Ashish Sunil Zope, Senior Data Engineer: turning messy data into
insights—faster than tea...!!!Without punctuation :  Ashish Sunil Zope Senior Data Engineer turning messy data into
---------------------------------------------------
binary_num = input("Enter a binary number: ")
if not all (bit in "01" for bit in binary_num):
    print("Invalid input!! Please enter only 0s and 1s")
else:
    decimal_num = int(binary_num, 2)
    print(f"The decimal value of binary {binary_num} is {decimal_num}")
Enter a binary number: 1010010101
The decimal value of binary 1010010101 is 661
---------------------------------------------------
num = int(input("Enter decimal number : "))
bin_no = ""
temp = num
if num == 0:
    bin_no = "0"
while num > 0:
    bin_no = str(num % 2) + bin_no
    num //= 2
print(f"The binary value of decimal number {temp} is {bin_no}")
Enter decimal number : 18
The binary value of decimal number 18 is 10010
---------------------------------------------------
sentence = input("Enter string : ")
freq = {}
for char in sentence:
    if char != " ":
        freq[char] = freq.get(char,0)+1
max_char = ""
max_count = 0
for char, count in freq.items():
    if count > max_count:
        max_char = char
        max_count = count
print()
print(f"The maximum occuring character is '{max_char}' with {max_count} occurances.")
Enter string : shish Sunil Zope, Senior Data Engineer: turning messy data into insights—faster than tea...!!!
The maximum occuring character is 'n' with 9 occurances.
---------------------------------------------------
str1 = input("Enter first string : ").replace(" ", "").lower()
str2 = input("Enter second string : ").replace(" ", "").lower()
if len(str1) != len(str2):
    print("No, the strings are not anagrams.")
else:
    freq = {}
    for ch in str1:
        freq[ch] = freq.get(ch, 0)+1
    for ch in str2:
        if ch in freq:
            freq[ch] -= 1
        else:
            freq[ch] = 1
if all(value==0 for value in freq.values()):
    print("Yes, the strings are anagrams.")
else:
    print("No, given strings are not anagrams.")
Enter second string : silent
Yes, the strings are anagrams.
---------------------------------------------------
str = input("Enter a string : ")
upper = lower = 0
for char in str:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
print(f"upper : {upper}, lower : {lower}")
Enter a string : Ashish Sunil Zope, Senior Data Engineer
upper : 6, lower : 27
---------------------------------------------------
str = input("Enter a string : ")
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
print(f"Capitalized : {result}")
Enter a string : ashish sunil zope senior data engineer
Capitalized : Ashish Sunil Zope Senior Data Engineer
---------------------------------------------------
str = input("Enter a string : ")
result = ""
new_word = True
for char in str:
    if char == " ":
        result += "_"
    else:
        result += char
print(f"Result : {result}")
Enter a string : Ashish Sunil Zope Senior Data Engineer
Result : Ashish_Sunil_Zope_Senior_Data_Engineer
---------------------------------------------------
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = int(input("Enter time in years: "))
n = int(input("Enter number of times interest applied per year: "))
amount = principal * (1 + rate/(100*n))**(n*time)
print(f"Compound Interest Amount: {amount:.2f}")
Enter principal amount: 100000
Enter annual interest rate (%): 13.74
Enter time in years: 10
Enter number of times interest applied per year: 12
Compound Interest Amount: 392039.88
---------------------------------------------------
