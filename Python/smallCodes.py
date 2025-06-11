import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
10
<class 'decimal.Decimal'>
12345
<class 'decimal.Decimal'>
************************************************************************************************************
str = "Python Programming"
print(str[::-1])

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
vowel_dict = {}
const_count = 0
const = []
for ch in str:
    if (ch in vowels or ch == ' '):
        vowel_dict[ch] = vowel_dict.get(ch, 0) + 1
        vowel_count += 1
    else:
        const_count += 1
        const.append(ch)

print(vowel_dict, "total vowels :=> ", vowel_count, "total constants :=> ", const_count, const)
gnimmargorP nohtyP
{'o': 2, ' ': 1, 'a': 1, 'i': 1} total vowels :=>  5 total constants :=>  13 ['P', 'y', 't', 'h', 'n', 'P', 'r', 'g', 'r', 'm', 'm', 'n', 'g']
************************************************************************************************************
fib = [0,1]
n = 5
for i in range(n):
    fib.append(fib[-1] + fib[-2])
print(', '.join(str(e) for e in fib))  ===>  0, 1, 1, 2, 3, 5, 8

import re
name = 'Python is 1'
digitCount = re.sub("[^0-9]", "",name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall(r"[ \s]", name)
print(digitCount, len(digitCount))
print(letterCount, len(letterCount))
print(len(spaceCount))
C:\Trainings\Pytest-Bdd-Udemy\TestFrameworkApp-main\.venv\Scripts\python.exe C:\Users\vwank\PycharmProjects\PytestFramework\Python_Codes\try.py 
1 1
Pythonis 8
2
************************************************************************************************************
def count_sp_char(string):
    sp_char = "!@#$%^&*()?|{}[]:;~`"
    char = []
    count = 0
    for i in string:
        if i in sp_char:
            count += 1
            char.append(i)
    return count, char
text = "Hello! How are you? #specialchars! 123"
result = count_sp_char(text)
print("Special Chars are: ", result)    ===>    Special Chars are:  (4, ['!', '?', '#', '!'])
************************************************************************************************************


************************************************************************************************************
