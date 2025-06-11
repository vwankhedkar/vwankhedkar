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

*****************************************************************************

*****************************************************************************

*****************************************************************************
