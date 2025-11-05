# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass
# you need to guess this number
number = 18
try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
OUTPUT :------------------
Enter a number: 10 
Exception occurred: Invalid Age
-----------------------------------------------------
class NegativeAgeError(Exception):
    """Exception raised when the age is negative."""
    def __init__(self, age):
        self.message = f"Age {age} is not valid. Age cannot be negative."
        super().__init__(self.message)
def check_age(age):
    if age < 0:
        raise NegativeAgeError(age)
        print(f"Age {age} is valid.")
try:
    check_age(-5)
except NegativeAgeError as e:
    print(e)
OUTPUT
Age -5 is not valid. Age cannot be negative.
*******************************************************************************
dictionary = {'euler_constant': 0.577, 'golden_ratio': 1.618}
try:
    dct = dictionary['euler_constant']
except KeyError:
    print("This code gives us KeyError")
dct = dictionary['euler_cont']
print(dct)
Traceback (most recent call last):
  File "/home/main.py", line 6, in <module>
    dct = dictionary['euler_cont']
          ~~~~~~~~~~^^^^^^^^^^^^^^
KeyError: 'euler_cont'
*******************************************************************************
num1 = float(input("Enter a number : "))
print("The entered value is : ", num1)
try:
    num2 = float(input("Enter a number : "))
    print("The entered value is : ", num2)
    value = num1/ num2
except ZeroDivisionError:
    print('This function gives a ZeroDivisionError since a number cannot divide') 
except ValueError:
    print('You should provide a number.')
except:
    print('Something went wrong !')
else:
    print('This process is running with value = ',value)
finally:
    print('This process is completed')
Enter a number : 3.33 
The entered value is :  3.33
Enter a number : 5.65
The entered value is :  5.65
This process is running with value =  0.5893805309734513
This process is completed

Enter a number : 7.89
The entered value is :  7.89
Enter a number : 0
The entered value is :  0.0
This function gives a ZeroDivisionError since a number cannot divide
Enter a number : 4
The entered value is :  4.0
Enter a number : 
You should provide a number.
*******************************************************************************
num = int(input("Enter number : "))
print('The entered valie is : ', num)
try:
    if num > 1000 and num % 2 == 0 or num%2 != 0:
        raise Exception ('Do not allow to the even numbers higher than 1000.')
except:
    print('Even or odd numbers higher than 1000 are not allowed!')
else:
    print('This process is running with value = ', num)
finally:
    print('The process is completed.')
Enter number : 1006
The entered valie is :  1006
Even or odd numbers higher than 1000 are not allowed!
The process is completed.
*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************

*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************

*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************

*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************

*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************

*******************************************************************************
*******************************************************************************
*******************************************************************************
*******************************************************************************

*******************************************************************************
*******************************************************************************
*******************************************************************************
