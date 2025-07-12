def memoize(fn):
    cache = {}
    def helper(x):
        if x not in cache:
            # The @memoize decorator is used to cache the results of the factorial function. 
            cache[x] = fn(x)
        return cache[x]
    return helper
@memoize
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
result = factorial(3)
print(result)    ===>  6
***********************************************************************
def caesar_cipher(text, shift) :
    result = ""
    for char in text:
        if char.isalpha() :
            # Determine if the character is uppercase or lowercase
            is_upper = char. isupper()
            char = char.lower() # Convert to lowercase for shifting
            shifted = chr(((ord(char) - ord('a' ) + shift) % 26) + ord( 'a' ))
            if is_upper:
                shifted = shifted.upper() # Convert back to uppercase
                result += shifted
            else:
                result += char # Non-alphabet characters remain unchanged
    return result
# Example usage:
text = "Hello, World! "
shift = 3
encrypted = caesar_cipher(text, shift)
decrypted = caesar_cipher(encrypted, -shift)
print("Original: " , text)
# Original: Hello, World!
print("Encrypted: " , encrypted)
print("Decrypted: ", decrypted) # Decrypted: Hello, World!
C:\Users\vwank\PycharmProjects\Python_Cucumber\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\Python_Cucumber\.venv\Scripts\tryPyProgs.py 
Original:  Hello, World! 
Encrypted:  KelloZorld
Decrypted:  HelloWorld
************************************************************************************************
class Singleton:
    _instance = None  # Use _instance consistently
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
singleton_1 = Singleton()
singleton_2 = Singleton()
print(singleton_1 is singleton_2)  # ✅ Output: True
************************************************************************************************
# public variable
class MyClass1:
    def __init__(self):
        self.public_variable = "This is public."
obj = MyClass1()
print(obj.public_variable)
# Protected variable
class Myclass2:
    def __init__(self):
        self._protected_variable = "This is protected variable"
class subClass(Myclass2):
    def print_protected(self):
        print(self._protected_variable)
obj = subClass()
obj.print_protected()
# Private
class MyClass3:
    def __init__(self):
        self.__private_variable = "This is private variable"
    def get_private_variable(self):
        return self.__private_variable
obj = MyClass3()
print(obj.get_private_variable())
This is public.
This is protected variable
This is private variable
************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************
************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************

************************************************************************************************
