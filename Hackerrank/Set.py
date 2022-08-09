def average(array):
    height = set(array)
    avg = sum(height) / len(height)
    return avg
if __name__=='__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
OUTPUT:
10
161 182 161 154 176 170 167 171 170 174
169.375
*************************************************************************
https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
n, m = input().split()
sc_ar = input().split()
A = set(input().split())
B = set(input().split())
print(sum([(i in A) - (i in B) for i in sc_ar]))
OUTPUT:
3 2
1 5 3
3 1
5 7
1
*************************************************************************
M = input().split()
ms = set(map(int, input().split(" ")))
N = input().split()
ns = set(map(int, input().split()))
for _ in sorted(ms.union(ns) - ms.intersection(ns)):
    print(_)
OUTPUT:
4
2 4 5 9
4
2 4 11 12

stdout)
5
9
11
12
*************************************************************************
n = int(input())
s = set()
for i in range(n):
    s.add(input())
print(len(s))
OUTPUT:
7
UK
China
USA
France
New Zealand
UK
France

5
*************************************************************************
n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    x = list(input().split())
    eval('s.{0}({1})'.format(*x+['']))
print(sum(s))
OUTPUT:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5

4
*************************************************************************
z1 = input()
n = set(input().split())
z2 = input()
b = set(input().split())
print(len(b&n))
OUTPUT:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

5
*************************************************************************
a, b = [set(input().split()) for _ in range(4)][1::2]
print(len(a) - len(a&b))
Output:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

4
*************************************************************************
a = input()
b = set(map(int, input().split()))
a = input()
d = set(map(int, input().split()))
print(len((b|d)- (b&d)))
Output:
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

8
*************************************************************************
m = int(input())
A = set(map(int, input().split(" ")))
n = int(input())
for i in range(n):
    cmd, args = input().split(" ")
    B = set(map(int, input().split(" ")))
    eval('A.'+cmd+'(B)')
print(sum(A))
Output:
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
4
intersection_update 10
2 3 5 6 8 9 1 4 7 11
update 2
55 66
symmetric_difference_update 5
22 7 35 62 58
difference_update 7
11 22 35 55 58 62 66

38
*************************************************************************
d = input()
a = input().split()
s1 = set()
s2 = set()
for i in a:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3 = s1.difference(s2)
print(list(s3)[0])
Output:
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 

8
*************************************************************************
for i in range(int(input())):
    a = int(input())
    A = set(input().split())
    b = int(input())
    B = set(input().split())
    subset = A.intersection(B)
    if len(subset) == len(A):
        print(True)
    else:
        print(False)
OUTPUT:
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2

True

False

False
*************************************************************************
A = set(map(int, input().split()))
N = int(input())
set_list = []
for i in range(N):
    x = set(map(int, input().split()))
    set_list.append(x)

result = True
for i in set_list:
    if not A.issuperset(i):
        result = False
print(result)
Output:
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12

False
