n = 5
for i in range(n):
    print(""*(n-i-1)+"*"*(2*i+1))
*
***
*****
*******
*********
-----------------------------------------------------------------------------
n = 5
for i in range(n):
    print(""*(n-i-1)+"*"*(i+1))
for i in range(n-1,0,-1):
    print(""*(n-i)+"*"*i)
*
**
***
****
*****
****
***
**
*
-----------------------------------------------------------------------------
n = 7
for i in range(1,n):
    for j in range(1,i):
        print("*", end="")
    print()
*
**
***
****
*****
-----------------------------------------------------------------------------
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
******
*****
****
***
**
*
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
---------------------------------------------------------------------------------------------

---------------------------------------------------------------------------------------------
    
    
    
    
    
