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
****************************************************************************
class Microorganism:
    def __init__(self,name,product):
        self.name = name
        self.product = product
    @property
    def show(self):
        return self.name+'produces'+self.product+'enzyme'
organism = Microorganism('Aspergillus niger', 'inulinase')
print(f'Microorganism name: {organism.name}')
print(f'Microorganism product: {organism.product}')
print(f'Message: {organism.show}')
Microorganism name: Aspergillus niger
Microorganism product: inulinase
Message: Aspergillus nigerproducesinulinaseenzyme
****************************************************************************
class Microorganism:
    @staticmethod
    def name():
        print('Aspergillus niger is a fungus that produces inulinase enzyme.')
organism = Microorganism()
organism.name()
Microorganism.name()
Aspergillus niger is a fungus that produces inulinase enzyme.
Aspergillus niger is a fungus that produces inulinase enzyme.
****************************************************************************
class Microorganism:
    def __init__(self,name,product):
        self.name = name
        self.product = product
    @classmethod
    def display(cls):
        return cls('Aspergillus niger', 'inulinase')
organism = Microorganism.display()
print(f'The fungus {organism.name} produces {organism.product} enzyme.')
The fungus Aspergillus niger produces inulinase enzyme.
****************************************************************************
import functools
def iterate(numbers):
    def decorate_iterate(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(numbers):
                worth = function(*args, **kwargs)
            return worth
        return wrapper
    return decorate_iterate
@iterate(numbers=4)
def function_one(name):
    print(f'{name}')
x = function_one('Python')
Python
Python
Python
Python
****************************************************************************
def arguments(func):
    def wrapper_arguments(argument_1, argument_2):
        print(f'The arguments are {argument_1} and {argument_2}.')
        func(argument_1, argument_2)
    return wrapper_arguments
@arguments
def programming_language(lang_1, lang_2):
    print(f'My favourite programming languages are: {lang_1} and {lang_2}')
programming_language("Python", "R")
The arguments are Python and R.
My favourite programming languages are: Python and R
****************************************************************************
Arbtrary arguments
import math
def arbitrary_argument(func):
    def wrapper(*args, **kwargs):
        print(f'These are positional arguments: {args}')
        print(f'These are keyword arguments: {kwargs}')
        return func(*args, **kwargs)  # pass both
    return wrapper
# 1. Without arguments decorator
print("1. Without arguments decorator")
@arbitrary_argument
def without_argument():
    print("There is no argument in this decorator.")
without_argument()
# 2. With positional arguments decorator
print("\n2. With positional arguments decorator")
@arbitrary_argument
def with_positional_argument(x1, x2, x3, x4, x5, x6):
    print("Values:", x1, x2, x3, x4, x5, x6)
with_positional_argument(math.inf, math.tau, math.pi, math.e, math.nan, -math.inf)
# 3. With keyword arguments decorator
print("\n3. With keyword arguments decorator")
@arbitrary_argument
def with_keyword_argument(**kwargs):
    print("Python and R are my favorite programming languages and keyword arguments.")
    for k, v in kwargs.items():
        print(f"{k} = {v}")
with_keyword_argument(language_1="Python", language_2="R")
1. Without arguments decorator
These are positional arguments: ()
These are keyword arguments: {}
There is no argument in this decorator.
2. With positional arguments decorator
These are positional arguments: (inf, 6.283185307179586, 3.141592653589793, 2.718281828459045, nan, -inf)
These are keyword arguments: {}
Values: inf 6.283185307179586 3.141592653589793 2.718281828459045 nan -inf
3. With keyword arguments decorator
These are positional arguments: ()
These are keyword arguments: {'language_1': 'Python', 'language_2': 'R'}
Python and R are my favorite programming languages and keyword arguments.
language_1 = Python
language_2 = R
****************************************************************************
Debuggng decorators
import functools
def capitalize_dec(function):
    @functools.wraps(function)
    def wrapper():
        return function().capitalize()
    return wrapper
@capitalize_dec
def message():
    "Python is the most popular programming language."
    return  'PYTHON IS THE MOST POPULAR PROGRAMMING LANGUAGE. '
print(message())
print()
print(message.__doc__)
print(message.__name__)
Python is the most popular programming language. 

Python is the most popular programming language.
message
****************************************************************************
Preservng decorators
from functools import wraps

def preserved_decorator(function):
    @wraps(function)  # This preserves name, docstring, etc.
    def wrapper():
        print('Before calling the function, this is printed.')
        function()
        print('After calling the function, this is printed.')
    return wrapper

@preserved_decorator
def message():
    """This function prints the message when it is called."""
    print('Python is the most popular programming language.')

message()

# Print function metadata
print("Function Name:", message.__name__)
print("Docstring:", message.__doc__)
print("Class:", message.__class__)
print("Module:", message.__module__)
print("Code Object:", message.__code__)
print("Closure:", message.__closure__)
print("Annotations:", message.__annotations__)
print("Dir:", message.__dir__())
print("Format:", message.__format__(''))
C:\Users\vwank\PycharmProjects\PythonProject4\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
Before calling the function, this is printed.
Python is the most popular programming language.
After calling the function, this is printed.
Function Name: message
Docstring: This function prints the message when it is called.
Class: <class 'function'>
Module: __main__
Code Object: <code object wrapper at 0x000002D421085B30, file "C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py", line 4>
Closure: (<cell at 0x000002D42109A4A0: function object at 0x000002D4210BB920>,)
Annotations: {}
Dir: ['__wrapped__', '__new__', '__repr__', '__call__', '__get__', '__closure__', '__doc__', '__globals__', '__module__', '__builtins__', '__code__', '__defaults__', '__kwdefaults__', '__annotations__', '__dict__', '__name__', '__qualname__', '__type_params__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__init__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
Format: <function message at 0x000002D4210BB9C0>
****************************************************************************

****************************************************************************
