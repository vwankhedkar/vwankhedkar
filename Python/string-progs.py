x = "I am an indian, I stay in Bangalore india"
y = 869456439
p = "       ';';';909I am an indian, I stay in Bangalore    999   "
print(len(x))
print(str(y))
# print(y.find("64"))   AttributeError: 'int' object has no attribute 'find'
z = str(y)
print(z.find("64"))
a = x.upper()
b = x.lower()
print(a)
print(b)
print(x.count("india"))
print(x.count("india",15,41))
print(a.isupper())
print(b.islower())
print(x.split())
print(p.strip())
print(p.strip(';9 \''))
print(p.lstrip(';9 \''))
print(p.rstrip(';9 \''))
print(x.replace("india","Bangalorian"))
print(x.replace("india","Bangalorian",2))
print(x.find("Bangalore"))
print(x.index("Bangalore"))

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
41
869456439
5
I AM AN INDIAN, I STAY IN BANGALORE INDIA
i am an indian, i stay in bangalore india
2
1
True
True
['I', 'am', 'an', 'indian,', 'I', 'stay', 'in', 'Bangalore', 'india']
';';';909I am an indian, I stay in Bangalore    999
09I am an indian, I stay in Bangalore
09I am an indian, I stay in Bangalore    999   
       ';';';909I am an indian, I stay in Bangalore
I am an Bangaloriann, I stay in Bangalore Bangalorian
I am an Bangaloriann, I stay in Bangalore Bangalorian
26
26
************************************************************************************************************************************
s = "Welcome to software, testing, academy"
print(s[0])
print(s[-1])
print(s[0:9])
print(s[6:10])
print(s[3:9:1])
print(s[3:20:2])
print(s[5:])
print(s[:8])
print(s[:-1])
print(s[:])
print(s[::-1])
print(s.index(','))
print(s[0:s.index(',')])

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
W
y
Welcome t
e to
come t
cm osfwr,
me to software, testing, academy
Welcome 
Welcome to software, testing, academ
Welcome to software, testing, academy
ymedaca ,gnitset ,erawtfos ot emocleW
19
Welcome to software
********************************************************************************************************************************
x = "Python Class"
y = "RCV Academy"
print("Welcome to"+x+" from "+y)
print("Welcome to %s from %s" %("Java Class",y))
print("Welcome to {0} from {1}".format(x,y))
print("Welcome to {classname} from {academyname}".format(classname="Perl",academyname=y))

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
Welcome toPython Class from RCV Academy
Welcome to Java Class from RCV Academy
Welcome to Python Class from RCV Academy
Welcome to Perl from RCV Academy
********************************************************************************************************************
Digits to word conversion:
--------------------------
words_upto_19 = ['','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT',
                 'NINE','TEN','ELEVEN','TWELVE','THIRTEEN','FOURTEEN','FIFTEEN',
                 'SIXTEEN','SEVENTEEN','EIGHTEEN','NINETEEN']
words_upto_tens = ['','','TWENTY','THIRTY','FOURTY','FIFTY','SIXTY',
                  'SEVENTY','EIGHTY','NINETY']

n = int(input("Enter a digit from 0-99: "))
output=''
if n==0:
    output='ZERO'
elif n<=19:
    output=words_upto_19[n]
elif n<=99:
    output = words_upto_tens[n//10]+" "+words_upto_19[n%10]
else:
    print("Please enter value from 0-99 only...")
print(output)
*********************************************************
s = input("Enter String: ")
s1 = input("Enter substring: ")
if s1 in s:
    print("Substring is part of string")
else:
    print("Substring is not part of string")
OUTPUT :-
--------- 
PS D:\Selenium\Scripts> & C:/Programs/Python/Python39/python.exe d:/Selenium/Scripts/Test_Framework/try.py
Enter String: vaishali wankhedkar
Enter substring: rd
Substring is not part of string

s1 = input("Enter String1: ")
s2 = input("Enter string2: ")
if s1 == s2:
    print("Strings are equal")
elif s1 < s2:
    print("Strings are inequal")
OUTPUT :-
--------- 
Enter String: abc
Enter substring: abc
Strings are equal

str = "BBBBBBBBB"
print(str.count("B"))
print(str.count("BB"))
print(str.count("BBB"))
OUTPUT :-
--------- 
9
4
3

str = 'ABCABCABCA'
i = str.find('ABC')
print(i)
i = str.find('ABC',3,9)
print(i)
i = str.find('ABC',6,9)
print(i)
i = str.find('ABC',9,10)
print(i)
str = 'ABCABCABCA'
subs = 'ABC'
i = str.find(subs)
if i == -1:
    print('Specified substring not found')
while i != -1:
    print('{} present at index {}'.format(subs, i))
    i = str.find(subs,i+len(subs),len(str))
OUTPUT:
------
0
3
6
-1
ABC present at index 0
ABC present at index 3
ABC present at index 6

s = "I am Vaishali Mangulal Wankhedkar"
str = ""
rev = s.replace(' ', '')
print(rev + " is replaced as" + rev[::-1])
OUTPUT:
-------
IamVaishaliMangulalWankhedkar is replaced asrakdehknaWlalugnaMilahsiaVmaI
*********************************************************

s = "I am Vaishali Mangulal Wankhedkar"
words = s.split()
print('_'.join(words))
OUTPUT:
--------
I_am_Vaishali_Mangulal_Wankhedkar

s = "I am Vaishali Mangulal Wankhedkar"
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.swapcase())
OUTPUT:
--------
i am vaishali mangulal wankhedkar
I AM VAISHALI MANGULAL WANKHEDKAR
I Am Vaishali Mangulal Wankhedkar
I am vaishali mangulal wankhedkar
i AM vAISHALI mANGULAL wANKHEDKAR

s = "I am Vaishali Mangulal Wankhedkar"
print(s.startswith("I"))
print(s.startswith("I am"))
print(s.endswith('kar'))
print(s.endswith('Wankhedkar'))
OUTPUT:
-------
True
True
True
True

s = "I am 123 Vaishali Mangulal Wankhedkar"
print(s.isspace())
print('Iam123'.isalnum())
print('IAM'.isalnum())
print(s.islower())
print(s.isupper())
print(s.istitle())
OUTPUT:
-------
False
True
True
False
False
False

s = "I am Vaishali Mangulal Wankhedkar"
r = reversed(s)
output=''.join(r)
print(output)
-------------------------------------
s = "I am Vaishali Mangulal Wankhedkar"
output = ''
i = len(s) - 1
while (i>=0):
    output = output+s[i]
    i = i - 1
print(output)
--------------------------------------
rakdehknaW lalugnaM ilahsiaV ma I
s = "I am Vaishali Mangulal Wankhedkar"
l = s.split()
l1 = l[::-1]
output = ' '.join(l1)
print(output)
OUTPUT:
------
Wankhedkar Mangulal Vaishali am I

s = "I am Vaishali Mangulal Wankhedkar"
l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
output = ' '.join(l1)
print(output)
------------------------------
I ma ilahsiaV lalugnaM rakdehknaW

s = "One Two Three Four Five Six"
l = s.split()
l1 = []
i = 0
while i < len(l):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i += 1
print(l1)
output = ' '.join(l1)
print(output)
-------------------------
['One', 'owT', 'Three', 'ruoF', 'Five', 'xiS']
One owT Three ruoF Five xiS

s1 = "One Two Three Four Five Six"
s = s1.replace(' ', '')
i = 0
print("Characters at Odd location")
while (i < len(s)):
    print(s[i], end = ' ')
    i += 2
i = 1
print("\nCharacters at Even location")
while (i < len(s)):
    print(s[i], end = ' ')
    i += 2
--------------------------------------
s1 = "One Two Three Four Five Six"
s = s1.replace(' ', '')
print("Characters at Odd location", s[::2])
print("\nCharacters at Even location", s[::1])

OUTPUT:
-------
Characters at Odd location
O e w T r e o r i e i 
Characters at Even location
n T o h e F u F v S x


s1 = "One"
s2 = "Two"
i,j = 0, 0
output = ''
while i<len(s1) and j<len(s2):
    output = output + s1[i] + s2[j]
    i += 1
    j += 1
print(output)
------------------------------------
s1 = "One"
s2 = "Two"
i,j = 0, 0
output = ''
while i<len(s1) and j<len(s2):
    if (i<len(s1)):
        output = output + s1[i]
    i += 1
    if (j<len(s2)):
        output = output + s2[j]
    j += 1
print(output)
----------------------------------
OUTPUT:   OTnweo

s = "B4AA1D7C3E1A"
alphabets = []
digits = []
for ch in s:
    if ch.isalpha():
        alphabets.append(ch)
    elif ch.isnumeric():
        digits.append(ch)
output = ''.join(sorted(alphabets)+sorted(digits))
print(output)

s = "B4AA1D7C3E1A"
alphabets = ''
digits = ''
output = ''
for ch in s:
    if ch.isalpha():
        alphabets+=ch
    else:
        digits += ch
for ch in sorted(alphabets):
    output = output + ch
for ch in sorted(digits):
    output = output + ch
print(output)

OUTPUT:   AAABCDE11347

s = "D3A4B2C3"
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
    else:
        d = int(ch)
        output = output + x*d
print(output)
print(''.join(sorted(output)))
OUTPUT :
----------
DDDAAAABBCCC
AAAABBCCCDDD

s = "AABBBCCCCDZZZZ"
output = ''
prev = s[0]
c = 1
i = 1
while i<len(s):
    if s[i] == prev:
        c = c + 1
    else:
        output=output+str(c)+prev
        prev = s[i]
        c = 1
    if i == len(s)-1:
        output = output+str(c)+prev
    i = i + 1
print(output)
OUTPUT :
----------
2A3B4C1D4Z

s = "a4k3b2"
output = ''
for ch in s:
    if ch.isalpha():
        x = ch
        output = output + ch
    else:
        d = int(ch)
        newc = chr(ord(x) + d)
        output = output + newc
print(output)
OUTPUT : aeknbd

s = "AAAAAAFFFFFFFFFFFEWEEEEEEEEXXXXXX"
output = ''
for ch in s:
    if ch not in output:
        output = output + ch
print(output)

s = "AAAAAAFFFFFFFFFFFEWEEEEEEEEXXXXXX"
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
output = ''.join(l)
print(output)
-------
OUTPUT:AFEWX

s = "AAAAAAFFFFFFFFFFFEWEEEEEEEEXXXXXX"
l = []
for ch in s:
    if ch not in l:
        l.append(ch)
for ch in sorted(l):
    print("{} Character occured {} times".format(ch,s.count(ch)))
output = ''.join(l)
-------
A Character occured 6 times
E Character occured 9 times
F Character occured 11 times
W Character occured 1 times
X Character occured 6 times

*************************************************************************
Dictionary string operations:
s = "AAAAAAFFFFFFFFFFFEWEEEEEEEEXXXXXX"
d = {}
for ch in s:
    d[ch] = d.get(ch,1) + 1
print(d)
for k, v in d.items():
    print("{} occured {} times".format(k, v))

OUTPUT: {'A': 7, 'F': 12, 'E': 10, 'W': 2, 'X': 7}
A occured 7 times
F occured 12 times
E occured 10 times
W occured 2 times
X occured 7 times

d = {100:'A', 200:'B', 300:'D'}
print(d.get(100))
print(d.get(700,'Guest'))
OUTPUT :
A
Guest

d1 = {100:'A', 200:'B', 300:'D'}
d2 = {'500':'E', '700':'F'}
d3 = {**d1, **d2}
print(d3)


s = "AAAAAAFFFFFFFFFFFEWEEEEEEEEXXXXXX"
d = {}
for ch in s:
    d[ch] = d.get(ch,0)+1
output=''
for k,v in sorted(d.items()):
    output = output + str(v) + k #### OR  output = output + k + str(v)
print(output)
OUTPUT : 6A9E11F1W6X

s = "AAAAAAFFFFFFFFFFFEWEEEEEEEEXXXXXX"
d = {}
vow = {'a','e','i','o','u','A','E','I','O','U'}
for ch in s:
    if ch in vow:
        d[ch] = d.get(ch,0)+1
print(d)
for k, v in d.items():

OUTPUT : {'A': 6, 'E': 9}
A occured 6 times
E occured 9 times

word = input("Enter statement to search the vowels: ")
s = set(word)
v = {'a','e','i','o','u'}
result = s.intersection(v)
print('The different vowels present in {} are {}'.format(word,sorted(result)))
OUTPUT :
Enter statement to search the vowels: i am an indian girl
The different vowels present in i am an indian girl are ['a', 'i']

word = "bshdgsahjlAKS,A njshiQOL;Q,asan"
vowels = ['a','e','i','o','u']
result = [ch for ch in vowels if ch in word]
print(result)
print("Number of unique vowels", len(result))
OUTPUT :
-------
['a', 'i']
Number of unique vowels 2

s1 = input("Enter s1:") #lazy
s2 = input("Enter s2:") #zaly
if sorted(s1) == sorted(s2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")
	
OUTPUT:
Enter s1:lazy
Enter s2:zaly
Strings are anagram

s1 = input("Enter s1:") #lazy
if (s1 == s1[::-1]):
    print("Strings are Palindrome")
else:
    print("Strings are not Palindrome")
OUTPUT :
Enter s1:abc
Strings are not Palindrome

Merge strings:
s1 = 'abcdefg'
s2 = 'xyz'
s3 = '12345'
i = j = k = 0
while i<len(s1) or j<len(s2) or k<len(s3):
    output = ''
    if i<len(s1):
        output = output + s1[i]
        i = i + 1
    if j<len(s2):
        output = output + s2[j]
        j = j + 1
    if k<len(s3):
        output = output + s3[k]
        k = k + 1
    print(output)
OUTPUT :
ax1
by2
cz3
d4
e5
f
g
************************************************************************
no_word=0
no_char=0
no_line=0
no_space = 0
with open("input.txt",'r') as file:
    for line in file:
        no_line += 1
        no_char = len(line)
        words = line.split()
        no_word += len(words)
        no_space += len(words)-1
    print("File analysis summary:")
    print("Character count:", no_char)
    print("Word count:", no_word)
    print("Space count:", no_space)
    print("Line count:", no_line)
File analysis summary:
Character count: 22
Word count: 33
Space count: 25
Line count: 8
*****************************************************************
def merge_the_tools(string, k):
    n = len(string)
    for i in range(0,n,k):
        word = ''
        for j in range(k):
            if string[i+j] not in word:
                word += string[i+j]
        print(word)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
AABCAAADA
3
AB
CA
AD
*****************************************************************
str = input("Enter string : ")
result = ""
new_word=True
for ch in str:
    if new_word and ch.isalpha():
        result += ch.upper()
        new_word = False
    else:
        result += ch
    if ch == " ":
        new_word = True
print(result)
Enter string : python automation architect
Python Automation Architect
*****************************************************************
*****************************************************************
*****************************************************************
*****************************************************************
*****************************************************************
*****************************************************************
