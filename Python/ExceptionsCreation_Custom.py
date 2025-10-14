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
