string = "abracadabra"
l = list(string)
l[5] = 'k'
string = ''.join(l)
print(string)

string = string[:5]+'k'+string[6:]
print(string)
OUTPUT:
abrackdabra
abrackdabra
**********************************************
def mutate_string(string, position, character):
    return string[:position]+character+string[position+1:]
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
----------------------------------------
line, info = [input() for _ in range(2)]
idx, rbl = info.split(" ")
idx = int(idx)
print(line[:idx]+rbl+line[(idx+1):])

OUTPUT:
abracadabra
5 k
abrackdabra
**********************************************
def split_and_join(line):
    return '-'.join(line.split(' '))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
-----------------
def split_and_join(line):
    x=line.split(" ") 
    x='-'.join(x)    
    return x
OUTPUT:
I am an indian
I-am-an-indian
**********************************************
def count_substring(string, sub_string):
    counter, sum = 0, 0
    for _ in range(0, len(string)):
        if matcher(string[counter:(len(sub_string)+counter)], sub_string):
            sum = sum + 1
        counter = counter + 1
    return sum
def matcher(sliced_str, sub_string):
    return sliced_str == sub_string
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
OUTPUT:
ABCDCDC
CDC
2
**********************************************
if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))
    print(any(c.isalpha() for c in s))
    print(any(c.isdigit() for c in s))
    print(any(c.islower() for c in s))
    print(any(c.isupper() for c in s))
OUTPUT:
qA2
True
True
True
True
True
************************************************
