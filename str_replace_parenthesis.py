import re
def duplicate_encode(word):
    str_dir = {}
    for ch in word:
        if ch in str_dir:
            str_dir[ch] += 1
        elif ch not in str_dir:
            str_dir[ch] = 1
    return replace(word, str_dir)

def replace(word, str_dir):
    for ch in word:
        if str_dir[ch] > 1:
            word = word.replace(ch, ")")
        elif str_dir[ch] == 1:
            word = word.replace(ch, "(")
    return word

if __name__ == '__main__':
    streams = ["Success", "din", "recede", "(( @"]
    
    for elements in streams:
        print(duplicate_encode(elements.lower()))
