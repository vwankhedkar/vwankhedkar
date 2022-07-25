#!/bin/python3
import math
import os
import random
import re
import sys

def reverseArray(a):
    # Write your code here
    return a[::-1]

if __name__ == '__main__':
    fptr = open('output.txt', 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')
    fptr.close()

 OUTPUT :
 4
1 2 3 4
