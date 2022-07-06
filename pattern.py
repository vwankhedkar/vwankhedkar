Pattern programmes :
------------------
n = int(input("Enter value of n: "))
for i in range(n):
    print('*', end=' ')
	
n = int(input("Enter value of n: "))
for i in range(n):
    print('*' * n)
OUTPUT :
------	
Enter value of n: 3
***
***
***
n = int(input("Enter value of n: "))
for i in range(n):
    print((str(i+1)+' ')*n)
OUTPUT :
------	
Enter value of n: 3
1 1 1 
2 2 2
3 3 3

n = int(input("Enter number of rows: "))
for i in range(n):
    print((chr(65+i)+' ')*n)
OUTPUT :
------	
Enter number of rows: 3
A A A 
B B B
C C C

n = int(input("Enter number of rows: "))
for i in range(n):
    for j in range(i+1):
        print('*', end=' ')
    print()
OUTPUT :
------
Enter number of rows: 3
*
* *
* * *

n = int(input("Enter number of rows: "))
for i in range(n):
    print('* '*(n-i))
OUTPUT :
------
Enter number of rows: 3
* * * 
* *
*

n = 5
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
OUTPUT :
------
    * 
   * *
  * * *
 * * * *
* * * * *

n = int(input('Enter number of rows: '))
for i in range(n):
   print(' '*i + '* '*(n-i))
   
Enter number of rows: 3
* * * 
 * *
  *
  
n = int(input('Enter number of rows: '))
for i in range(n):
    print(' '*(n-i-1)+('* ')*(i+1))
for i in range(n):
    print(' '*(i+1) + '* '*(n-i-1))
------------------------------------
n = int(input('Ener number of rows: '))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n-1):
    print(' '*(i+1) + '* '*(n-i-1))

  * 
 * *
* * *
 * *
  *
  
n = int(input('Enter number of rows: '))
for i in range(n):
   print('* '*(i+1))
for i in range(n-1):
    print('* '*(n-i-1))
	
* 
* *
* * *
* *
*  
