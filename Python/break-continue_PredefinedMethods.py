x = 0
y = 0
while x <= 10:
    print(x)
    x = x + 1
    print("Parent while")
    while y <= 5:
        print(y)
        break
        print("inner loop")
print("out of while loop")
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
0
Parent while
0
1
Parent while
0
2
Parent while
0
3
Parent while
0
4
Parent while
0
5
Parent while
0
6
Parent while
0
7
Parent while
0
8
Parent while
0
9
Parent while
0
10
Parent while
0
out of while loop
*****************************************************************************
x = 0
y = 0
while x <= 10:
    print(x)
    x = x + 1
    print("Parent while")
    while y < 5:
        print(y)
        y = y+1
        continue
        print("inner loop")
print("out of while loop")
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
0
Parent while
0
1
2
3
4
1
Parent while
2
Parent while
3
Parent while
4
Parent while
5
Parent while
6
Parent while
7
Parent while
8
Parent while
9
Parent while
10
Parent while
out of while loop
*****************************************************************************
x = 0
y = 0
while x <= 10:
    print(x)
    x = x + 1
    if x == 5:
        break
else:
    print("out of while loop")
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
0
1
2
3
4
*********************************************************************
import numpy as np
rows = 3
cols = 3
random_matrix = np.random.rand(rows, cols)
print("Random Matrix : ",random_matrix)
Random Matrix :  [[0.1908944  0.05831195 0.04394315]
 [0.28796139 0.65179879 0.74098046]
 [0.86922028 0.4207848  0.64469013]]
**********************************************************
import random
import string
def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password
password_length=12
print("Generated password:", generate_password(password_length))
Generated password: h6fRPl6;1VTo
**************************************************************
import statistics
data = [1,2,3,4,5]
std_dev = statistics.stdev(data)
print("Standard deviation : ", std_dev)
Standard deviation :  1.5811388300841898
***************************************************************
import math
numbers = [24, 36, 48, 60, 72]
gcd = math.gcd(*numbers)
print("GCD of the numbers:", gcd)    ---->    GCD of the numbers: 12
*************************************************************************
import random
random_list = random.sample(range(1, 100), 5)
print("Random list:", random_list)
SET-10
*************************************************************************
list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25},
{'name': 'Bob', 'age': 35}]
sorted_list = sorted(list_of_dicts, key=lambda x:x['age'])
print("Sorted list of dictionaries:", sorted_list)
OUTPUT - Sorted list of dictionaries: [{'name': 'Jane', 'age': 25}, {'name': 'John', 'age': 30}, {'name': 'Bob', 'age': 35}]           
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
   
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
   
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
   
