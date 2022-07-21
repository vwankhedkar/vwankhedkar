l = {x:x*x for x in range(1,6)}
print(l)

l = [x*x for x in range(1,6)]
print(l)

strng = "I am vaishali wankhedkar"
wrd = [ch for ch in strng if ch != ' ']
print(wrd)

l = [x for x in range(1,10) if x%2 == 0]
print(l)

l1 = [10, 20, 30, 40, 50]
l2 = [40, 50, 60, 70, 80]
l = [x for x in l1 if x not in l2 ]
ll = [x for x in l1 if x in l2]
print(l)
print(ll)

word = ['Vaishali', 'Sushila', 'Mangulal', 'Wankhedkar']
l = [ch[0] for ch in word] 
print(l)

OUTPUT:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

[1, 4, 9, 16, 25]

['I', 'a', 'm', 'v', 'a', 'i', 's', 'h', 'a', 'l', 'i', 'w', 'a', 'n', 'k', 'h', 'e', 'd', 'k', 'a', 'r']
[2, 4, 6, 8]

[10, 20, 30]
[40, 50]

['V', 'S', 'M', 'W']


-----------------------------------------------------------------------------------------------------------------------------------
s = "the quick brown fox jumps over the lazy dog"
words = s.split()
l = [[word.upper(), len(word)] for word in words]
print(l)


-----------------------------------------------------------------------------------------------------------------------------------
l = [ch for ch in s if ch not in ' ']
print(sorted(set(l)))

OUTPUT : [['THE', 3], ['QUICK', 5], ['BROWN', 5], ['FOX', 3], ['JUMPS', 5], ['OVER', 4], ['THE', 3], ['LAZY', 4], ['DOG', 3]]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
-----------------------------------------------------------------------------------------------------------------------------------
vowels = ['a', 'e', 'i', 'o', 'u']
word = "python programming"
l = [ch for ch in vowels if ch in word]
print(l)

OUTPUT: ['a', 'i', 'o']
