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
Convert from word to digit 

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
*****************************************************************************

*****************************************************************************

*****************************************************************************
