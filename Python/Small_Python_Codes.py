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
*************************************************************************************************
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
***********************************************************************
