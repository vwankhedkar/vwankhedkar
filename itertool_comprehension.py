import itertools
if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 3
print([ [i, j, k] for i, j, k in itertools.product(range(x+1), range(y+1), range(z+1)) if i+j+k != n ])

OUTPUT : [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 2]]
--------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = []
    l1 = []
    for c1 in range(0, x+1):
        for c2 in range(0, y+1):
            for c3 in range(0, z+1):
                if  c1+c2+c3 != n:
                    l.append([str(c1)+ " " +str(c2)+ " " +str(c3)]) 
    print(l)
OUTPUT:
1
1
2
3
[['0 0 0'], ['0 0 1'], ['0 0 2'], ['0 1 0'], ['0 1 1'], ['1 0 0'], ['1 0 1'], ['1 1 0'], ['1 1 2']]
------------------------------------------------------------------------------------------------------
s = 'abc'
l = []
for c1 in range(0, 3):
    for c2 in range(0, 3):
        for c3 in range(0, 3):
            l.append(s[c1]+s[c2]+s[c3])
            # print(s[c1]+s[c2]+s[c3])
print(l)
OUTPUT:
['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 
'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']
-------------------------------------------------------------------------------------------------------


