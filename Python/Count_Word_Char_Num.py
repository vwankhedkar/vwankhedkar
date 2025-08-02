def str_to_paren(str):
    str_dir = {}
    for ch in str:
        if ch in str_dir:
            str_dir[ch] += 1
        else:
            str_dir[ch] = 1
    return str_dir

if __name__ == '__main__':
    str = "ababdede"
    print(str_to_paren(str))

char count 
--------
st ="happyprogrampppming"
ch = "p"
dir = {}

for ele in st:
    if ele not in dir:
        dir[ele] = 1
    else:
        dir[ele] += 1

for k, v in dir.items():
    # print("Character : ", k , "Appears: ", v, "times")
    if (ch == k):
        print("Character : ", k , "Appears: ", v, "times")
        
vowels count -->

string ="absdauoi"
char, vow = 0, 0 

for ele in string:
    if ele in ['a','e','i','o','u']:
        vow += 1
    else:
        char += 1

print("Character : ", char , "vowels: ", vow)
*****************************************************************************
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
*****************************************************************************
lst = [1,2,1,3,3,2,1]
dct = {}
for num in lst:
    dct[num] = dct.get(num,0)+1
print(dct)
{1: 3, 2: 2, 3: 2}
***********************************************************************
str = "Vaishali"
str_dct = {}
for ch in str:
    str_dct[ch] = str_dct.get(ch,0)+1
print(f"All Char count is : {str_dct}")
for k, v in str_dct.items():
    if v == 1:
        print(f"first unique character is -> {k} : {v}")
        break
All Char count is : {'V': 1, 'a': 2, 'i': 2, 's': 1, 'h': 1, 'l': 1}
first unique character is -> V : 1
***********************************************************************
str = "Vaishali"
str_dct = {}
for ch in str:
    str_dct[ch] = str_dct.get(ch,0)+1
for k, v in str_dct.items():
    print(f"Unique character {k} appeared {v} times")
Unique character V appeared 1 times
Unique character a appeared 2 times
Unique character i appeared 2 times
Unique character s appeared 1 times
Unique character h appeared 1 times
Unique character l appeared 1 times
***********************************************************************
word = "Kundan Kumar Pandey Kundan Kumar"
words = word.split(" ")
wrd_cnt = {}
for str in words:
    wrd_cnt[str] = wrd_cnt.get(str,0)+1
print("Words count are : ", wrd_cnt)
Words count are :  {'Kundan': 2, 'Kumar': 2, 'Pandey': 1}
***********************************************************************
***********************************************************************
***********************************************************************

*****************************************************************************

*****************************************************************************

*****************************************************************************
