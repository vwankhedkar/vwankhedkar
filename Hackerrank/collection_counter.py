import collections
numShoes = int(input())
shoes = collections.Counter(map(int, input().split()))
numCust = int(input())
income = 0
for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]:
        income += price
        shoes[size] -= 1
print(income)
OUTPUT:
10
1 2 3 4 5 6 7 8 9 10
5
4 77
3 88
5 99
1 55
2 66
385
***************************************************************
from collections import defaultdict
d = defaultdict(list)
list1 = []
n, m = map(int, input().split())
for i in range(0, n):
    d[input()].append(i+1)
for i in range(0, m):
    list1 = list1+[input()]
for i in list1:
    if i in d:
        print(" ".join( map(str,d[i])))
    else:
        print(-1)
OUTPUT:
5 2
a
a
b
a
b
a
b
1 2 4
3 5
*********************************************************
from collections import defaultdict
d = defaultdict(list)
d['python'].append("awesme")
d['something-else'].append("Not relevant")
d['python'].append("language")
for i in d.items():
    print(i)
OUTPUT:
('python', ['awesme', 'language'])
('something-else', ['Not relevant'])
OUTPUT : 11
*********************************************************
from collections import namedtuple
Car = namedtuple('Car','Price Miledge Colour Class')
xyz = Car(Price=1000000, Miledge=30, Colour='Cyan', Class='Y')
print(xyz)
Car(Price=1000000, Miledge=30, Colour='Cyan', Class='Y')
print(xyz.Class)
OUTPUT: Y
*********************************************************
from collections import namedtuple
n, Student = input(), namedtuple('Student', raw_input())
print "%.2f" %( sum([float(stud.MARKS) for stud in [Student(*raw_input().split()) for _ in xrange(n)]]) / n )
OUTPUT:
  
