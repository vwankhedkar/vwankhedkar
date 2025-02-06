def recFactorial(x):
   if ( x<= 1 ):
      return 1
   else:
      return x * recFactorial(x-1)

print(recFactorial(5))

--------------------------------------

def tailFactorial(x, totalSoFar=1):
   if ( x == 0 ):
      return totalSoFar
   else:
      return tailFactorial(x-1, totalSoFar * x)

print(tailFactorial(5))
--------------------------------------

OUTPUT : 120

memo = {}
def fact(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * fact(n-1)
    return memo[n]
print(fact(5))
print(memo)
OUTPUT
120
{1: 1, 2: 2, 3: 6, 4: 24, 5: 120}
*********************************************
Nonrecursive
def compute_factorial(num):
    factorial = 1
    if num < 0:
        print("Factorial does not exists for negative numbers")
    elif num == 0:
        print("Factorial of 0 = 1")
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        print("The factorial of ",num, "is: ", factorial)
compute_factorial(int(input("Enter a number: ")))
Enter a number: 4
The factorial of  4 is:  24
******************************************************
memo = {}
def factorial_memory(n):
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = n * factorial_memory(n-1)
    return memo[n]
factorial_memory(int(input("Enter a number: ")))
print(memo)
OUTPUT
Enter a number: 6
{1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}
