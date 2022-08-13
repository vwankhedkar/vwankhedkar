from itertools import product

print(list(product([1, 2, 3], repeat=2)))
print(list(product([1, 2, 3], [3, 4])))
A = [[1,2,3],[3,4,5]]
print(list(product(*A)))

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))

OUTPUT:
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
[(1, 3), (1, 4), (2, 3), (2, 4), (3, 3), (3, 4)]
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]
[(1, 3, 7), (1, 3, 8), (1, 4, 7), (1, 4, 8), (1, 5, 7), (1, 5, 8), (2, 3, 7), (2, 3, 8), (2, 4, 7), (2, 4, 8), (2, 5, 7), (2, 5, 8), (3, 3, 7), (3, 3, 8), (3, 4, 7), (3, 4, 8), (3, 5, 7), (3, 5, 8)]

A = [1, 2]
B = [3, 4]

AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]
*****************************************************************************
from itertools import product
A = map(int,input().split())
B = map(int,input().split())
# A.sort()
# B.sort()
ans = [A,B]
AXB = list(product(*ans))
for i in AXB:
    print(i)
	
1 2
3 4
(1, 3)
(1, 4)
(2, 3)
(2, 4)
***********************************************************
from itertools import permutations
print(permutations(['1','2','3']))
print(list(permutations(['1','2','3'])))
print(list(permutations(['1','2','3'],2)))
print(list(permutations('abc',3)))

<itertools.permutations object at 0x0000019FDF5FEDB0>
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
**********************************************************************
from itertools import permutations
s1 = []
string=input().split()
for i in string[0]:
    s1.append(i)
p1 = sorted(list(permutations(s1, int(string[1]))))
for i in p1:
    print("".join(i))
	
HACK 2
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH

**********************************************************************************************
from itertools import combinations
print(list(combinations('12345',2)))
A = [1,1,3,3,3]
print(list(combinations(A,4)))

[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

from itertools import combinations
word_comb, number_comb = input().split()
word_comb = sorted(word_comb)
number_comb = int(number_comb)
for i in range(1, number_comb +1):
    list_comb = list(combinations(word_comb, i))
    for j in list_comb:
        print("".join(j))

HACK 2
A
C
H
K
AC
AH
AK
CH
CK
HK

from itertools import combinations_with_replacement
from itertools import combinations 
print(list(combinations_with_replacement('12345',2)))
A = [1,1,3,3,3]
print(list(combinations(A,2)))

[('1', '1'), ('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '2'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '3'), ('3', '4'), ('3', '5'), ('4', '4'), ('4', '5'), ('5', '5')]
[(1, 1), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (1, 3), (3, 3), (3, 3), (3, 3)]

from itertools import combinations_with_replacement
string,n = input().split()
list1 = list(combinations_with_replacement(string,int(n)))
a = []
list2 = []
for i in range(len(list1)):
    list2.append(list(list1[i]))
list3 = []
for i in range(len(list2)):
    list2[i].sort()
for i in range(len(list2)):
    a.append(''.join(map(str,list2[i])))
a.sort()
for i in range(len(a)):
    print(a[i])
   
HACK 2
AA
AC
AH
AK
CC
CH
CK
HH
HK
KK

from __future__ import print_function
from itertools import groupby
string = [(len(list(gr)),int(k)) for k, gr in groupby(input())]
print(*string)

11222311
(2, 1) (3, 2) (1, 3) (2, 1)

import itertools
n = int(input())
k = input().split()
l = int(input())
count = 0
itcomb = list(itertools.combinations(k,l))
lilen = float(len(itcomb))
for i in itcomb:
    if 'a' in i:
        count += 1
print(float(count)/lilen)

4
a a c d
2
0.8333333333333334

####Failing
(K,M)=map(int, input().split())
X = []
def Cal2list(list0,list1):
    newset=set()
    for i in range(len(list0)) :
        for j in range(len(list1)):
            newset.add((list0[i]+list1[j]) % M)
    return list(newset)
def mergelist(input_list) :
    while(len(input_list)>1) :
        input_list[1] = Cal2list(input_list[0],input_list[1])
        del input_list[0]

X=list(map(lambda x: (int(x)**2)%M,  (input().split())[1:]) for i in range(K))

mergelist(X)
print(max(X[0]))
