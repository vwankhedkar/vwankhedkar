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
