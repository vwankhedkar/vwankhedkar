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

