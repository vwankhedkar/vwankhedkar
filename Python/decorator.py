import math
def outer_addition(function):
    def inner(a,b):
        if a < b:
            a, b = b, a
        return function(a,b)
    return inner
@outer_addition
def addition(a, b):
    print(a + b)
result = outer_addition(addition)
result(math.pi, math.e)
OUTPUT - 5.859874482048838
*******************************************************************
def decorator_text_uppercase(func):
    def wrapper():
        function = func()
        text_uppercase = function.upper()
        return text_uppercase
    return wrapper
def text():
    return "Python is most popular language"
decorated_result = decorator_text_uppercase(text)
print(decorated_result())
@decorator_text_uppercase
def text():
    return "Python is most popular language"
print(text())
PYTHON IS MOST POPULAR LANGUAGE
PYTHON IS MOST POPULAR LANGUAGE
*******************************************************************
def do_twice(function):
    def wrapper_do_twice():
        function()
        function()
    return wrapper_do_twice
@do_twice
def text():
    print("Python is programming language")
text()
OUTPUT :
Python is programming language
Python is programming language
**********************************************************************
def do_twice(function):
    def wrapper_function(*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper_function
@do_twice
def text(programming_language):
    print(f'{programming_language} is a programming_language')
text('Python')
Python is a programming_language
Python is a programming_language
*************************************************************************
def do_twice(function):
    def wrapper_function(*args, **kwargs):
        function(*args, **kwargs)
        function(*args, **kwargs)
    return wrapper_function
@do_twice
def returning(programming_language):
    print('Python is programming language.')
    return f'Hello, {programming_language}'
hello_python = returning('Python')
Python is programming language.
Python is programming language.
***************************************************************************
class FirstClass:
    def __init__(self):
        pass
    def something_useful(self,string):
        return string

class Decorator:
    def __init__(self,wrapped):
        self._wrapped = wrapped
    def withUnderscores(self,string):
        return "_".join(string.split())
    def __getattr__(self,name):
        return getattr(self._wrapped,name)

def div(a,b):
    print(a/b)

def smart(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart(div)
div1(2,4)

OUTPUT - 2.0

def my_decor(func):
    def wrapper():
        print("Inside before wrapper")
        func()
        print("Inside after wrapper")
    return wrapper
@my_decor
def hello():
    print("Hello")
hello()
OUTPUT -
Inside before wrapper
Hello
Inside after wrapper
