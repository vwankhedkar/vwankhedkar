             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
import math
def rowSumOddNumbers(n):
    return math.pow(n, 3)

if __name__ == '__main__':
    print (rowSumOddNumbers(3))
    
  ********************************************
  
 import math
def rowSumOddNumbers(n):
    return n * n * n

if __name__ == '__main__':
    print (rowSumOddNumbers(3))
  
*******************************************
def row_sum_odd_numbers(n):
    num_pos = find_numb_count(n)
    sum = 0
    for i in range(n):
        sum += (num_pos * 2) - 1
        num_pos -= 1
    
    return sum

# Return the position of the last number in the triangle row
def find_numb_count(n):
    if n == 1:
        return 1
    return find_numb_count(n-1) + n
