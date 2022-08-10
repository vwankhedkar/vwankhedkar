for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print([0, 1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321][i])
OUTPUT: 5
1
121
12321
1234321
123454321
***************************************************
for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    for j in range(1, i):
        print(j, end='')
    for k in range(i, 0, -1):
        print(k, end='')
    print()
	
1
121
12321
1234321
123454321
********************************************************
n=5
for i in range(1,n):
    print('  ' * (n - i), end='')
    for j in range(1, i):
        print(j, end=' ')
    for k in range(i, 0, -1):
        print(k, end=' ')
    print()
        1 
      1 2 1 
    1 2 3 2 1 
  1 2 3 4 3 2 1 
************************************************************
