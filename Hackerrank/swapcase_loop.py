def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':

**********************************
class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):
    stream.__init__()
    for _ in range(n):
        print(stream.get_next())


queries = int(input())
for _ in range(queries):
    stream_name, n = input().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

OUTPUT:
  3
odd 2
even 3
odd 5
 ******************************************
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
 ************************************************
#!/bin/python3

import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n = int(input().strip())
    if (n % 2 == 0):
        if (n >= 2) and (n <= 5):
            print("Not Weird")
        elif (n > 6) and (n <= 20):
            print("Weird")
        elif (n > 20):
            print("Not Weird")
    else:
        print("Weird")
*************************************************
