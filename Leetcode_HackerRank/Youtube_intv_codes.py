			Simple codes - multiple ways 
Link - https://www.youtube.com/watch?v=g56e2YowN38&list=PLFV6T8f5WU2FRO_Hu7q9b18yB1P98NSZd&index=1

INTERVIEW QUESTION - Find out common letters between two strings Using Python
def common_ele(str1, str2):
    # s = set()
    # for ch1 in str1:
    #     for ch2 in str2:
    #         if (ch1 == ch2):
    #             s.add(ch1)
    # return s
    # --------------------------------------------#
    # from collections import Counter 
    # c1 = Counter(str1)
    # c2 = Counter(str2)
    # return set(c1.keys() & c2.keys())
    # --------------------------------------------#
    # result =[]
    # for ch in str1:
    #     if ch in str2:
    #         result.append(ch)
    # return set(result)
    # --------------------------------------------#
    from functools import reduce
    return reduce(
        lambda acc, ch : acc | {ch} if ch in str2 else acc, str1, set())
    # --------------------------------------------#
    # for ch1 in str1:
    #     if ch1 in str2:
    #         s.add(ch1)
    # return s    
    # --------------------------------------------#
    # return set(str1) & set(str2)
    # --------------------------------------------#
    # return set([ch for ch in str1 if ch in str2])
    # --------------------------------------------#
    # return set(str1).intersection(set(str2))
    # --------------------------------------------#
    # return set(filter(lambda ch : ch in str2, str1))
    # --------------------------------------------#
if __name__ == '__main__':
    str1 = "NAINA"
    str2 = "REENE"
    print(common_ele(str1, str2))	=> 'N'
*************************************************************************

def reverse_str(str1):
    # return str1[::-1]
    #------------------------------------#
    # return "".join(reversed(str1))
    #------------------------------------#
    # l = len(str1)-1
    # output = ""
    # while (l >= 0):
    #     output = output + str1[l]
    #     l -= 1
    # return output
    #------------------------------------#
    # output = ""
    # for ch in str1:
    #     output = ch + output
    # return output
    #------------------------------------#
    # if len(str1) == 0:
    #     return str1
    # return reverse_str(str1[1:]) + str1[0]
    #------------------------------------#
    # stack = list(str1)
    # output = ""
    # while stack:
    #     output += stack.pop()
    # return output
    #------------------------------------#
    # return "".join([str1[i] for i in range(len(str1)-1, -1, -1)])
    #------------------------------------#
    # from functools import reduce
    # return reduce(lambda x,y:y+x,str1)
    #------------------------------------#
    # l = []
    # for ch in str1:
    #     l.insert(0, ch)
    # return "".join(l)
    #------------------------------------#
    # from collections import deque
    # d = deque(str1)
    # output = ""
    # while d:
    #     output += d.pop()
    # return output
    #------------------------------------#
    b = bytearray(str1, 'utf-8')
    return b[::-1].decode()
    #------------------------------------#
if __name__ == '__main__':
    str1 = "Python programming"
    print(reverse_str(str1))	===>	gnimmargorp nohtyP
*************************************************************************
def topper(students):
    # top_stud = max(students, key=students.get)
    # return top_stud, students[top_stud]
    # --------------------------------------------#
    max_marks = 0
    top = ""
    for name, marks in students.items():
        if marks > max_marks:
            max_marks = marks
            top = name
    return name, max_marks
if __name__ == '__main__':
    students = {
        "Rahul": 450,
        "Priya": 480,
        "Amit": 470,
        "Sneha": 490
        }
    mark, stud = topper(students)
    print("Topper : ", mark )
    print("Marks : ", stud)
Topper :  Sneha
Marks :  490
*************************************************************************
import re
def addDigits(str1):
    # num = ""
    # total = 0
    # for ch in str1:
    #     if ch.isdigit():
    #         num += ch
    #     else:
    #         if num:
    #             total += int(num)
    #             num = ""
    # if num:
    #     total += int(num)
    # return total
    # --------------------------------------------#
    numbers = re.findall(r'\d+', str1)
    total = sum(map(int, numbers))
    return numbers, total
if __name__ == '__main__':
    str1 = "Today is 20th March, 2026."
    print(addDigits(str1))
(['20', '2026'], 2046)
*************************************************************************
INTERVIEW QUESTION - Count the frequency of words appearing in a string Using Python
def freq_words(str1):
    dir = {}
    words = str1.split(" ")
    # for word in words:
    #     dir[word] = dir.get(word, 0)+1
    # return dir
    # --------------------------------------------#
    # for word in words:
    #     if word not in dir.keys():
    #         dir[word] = 0
    #     dir[word] = dir[word] + 1
    # return dir
    # --------------------------------------------#
    # from collections import Counter
    # return (Counter(str1.split()))
    # --------------------------------------------#
    # for word in words:
    #     dir[word] = words.count(word)
    # return dir
    # --------------------------------------------#
    return {word:words.count(word) for word in set(words)}
if __name__ == '__main__':
    str1 = 'some sample words to test the pattern some sample words'
    print(freq_words(str1))
{'the': 1, 'some': 2, 'words': 2, 'pattern': 1, 'sample': 2, 'test': 1, 'to': 1}
*************************************************************************
INTERVIEW QUESTION - Conversion of two list into Dictionary Using Python
def list_to_dict():
    keys = [1, 2, 3]
    values = ["one", "two", "three"]
    # result = dict(zip(keys, values))
    # return result
    # --------------------------------------------#
    return {k: v for k, v in zip(keys, values)}
    
def dict_to_tuple():
    x = {1: 'One', 2: 'Two', 3: 'Three'}
    # for i in x.items():
    #     print(i, end = " ")
    # --------------------------------------------#
    # return tuple(x.items())
    # --------------------------------------------#
    # return list(x.items())   
    # --------------------------------------------#
    return tuple(x.keys()), tuple(x.values())
if __name__ == '__main__':
    print(list_to_dict())
    print(dict_to_tuple())
{1: 'one', 2: 'two', 3: 'three'}
((1, 2, 3), ('One', 'Two', 'Three'))
*************************************************************************
FIND MISSING NUMBER IN AN ARRAY IN PYTHON
def get_missing_sum(lst):
    # n = lst[-1]
    # sum1 = 0
    # total = n*(n+1)//2
    # sum1 = sum(lst)
    # return (total - sum1)
    # ---------------With XOR method-----------------#
    # n = len(lst)
    # xor_lst = lst[0]
    # for index in range(1,n):
    #     xor_lst = xor_lst^lst[index]
    # x2 = 0
    # for index in range(1, n+2):
    #     x2 = x2^index
    # return (xor_lst^x2)
    # --------------------------------------------#
    n = len(lst)+1
    # full_set = set(range(1, n+1))
    # return list(full_set - set(lst))[0]
    # --------------------------------------------#
    # for i in range(1, n+1):
    #     if i not in lst:
    #         return i
    # --------------------------------------------#
    # for i in range(n+1):
    #     if lst[i] != i+1:
    #         return i+1
    # --------------------------------------------#
    for index, value in enumerate(lst, start=1):
        if index != value:
            return index
    return len(lst)+1
if __name__ == '__main__':
    lst = [1, 2, 4, 5, 6, 7]
    print(get_missing_sum(lst))	=====>	3
*************************************************************************
Find Out Pairs with given sum in an array in python of time complexity O(n log n)- FACEBOOK,AMAZON
def two_sums(arr, sum):
    # arr.sort()
    # left = 0
    # right = len(arr)-1
    # while (left < right):
    #     if (arr[left]+arr[right] > sum):
    #         right = right - 1
    #     elif (arr[left]+arr[right] < sum):
    #         left = left + 1
    #     elif (arr[left]+arr[right] == sum):
    #         print("Value of pair are : ",arr[left], "&", arr[right])
    #         right = right - 1
    #         left = left + 1
    # print(left, right)
    # --------------------------------------------#
    # pairs = [(arr[i], arr[j])
    #         for i in range(len(arr))
    #         for j in range(i+1, len(arr))
    #         if arr[i] + arr[j] == sum]
    # print(pairs)
    # --------------------------------------------#
    # d = {}
    # for i, num in enumerate(arr):
    #     diff = sum - num
    #     if diff in d:
    #         print (diff, num)
    #     d[num] = i
    # --------------------------------------------#
    s = set()
    for num in arr:
        diff = sum - num
        if diff in s:
            print(diff, num)
        s.add(num)
if __name__ == '__main__':
    arr = [5, 7, 4, 3, 9, 8, 19, 21, 10]
    sum = 17
    two_sums(arr, sum)
Value of pair are :  7 & 10
Value of pair are :  8 & 9
*************************************************************************
LeetCode #104 Height of Binary Tree(Max Depth) - Python Interview Question(Recursion)
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
def height_tree(A):
    if (A == None):
        return 0
    else:
        ldepth = height_tree(A.left)
        rdepth = height_tree(A.right)
        if (ldepth > rdepth):
            return (1+ldepth)
        else:
            return (1+rdepth)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)
print(height_tree(root))
*************************************************************************
Min Depth of Binary Tree - Python Interview Question #Recursion
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
def min_height_binary(root):
    if (root == None):
        return 0
    else:
        ldepth = min_height_binary(root.left)
        rdepth = min_height_binary(root.right)
        if (ldepth > rdepth):
            return (1+rdepth)
        else:
            return (1+ldepth)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.left.left = Node(7)
root.right.right = Node(6)
print(min_height_binary(root))		==>	2
*************************************************************************
Find minimum difference between two elements of Binary Tree | Data Structures #Python Code
def minimum_diff(arr):
    arr = sorted(arr)
    size = len(arr)
    min_diff = 9999*999
    for i in range(size-1):
        if (arr[i+1] - arr[i] < min_diff):
            min_diff = arr[i+1]-arr[i]
        return min_diff, arr[i+1], arr[i]
arr = [5, 32, 45, 4, 12, 18, 25]
diff, no1, no2 = minimum_diff(arr)
print(f"Minimum difference between array elements {no1} - {no2} = {diff} ")
Minimum difference between array elements 5 - 4 = 1 
*************************************************************************
Maximum Difference of Binary Tree #Data Structures #Python Interview Questions
def maximum_diff(arr):
    arr = sorted(arr)
    size = len(arr)
    max_diff = -9999*999
    for i in range(size-1):
        if (arr[i+1] - arr[i] > max_diff):
            max_diff = arr[i+1]-arr[i]
    return max_diff, arr[i+1], arr[i]
arr = [5, 32, 45, 4, 12, 18, 25]
diff, no1, no2 = maximum_diff(arr)
print(f"Maximum difference between array elements {no1} - {no2} = {diff} ")
Maximum difference between array elements 45 - 32 = 13  
*************************************************************************
Postfix expression using Stack
def eval_expr(arr):
    stack = []
    operator = ["+","-","*","/","%"]
    for item in arr:
        if item not in operator:
            stack.append((item))
        else:
            first = int(stack.pop())
            sec = int(stack.pop())
            if (item == "+"):
                stack.append(sec + first)
            if (item == "-"):
                stack.append(sec - first)
            if (item == "*"):
                stack.append(sec * first)
            if (item == "/"):
                stack.append(sec / first)
            if (item == "%"):
                stack.append(sec % first)
    return stack[-1]
A = ["2", "1", "+", "3", "*"]
print(eval_expr(A))		==>	9
*************************************************************************
Cracking #DS Algo: Trapping Rain Water Problem (#Python)
def rain_trap(arr):
    size = len(arr)
    left = size * [0]
    right = size * [0]
    left[0] = arr[0]
    water = 0
    max_so_far_left = arr[0]
    for index in range(0, size):
        if (max_so_far_left < arr[index]):
            max_so_far_left = arr[index]
            left[index] = max_so_far_left
        else:
            left[index] = max_so_far_left
    max_so_far_right = arr[-1]
    for index in range(size-1, -1, -1):
        if (max_so_far_right < arr[index]):
            max_so_far_right = arr[index]
            right[index] = max_so_far_right
        else:
            right[index] = max_so_far_right
    for index in range(0, size):
        water = water + min(left[index], right[index]) - arr[index]
    return water
    
arr = [1, 0, 2, 0, 1, 0, 3, 1, 0, 2]
print(rain_trap(arr))	===>	9
*************************************************************************
# WAVE ARRAY - DS & ALGO WITH PYTHON CODE -AMAZON,GOOGLE,ADOBE INTERVIEW QUESTION
def wave(arr):
    size = len(arr)
    for index in range(0, size, 2):
        if (index > 0 and arr[index-1]>arr[index]):
            arr[index-1], arr[index] = arr[index], arr[index-1]
        if (index < size-1 and arr[index]<arr[index+1]):
            arr[index], arr[index+1] = arr[index+1], arr[index]
    return arr
arr = [3, 5, 12, 2, 6, 10, 7, 9, 8]
print(wave(arr))
[5, 3, 12, 2, 10, 6, 9, 7, 8]
*************************************************************************
Hotel bookings Possible - DS & ALGO Interview Question With Python Code
def hotel_booking(arrival, depart, K):
    event = [(t, "RED") for t in arrival] + [(t, "BLUE") for t in depart]
    event = sorted(event)
    print(event)
    guest = 0
    for e in event:
        if (e[1] == 'RED'):
            guest = guest + 1
        else:
            guest = guest - 1
        if (guest > K):
            return 0
    return 1
arrival = [1, 3, 5]
depart = [2, 6, 8]
print(hotel_booking(arrival, depart, 1))
[(1, 'RED'), (2, 'BLUE'), (3, 'RED'), (5, 'RED'), (6, 'BLUE'), (8, 'BLUE')]
0
*************************************************************************
Length of Last Word - Algorithm /Code in Python
def len_last_word(arr):
    words = arr.split(' ')
    size = len(words)
    if (size == 1):
        return len(arr)
    last_word = words[-1]
    return last_word
arr = "Netsetos"
print(len_last_word(arr))	===>		8
*************************************************************************
Remove Duplicates from Sorted Array (With Algorithm & Python Code)
def remove_duplicates_space(arr):
    n = len(arr)
    if (n==0 or n==1):
        return arr
    temp = [0] * n
    pivot = 0
    for last_o in range(0, n-1):
        if (arr[last_o] != arr[last_o+1]):
            temp[pivot] = arr[last_o]
            pivot = pivot + 1
    temp[pivot] = arr[n-1]
    return temp[0:pivot+1]
arr = [1,1,2,2,2,3,4,4,4,5,5]
print(remove_duplicates_space(arr))
[1, 2, 3, 4, 5]
*************************************************************************
Maximum Sum SubArray (Kadane's algorithm) With Algorithm & Python Code
def max_sum_subarray(arr):
    size = len(arr)
    curr_sum = 0
    max_so_far = arr[0]
    st=0; end=0; poi=0
    for i in range(0, size):
        curr_sum = curr_sum + arr[i]
        if (max_so_far < curr_sum):
            max_so_far = curr_sum
            st = poi
            en = i
        if (curr_sum < 0):
            curr_sum = 0
            poi = i+1
    print("Maximum sum SubArray is : ", max_so_far)
    print("Start index of windows is : ", st)
    print("End index of window is : ", en)
arr = [4, -3, -2, 2, 3, 1, -2, -3, 6, -6, -4, 2, 1]
max_sum_subarray(arr)
Maximum sum SubArray is :  7
Start index of windows is :  3
End index of window is :  8
*************************************************************************
Maximum Sum SubArray (Kadane's algorithm) With Algorithm & Python Code
def anagram(arr):
    if (arr == None):
        return
    else:
        dict = {}
        for i in range(len(arr)):
            word = ''.join(sorted(arr[i]))
            if (word not in dict):
                dict[word] = [i + 1]
            else:
                dict[word].append(i+1)
    return dict
arr = ["cat", "dog", "god", "tca", "act"]
print(anagram(arr))
{'act': [1, 4, 5], 'dgo': [2, 3]}
*************************************************************************
Maximum Sum SubArray (Kadane's algorithm) With Algorithm & Python Code
def remove_duplicate_num(arr):
    # arr2 = set(arr)
    # return arr2
    # return list(set(arr))
    #----------------------------------#
    # arr2 = []
    # for i in arr:
    #     if i not in arr2:
    #         arr2.append(i)
    # return arr2
    #----------------------------------#
    rem_dups = lambda x: list(set(x))
    return rem_dups(arr) 
arr = [1,4,2,5,2,3,4,1,4,5,2,3]
print(remove_duplicate_num(arr))	====>	[1, 2, 3, 4, 5]
*************************************************************************
def remove_duplicate_str(dct):
    for key, val in dct.items():
        dct[key] = set(val)
    return dct
dict = {
    'Car' : ["Ford", "Toyata", "Ford", "Toyata"],
    'Brand' : ["Mustang", "Ranz", "Mustang", "Ranz"]
}
print(remove_duplicate_str(dict))
{'Car': {'Ford', 'Toyata'}, 'Brand': {'Ranz', 'Mustang'}}
*************************************************************************
Maximum Sum SubArray (Kadane's algorithm) With Algorithm & Python Code
def find_min_max(arr):
    max = arr[0]
    min = arr[0]
    for i in range(len(arr)):
        if (arr[i] > max):
            max = arr[i]
        if (arr[i] < min):
            min = arr[i]
    return min, max
arr = [64, 54, 98, 34, 89, 42, 18]
print(find_min_max(arr))
===>	(18, 98)
*************************************************************************
Find Rotated #String | #Python
def left_rotate_str(name):
    size = len(name)
    temp = name + name
    for i in range(size):
        for j in range(size):
            print(temp[i+j], end = "")
        print()
str = "NETSET"
left_rotate_str(str)
NETSET
ETSETN
TSETNE
SETNET
ETNETS
TNETSE
*************************************************************************
Find Rotated #String | #Python
def check_rotation(str1, str2):
    if (len(str1) != len(str2)):
        return False
    size = len(str1)
    s = str1 + str1
    if (str2 in s):
        print(str1, " is matching with ", str2)
    else:
        print(str1, " is not matching with ", str2)
check_rotation("ANU", "NUR")
ANU  is not matching with  NUR
*************************************************************************
Reverse Words in String #Python
def reverse(str_r):
    str_r = str_r[::-1]
    return str_r
def reverse_word(str_r):
    n = len(str_r)
    if (n == 1):
        return str_r
    str2 = str_r.split(" ")
    size = len(str2)
    rev_all = " "
    for i in range(size):
        rev = reverse(str2[i])
        rev_all=rev_all+rev+" "
    d = reverse(rev_all)
    return d.strip()
    
str_r = "NETSETOS IS EXCELLENT"
print(reverse_word(str_r))
EXCELLENT IS NETSETOS
*************************************************************************
def frst_non_repeat_char(str_r):	# AMAZON CODING INTERVIEW QUESTION - FIRST NON-REPEATING CHARACTER IN A STRING (LeetCode)
    dict = {}
    size = len(str_r)
    for i in range(size):
        key = str_r[i]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key] = dict[key]+1
    counter = 0
    for index in range(len(str_r)):
        if (dict[str_r[index]] == 1):
            return str_r[index], counter
        counter = counter + 1
    
str_r = "NETSETOSNET"
print(frst_non_repeat_char(str_r))
('O', 6)
*************************************************************************
Python Interview Question - Excel column number [ LEETCODE 171 ]
def exceltitle_num(str_r):
    size = len(str_r)
    result = 0
    for i in range(size):
        num = ord(str_r[i]) - ord('A') + 1
        result = result + num*pow(26,size-1)
        size = size - 1
    return result
str_r = "AB"
print(exceltitle_num(str_r))		==>	28
*************************************************************************
Amazon Interview question :- Roman Numerals to Integers (Python)
def romanToInteger(A):
    result = 0
    i = 0
    while (i<len(A)):
        curr = value(A[i])
        if (i+1 < len(A)):
            next = value(A[i+1])
            if (curr >= next):
                result = result + curr
                i = i + 1
            else:
                result = result + (next - curr)
                i = i + 2
        else:
            result = result + curr
            i = i + 1
    return result
def value(A):
    if (A == 'I'):
        return 1
    if (A == 'V'):
        return 5
    if (A == 'X'):
        return 10
    if (A == 'L'):
        return 50
    if (A == 'C'):
        return 100
    if (A == 'D'):
        return 500
    if (A == 'M'):
        return 1000
print(romanToInteger("CXLLIVI"))	==>	195
*************************************************************************
Amazon Interview question :- Roman Numerals to Integers (Python)
def common_ele(list1, list2):
    common = []
    count = 0
    for i in list1:
        for j in list2:
            if (i == j):
                common.append(i)
                count = count + 1
    print(common)
    print("Common elements in both list is : ", count)
def common_ele_dict(list1, list2):
    dict1 = {}
    for element in list2:
        dict[element] = 1
    for i in list1:
        if dict.get[i] != None:
            print(i)
            count = count + 1
    print("Number of elements common are : ", count)
l1 = [2, 4, 6, 8, 10, 12, 14]
l2 = [3, 6, 9, 12, 15, 18]
common_ele(l1, l2)
[6, 12]
Common elements in both list is :  2
*************************************************************************
Interview Question : Multiply Strings [LeetCode] Python Code
def multiply_str(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    str1 = list(map(int, reversed(str1)))
    str2 = list(map(int, reversed(str2)))
    res = [0 for i in range(len1+len2)]
    for j in range(len2):
        for i in range(len1):
            res[i+j] = res[i+j] + str1[i] * str2[j]
            res[i+j+1] = res[i+j+1] + res[i+j] // 10
            res[i+j] = res[i+j] % 10
    i = len(res) -1
    while (res[i] == 0 and i > 0):
        i = i - 1
    return "".join(map(str, res[:i+1][::-1]))
print(multiply_str("78", "57"))		==>		4446
*************************************************************************
Sort Colors | LeetCode -75 | Python
def sort_colors(arr):
    size = len(arr)
    red = 0
    blue = 0
    for i in range(size):
        if (arr[i] == 1):
            red = red + 1
        elif (arr[i] == 2):
            blue = blue + 1
    return [1]*red + [2]*blue+[3]*(size-red-blue)
arr = [1,2,3,1,3,2,1,2,3,1]
print(sort_colors(arr))
[1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
*************************************************************************
Check if a number is prime or not | Python Tutorial
def prime_num(num):
    if (num > 1):
        for i in range(2, num):
            if (num % i == 0):
                return False
        return True
is_prime = prime_num(17)
if (is_prime):
    print("Is a prime number")
else:
    print("Is not a prime number")
*************************************************************************
Sieve of Eratosthenes | Fastest way for Prime Number | Facebook
from math import sqrt
def sieve_prime(num):
    prime_arr = [1]*(num+1)
    prime_arr[0] = 0
    prime_arr[1] = 0
    for i in range(2, int(sqrt(num))):
        if (prime_arr[i] == 1):
            j = 2
            while (i * j < num + 1):
                prime_arr[j*i]=0
                j = j + 1
    return prime_arr
print(sieve_prime(15))
[0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
*************************************************************************
Interview Question : Find Substring of String | Python Code
def substring(str1, n):
    for i in range(n):
        for j in range(i+1, n+1):
            print(str1[i:j])
str1 = "VAISH"
n = len(str1)
substring(str1, n)
V
VA
VAI
VAIS
VAISH
A
AI
AIS
AISH
I
IS
ISH
S
SH
H
*************************************************************************
Interview Question : Subsequence of String | Python Code
def subsequence(str1):
    if (len(str1) == 0):
        return [' ']
    small = subsequence(str1[1:len(str1)])
    result = [" "]* (2 * len(small))
    k = 0
    for i in range(len(small)):
        result[k] = small[i]
        k = k + 1
    for i in range(len(small)):
        result[k] = str1[0] + small[i]
        k = k + 1
    return result
print(subsequence("net"))
[' ', 't ', 'e ', 'et ', 'n ', 'nt ', 'ne ', 'net ']
*************************************************************************
list1 = [4,7,9,2]
list1.reverse()
print(list1)

print(list1[::-1])

print(list(reversed(list1)))

list2 = []
for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
print(list2)
[2, 9, 7, 4]
[4, 7, 9, 2]
[4, 7, 9, 2]
[4, 7, 9, 2]
*************************************************************************
sentence = "Nancy is 90 years old. she wants 120 tofees with 47.9 weight"
num = []
for word in sentence.split():
    if word.isdigit():
        num.append(word)
print(num)

import re
digit = re.findall(r"\d*\.?\d+",sentence)
print(digit)
['90', '120']
['90', '120', '47.9']
*************************************************************************
import timeit
print(timeit.timeit('x=[1,2,3,4,5,6,7,8,9,10,11,12]', number=1000000))
print(timeit.timeit('x=[1,2,3,4,5,6,7,8,9,10,11,12]', number=1000000))
0.07556600699899718
0.07476797899289522
*************************************************************************
def fib_gen():
    a = 0
    b = 1
    while True:
        c = a
        a = b
        b = c + a
        yield c
f =fib_gen()
for i in range(10):
    print(next(f), end = "  ")
0  1  1  2  3  5  8  13  21  34  	
*************************************************************************
import re
def isValidEmail(email):
    regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.match(regex, email) is not None
email = "nesetos@gmail.com"
if isValidEmail(email):
    print("Valid Email...")
else:
    print("Invalid Email...")
Valid Email...
*************************************************************************
def pascal_triangle(M):
    a=[[] for i in range(M)]
    for i in range(M):
        for j in range(i+1):
            if (j < i):
                if (j == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i-1][j]+a[i-1][j-1])
            elif (j == i):
                a[i].append(1)
    return a
print(pascal_triangle(5))
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
*************************************************************************
