import time
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print("union_set", union_set)
time.sleep(1)
intersection_set = set1 & set2
print("intersection_set", intersection_set)
time.sleep(1)
difference_set = set1 - set2
print("difference_set", difference_set)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
union_set {1, 2, 3, 4, 5}
intersection_set {3}
difference_set {1, 2}
*******************************************************************************
# Zip
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
combined = zip(names, scores)
print(list(combined))

# Enumerate
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
[('Alice', 85), ('Bob', 90), ('Charlie', 95)]
0: apple
1: banana
2: cherry
*******************************************************************************
# List Comprehension
numbers = [1,2,3,4,5]
square = [x**2 for x in numbers]
print("List Comprehension :", square)

#Dictionary Comprehension
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
age_dict = {name:age for name, age in zip(names, ages)}
print("Dictionary Comprehension: ", age_dict)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
List Comprehension : [1, 4, 9, 16, 25]
Dictionary Comprehension:  {'Alice': 25, 'Bob': 30, 'Charlie': 35}
*******************************************************************************
# Iterator
numbers = [1,2,3]
iterator = iter(numbers)
print(next(iterator))

# Generator
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
counter = count_up_to(3)
for num in counter:
    print(num, end=" ")
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
1
1 2 3 
*******************************************************************************
Decorators
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper()
@decorator
def say_hello():
    print("Hello")
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Before function call
Hello
After function call
*******************************************************************************
class Car:
    # Class attribute (shared by all cars)
    wheels = 4
    # Constructor (used to create objects)
    def __init__(self, brand, model):
        self.brand = brand # Instance attribute
        self.model = model # Instance attribute
    # Method (action)
    def display_info(self):
        print(f"{self.brand} {self.model} has {self.wheels} wheels.")
my_car = Car("Toyota", "Corolla")
my_car.display_info()
OUTPUT -------    Toyota Corolla has 4 wheels.
---------------------------------------
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print(f"{self.name} says Woof!")
dog = Dog("Buddy", "Golden Retriever")
dog.bark() # Calling a method
OUTPUT ------    Buddy says Woof!
*******************************************************************************
class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog Barks")
dog = Dog()
dog.speak()
OUTPUT         -------------------    Dog Barks
*******************************************************************************
# Encapsulation: Hiding Data Inside an Object
class Car:
    def __init__(self,brand,speed):
        self.__brand = brand
        self.__speed = speed
    def accelerate(self, increment):
        if increment > 0:
            self.__speed += increment
    def brake(self,decrement):
        if decrement > 0 and self.__speed-decrement>=0:
            self.__speed-=decrement
    def get_speed(self):
        return self.__speed
    def get_brand(self):
        return self.__brand
my_car = Car("Toyota", 50) # Create a Car object with brand "Toyota" and speed 50
print(my_car.get_speed()) # Output: 50
my_car.accelerate(30) # Accelerate the car by 30
print(my_car.get_speed()) # Output: 80
my_car.brake(20) # Apply the brake to reduce speed by 20
print(my_car.get_speed()) # Output: 60
50
80
60
*******************************************************************************
Polymorphism: One Method, Different Behaviors
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
*******************************************************************************
Abstraction: Hiding Complex Details
from abc import ABC, abstractmethod
class Animal(ABC): # Abstract class
    @abstractmethod
    def speak(self):
        pass # Must be defined in child classes
class Dog(Animal):
    def speak(self):
        print("Woof")
dog = Dog()
dog.speak()
OUTPUT     --    Woof
*******************************************************************************
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
with open("example.txt", "w") as file:
    file.write("Hello World! \n")
    file.write("Hello India! \n")
with open("example.txt", "a") as file:
    file.write("New log entry \n")
with open("example.txt", "r") as file:
    content = file.read()
print(content)
Hello World! 
Hello India! 
New log entry 
*******************************************************************************
from functools import reduce
numbers = [1, 2, 3, 4]
square = list(map(lambda x:x**2, numbers))
print(square)
even_nums = list(filter(lambda x:x%2==0, numbers))
print(even_nums)
product = reduce(lambda x,y:x*y, numbers)
print(product)
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
[1, 4, 9, 16]
[2, 4]
24
*******************************************************************************
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("This always runs!")
Division successful!
This always runs!
*******************************************************************************
def fib(n):
    a, b = 0, 1
    sequence = []
    while a<n:
        sequence.append(a)
        a, b = b, a+b
    return sequence
max_price = 1000
retracement_levels = fib(max_price)
print("Fibbonacci series is: ", retracement_levels)
Fibbonacci series is:  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987]
*******************************************************************************
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old"
person1 = Person("Alice", 25)
print(person1.greet())
OUTPUT    ------    Hello, my name is Alice and I am 25 years old
*******************************************************************************
numbers = [4, 7, 3, 5, 8, 9]
square = [x**2 for x in numbers]
print(square)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
[16, 49, 9, 25, 64, 81]
[3, 4, 5, 7, 8, 9]
[9, 8, 7, 5, 4, 3]
*******************************************************************************
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))        ====>    120
