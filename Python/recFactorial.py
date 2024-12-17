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
