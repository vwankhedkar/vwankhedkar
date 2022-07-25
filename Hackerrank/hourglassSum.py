#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_sum = 0
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            SUM = (arr[i][j] + arr[i][j + 1] + arr[i][j + 2]) + (arr[i + 1][j + 1]) +       (arr[i + 2][j] +
                    arr[i + 2][j + 1] + arr[i + 2][j + 2])
            if(SUM > max_sum):
                max_sum = SUM
            else:
                continue
    return max_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

OUTPUT :
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

19
------------------------------------------------------------------------------
import sys
 
R = 5
C = 5
 
# Function to return the maximum sum
# of a cocktail glass
def findMaxCock(ar):
     
    # If no cocktail glass is possible
    if (R < 3 or C < 3):
        return -1
 
    # Initialize max_sum with the mini
    max_sum = -sys.maxsize - 1
 
    # Here loop runs (R-2)*(C-2) times considering
    # different top left cells of cocktail glasses
    for i in range(R - 2):
        for j in range(C - 2):
             
            # Considering mat[i][j] as the top left
            # cell of the cocktail glass
            sum = ((ar[i][j] + ar[i][j + 2]) +
                   (ar[i + 1][j + 1]) +
                   (ar[i + 2][j] + ar[i + 2][j + 1] +
                    ar[i + 2][j + 2]))
 
            # Update the max_sum
            max_sum = max(max_sum, sum)
 
    return max_sum;
 
# Driver code
if __name__ == '__main__':
    ar = [[0, 3, 0, 6, 0],
          [0, 1, 1, 0, 0],
          [1, 1, 1, 0, 0],
          [0, 0, 2, 0, 1],
          [0, 2, 0, 1, 3]]
 
    print(findMaxCock(ar))
 
