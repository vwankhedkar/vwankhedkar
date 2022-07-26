def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    count = 0
    sum = 0
    for word in words:
        count = 0
        for letter in word:
            if is_vowel(letter):
                count += 1
            else:
                continue
        if count % 2 == 0:
            sum += 2
        else:
            sum += 1 
    return sum


n = int(input())
words = input().split()
print(score_words(words))

OUTPUT:
3
programming is awesome
4
