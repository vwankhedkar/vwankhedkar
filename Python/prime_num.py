n = int(input("Enter input: "))
is_prime=True
if (n<1):
    print("It's not prime number")
for i in range(2,n):
    if (n%i == 0):
        is_prime = False
        break
if is_prime == True:
    print("It's prime number")
else:
    print("It's not prime number")
    
OUTPUT:
------
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
Enter input: 5
It's prime number
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
Enter input: 6
************************************************************************************************************
n = int(input("Enter Input: "))
n1 = 2
while (n1 <= n):
    is_prime = True
    for i in range(2,n1//2+1):
        if n1%i==0:
            is_prime = False
            break
    if is_prime==True:
        print(n1, end =' ')
    n1 = n1 + 1
    
 Enter Input: 5
 2 3 5 
************************************************************************************************************
def is_prime(num):
    # check is number is less than 2
    if num<2:
        return False
    # check for factors from 2 to the square root of the number
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    # if no factors are found number is prime
    return True
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} Number is prime")
else:
    print(f"{num} Number is not prime")

OUTPUT - Enter a number: 5
5 Number is prime
