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
*************************************************************
import keyword
keywordlist = keyword.kwlist
print(keywordlist)
print(keyword.iskeyword("try"))

OUTPUT
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
True
****************************************************************************
x = "This \'is\' a string"
y = "This is string in \'single\' quotes"
z= """
This is 
multiline comment
"""
c = '''
This is also multiline comment
'''
print("is" in c)
print(x)
print(y[5])
print(z)
print(c)
OUTPUt-
True
This 'is' a string
i
This is 
multiline comment
This is also multiline comment
***********************************************************************************
for i in range(1, 4):
    for j in range(1, 4):
        print(f'({i}, {j})', end=' ')
    print()
(2, 1) (2, 2) (2, 3) 
(3, 1) (3, 2) (3, 3)  
***********************************************************************************
lst = [[1,3,5],[22,4,6],[9,7,5]]
for sublst in lst:
    for num in sublst:
        if num % 2 == 0:
            print("First even num in list : ", num)
            break
First even num in list :  22
***********************************************************************************
class Solution:
    def isPowerOfTwo(n):
        count = 0
        if n == 0:
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
            count += 1
        return count, True

if(Solution.isPowerOfTwo(31)):
    print('Yes')
else:
    print('No')
if(Solution.isPowerOfTwo(64)):
    print('Yes')
else:
    print('No')
    
OUTPUT :
No
Yes
-------------------------------------------------
import math
def Log2(x):
    return math.log10(x)/math.log10(2)

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

if(isPowerOfTwo(31)):
    print("Yes");
else:
    print("No");
 
if(isPowerOfTwo(64)):
    print("Yes");
else:
    print("No");
----------------------------------------------------------
def isPowerOfTwo(x):
    return (x and (not (x & (x-1))))

if(isPowerOfTwo(31)):
    print("Yes");
else:
    print("No");
 
if(isPowerOfTwo(64)):
    print("Yes");
else:
    print("No");
 --------------------------------------------------------------
OUTPUT:
  No
  Yes
 

***********************************************************************************
***********************************************************************************
***********************************************************************************
***********************************************************************************
***********************************************************************************
***********************************************************************************
