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

*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************
