import cmath
import math
eq = input()
pa = cmath.phase(complex(eq))
r = abs(complex(eq))
print("{0}\n{1}".format(r,pa))

OUTPUT:
  1+2j
  
2.23606797749979
1.1071487177940904
*********************************************

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print([0, 1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321][i])
OUTPUT: 5
1
121
12321
1234321
123454321
***************************************************
a, b = int(input()), int(input())
print("{d[0]}\n{d[1]}\n{d}".format(d=divmod(a, b)))
OUTPUT:
177
10
17
7
(17, 7)
**********************************************************
inp = (int(input()), int(input()), int(input()))
print("{0} \n {1}".format(pow(inp[0], inp[1]), pow(*inp)))
OUTPUT:
3
4
5

81 
 1
*************************************************************
a,b,c,d = (int(input()) for _ in range(4))
print (pow(a,b)+pow(c,d))
OUTPUT:
9
29
7
27
4710194409608608369201743232
*************************************************************
for i in range(1, int(input())):
    print(int((pow(10,i) -1) / (10-1))*i)
5
1
22
333
4444
