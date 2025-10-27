def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
num = int(input("Enter number : "))
print("Factorial : ", fact(num))
Enter number : 6
Factorial :  720
***************************************************************************
def fibbo(n):
    if n <= 1:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)
num = int(input("Enter number : "))
print("Fibbonacci sequence : ", end="")
for i in range(num):
    print(fibbo(i), end=" ")
------------------------------------------
def fibbo_series(n):
    a, b = 0, 1
    for _ in range(n+1):
        print(a, end=" ")
        a, b = b, a+b
terms = int(input("Enter number of terms : "))
print("Fibbocci Series : ")
fibbo_series(terms)
Enter number : 7
Fibbonacci sequence : 1 1 2 3 5 8 13
***************************************************************************
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**5)+1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter number : "))
if is_prime(num):
    print("Prime")
else:
    print("Not prime")
Enter number : 17
Not prime
***************************************************************************
with open("output.txt","w") as file:
    file.write("Hello, this is sample text!")
with open("output.txt","r") as file:
    data = file.read()
    print("Data from file : ", data)  ==>  Data from file :  Hello, this is sample text!
***************************************************************************
def is_palindrome(s):
    return s == s[::-1]
string = input("Enter string : ")
if is_palindrome(string):
    print("Palindrome")
else:
    print("Not a Palindrome")
Enter string : malayalam
Palindrome
***************************************************************************
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array : ", arr)
Sorted array :  [11, 12, 22, 25, 34, 64, 90]
***************************************************************************
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
year = int(input("Enter year : "))
if is_leap_year(year):
    print("Is leap year")
else:
    print("Not a leap year")
Enter year : 2025
Not a leap year
***************************************************************************
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count=0
    for char in s:
        if char in vowels:
            count += 1
    return count
string = input("Enter string : ")
print("Number of vowels : ", count_vowels(string))
Enter string : Hello world
Number of vowels :  3
***************************************************************************
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
rect = Rectangle(length, width)
print("Area of the rectangle:", rect.area())
Enter length of the rectangle: 20
Enter width of the rectangle: 30
Area of the rectangle: 600.0
***************************************************************************
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
string1 = input("Enter 1st string : ")
string2 = input("Enter 2nd string : ")
if is_anagram(string1, string2):
    print("Anagram")
else:
    print("Not Anagram")
Enter 1st string : listen
Enter 2nd string : silent
Anagram
***************************************************************************
def binary_search(arr, x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print(f"Element not found ! ")    ==>    Element found at index 3
***************************************************************************
def is_armstrong(n):
    order = len(str(n))
    temp = n 
    sum = 0
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10
    return n == sum
n = int(input("Enter a number : "))
if is_armstrong(n):
    print("Armstrong number")
else:
    print("Not a Armstrong number")
Enter a number : 153
Armstrong number
***************************************************************************
n = 5
for i in range(n):
    print("*"*(i+1))    # print(""*(n-i-1)+"* "*(2*i+1))
*
**
***
****
*****
n = 5
for i in range(n):
    print(" "*(n-i-1),"* "*(i+1))
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
n = 5
for i in range(n):
    print(""*(n-i-1)+"*"*(i+1))
for i in range(n-1, 0, -1):
    print(""*(n-i)+"*"*i)
*
**
***
****
*****
****
***
**
*
***************************************************************************
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [4, 2, 1, 7, 5]
x = 7
result = linear_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element found !")    ==>    Element found at index 3
***************************************************************************
def generate_primes(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
start_range = int(input("Enter the starting range: "))
end_range = int(input("Enter the ending range: "))
print("Prime numbers:", generate_primes(start_range, end_range))
Enter the starting range: 1
Enter the ending range: 20
Prime numbers: [2, 3, 5, 7, 11, 13, 17, 19]
***************************************************************************
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
year = int(input("Enter year : "))
if is_leap_year(year):
    print("Leap year")
else:
    print("Not a Leap year")
Enter year : 2028
Leap year
***************************************************************************
def is_perfect_number(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n
number = int(input("Enter number : "))
if is_perfect_number(number):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
***************************************************************************
import math
def is_perfect_square(n):
    root = math.sqrt(n)
    return root * root == n
number = int(input("Enter number : "))
if is_perfect_square(number):
    print("Perfect Square")
else:
    print("Not a Perfect Square")
***************************************************************************
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Popped Items : ", stack.pop())
print("Stack is empty : ", stack.is_empty())
Popped Items :  3
Stack is empty :  False
***************************************************************************
def is_perfect_cube(n):
    root = round(n**(1/3))
    return root**3 == n
number = int(input("Enter number : "))
if is_perfect_cube(number):
    print("Perfect Cube...")
else:
    print("Not a Perfect Cube...")
Enter number : 153
Not a Perfect Cube...
***************************************************************************
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("dequeued items : ", queue.dequeue())
print("Queue is empty : ", queue.is_empty())
dequeued items :  1
Queue is empty :  False
***************************************************************************
from itertools import chain, combinations
def power_set(s):
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
input_set = [1,2,3]
print("Power Set : ", power_set(input_set))
Power Set :  [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
***************************************************************************
import string
def is_pangram(s):
    dct = {}
    alphabet = set(string.ascii_lowercase)  # {'a', 'b', 'c', ..., 'z'}
    for ch in s.lower():
        if ch in alphabet:
            dct[ch] = dct.get(ch, 0) + 1
    for key in sorted(dct.keys()):
        print(f"{key}: {dct[key]}", end = " ")
    return set(s.lower()) >= alphabet
input_string = input("Enter String : ")
if is_pangram(input_string):
    print("==> This is Pangram")
else:
    print("Not Pangram")
Enter String : The quick brown fox jumps over the lazy dog
a: 1 b: 1 c: 1 d: 1 e: 3 f: 1 g: 1 h: 2 i: 1 j: 1 k: 1 l: 1 m: 1 n: 1 o: 4 p: 1 q: 1 r: 2 s: 1 t: 2 u: 2 v: 1 w: 1 x: 1 y: 1 z: 1 ==> This is Pangram
***************************************************************************
def generate_pascal_triangle(n):
    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]+[prev_row[j]+prev_row[j+1] for j in range(i-1)]+[1]
        triangle.append(curr_row)
    return triangle
rows = 5
print("Pascal's Triangle : ")
for row in generate_pascal_triangle(rows):
    print(row)
Pascal's Triangle : 
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
***************************************************************************
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
***************************************************************************
from sklearn.linear_model import LinearRegression
import numpy as np
X = np.array([[1,1], [1,2],[2,2],[2,3]])
y = np.dot(X, np.array([1,2])) + 3
reg = LinearRegression().fit(X, y)
print("Coef: ", reg.coef_)
print("Intercept : ", reg.intercept_)
Coef:  [1. 2.]
Intercept :  3.0000000000000018
***************************************************************************
num = int(input("Enter an Integer : "))
num_digits = len(str(abs(num)))
print("Number of digits: ", num_digits)   
Enter an Integer : 5234
Number of digits:  4
***************************************************************************
import random
import string
def generate_password(length):
    characters = string.ascii_letters+string.digits+string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = 12
print("Generate Password : ",generate_password(password_length))
Generate Password :  [HtRq|byMX}=
***************************************************************************
import socket
def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False
ip_address = input("Enter an IP address")
if is_valid_ip(ip_address):
    print("Valid IP address")
else:
    print("Invalid IP address")
Enter an IP address 121.34.56.190
Invalid IP address
***************************************************************************
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        if self.items:
            return self.items.pop()
        return None
    def is_empty(self):
        return self.items == []
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Dqueued item : ", queue.dequeue())
print("Queue is empty : ", queue.is_empty())
Dqueued item :  1
Queue is empty :  False
***************************************************************************
def power_set_iterative(s):
    power_set = [[]]
    for elem in s:
        for sub_set in power_set[:]:
            power_set.append(sub_set+[elem])
    return power_set
input_set = [1, 2, 3]
print("Power set (iterative) : ", power_set_iterative(input_set)) 
Power set (iterative) :  [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
***************************************************************************
def binary_search_recursive(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid-1, x)
        else:
            return binary_search_recursive(arr, mid+1, high, x)
    else:
        return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search_recursive(arr, 0, len(arr)-1, x)
if result != -1:
    print(f"Element found at index : {result}")
else:
    print("Element not found")
Element found at index : 3
***************************************************************************
def sum_of_digit(n):
    return sum(int(digit) for digit in str(n))
num = int(input("Enter number : "))
print("Sum of digits : ", sum_of_digit(num))
print("Binary : ", bin(num))
print("HexaDecimal : ", hex(num))
print("Octal : ", oct(num))
Enter number : 1234
Sum of digits :  10
Binary :  0b10011010010
HexaDecimal :  0x4d2
Octal :  0o2322
***************************************************************************
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        mid_idx = i
        for j in range(i+1,n):
            if arr[j] < arr[mid_idx]:
                mid_idx = j
            arr[i], arr[mid_idx] = arr[mid_idx], arr[i]
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array : ", arr)
Sorted array :  [11, 22, 12, 25, 64]
***************************************************************************
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j>=0 and key <= arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key    
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted array : ", arr)
Sorted array :  [5, 6, 11, 12, 13]
***************************************************************************
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sorted array : ", arr)
Sorted array :  [11, 12, 22, 25, 34, 64, 90]
***************************************************************************
def compute_lcm(x, y):
    lcm = (x * y) // compute_gcd(x,y)
    return lcm
def compute_gcd(x, y):
    while y:
        x, y = y, x%y
    return x
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM:", compute_lcm(num1, num2))
print("GCD:", compute_gcd(num1, num2))
Enter second number: 11
LCM: 264
GCD: 1
***************************************************************************
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = quick_sort(arr)
print("sorted_arr : ", sorted_arr)
sorted_arr :  [5, 6, 7, 11, 12, 13]
***************************************************************************
def generate_fibonacci(n):
    fibbonacci_sequence = [0, 1]
    for i in range(2, n):
        next_num = fibbonacci_sequence[-1] + fibbonacci_sequence[-2]
        fibbonacci_sequence.append(next_num)
    return fibbonacci_sequence
terms = 10
print("Fibbonacci sequence : ", generate_fibonacci(terms))
Fibbonacci sequence :  [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
***************************************************************************
base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = 1
for _ in range(exponent):
    result *= base
print("Result:", result)
Enter the base: 10
Enter the exponent: 3
Result: 1000
***************************************************************************
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
arr = [4, 2, 1, 7, 5]
x = 7
result = linear_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
Element found at index 3
***************************************************************************
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_hand = arr[:mid]
        right_hand = arr[mid:]
        merge_sort(left_hand)
        merge_sort(right_hand)
        i = j = k = 0
        while i < len(left_hand) and j < len(right_hand):
            if left_hand[i] < right_hand[j]:
                arr[k] = left_hand[i]
                i += 1
            else:
                arr[k] = right_hand[j]
                j += 1
            k += 1
        while i < len(left_hand):
            arr[k] = left_hand[i]
            i += 1
            k += 1
        while j < len(right_hand):
            arr[k] = right_hand[j]
            j += 1
            k += 1
arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:", arr)
Sorted array: [5, 6, 7, 11, 12, 13]
***************************************************************************
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
Element found at index 3
***************************************************************************
import re
def is_valid_email(email):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", email))
input_mail = input("Enter an email address : ")
if is_valid_email(input_mail):
    print("Valid email address")
else:
    print("InValid email address")
Enter an email address : abc@gmail.com
Valid email address
***************************************************************************
import random
random_list = random.sample(range(1, 100), 5)
print("Random list : ", random_list)
Random list :  [76, 22, 35, 69, 47]
***************************************************************************
import math
numbers = [24, 36, 48, 60, 72]
gcd = math.gcd(*numbers)
print("GCD of the numbers : ", gcd)
GCD of the numbers :  12
***************************************************************************
import statistics
data = [1, 2, 3, 4, 5]
std_dev = statistics.stdev(data)
print("Standard deviation : ", std_dev)
Standard deviation :  1.5811388300841898
***************************************************************************
import random
import string
def generate_password(length, include_digits=True, include_special_chars=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password_length = 12
print("Generate password : ", generate_password(password_length))
Generate password :  ^#J6=r+^9m2V
***************************************************************************
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number : "))
if is_prime(num):
    print("Prime number")
else:
    print("Not a Prime number")
Enter a number : 11
Prime number
***************************************************************************
list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}, {'name': 'Bob', 'age': 35}]
sorted_list = sorted(list_of_dicts, key = lambda x:x['age'])
print("Sorted list of dictionaries:", sorted_list)
Sorted list of dictionaries: [{'name': 'Jane', 'age': 25}, {'name': 'John', 'age': 30}, {'name': 'Bob', 'age': 35}]
***************************************************************************
import numpy as np
rows = 3
cols = 3
random_matrix = np.random.rand(rows, cols)
print("Random matrix : ")
print(random_matrix)
Random matrix : 
[[0.15616339 0.85962029 0.97933921]
 [0.90341399 0.15640342 0.70590951]
 [0.59602864 0.70466881 0.19473243]]
***************************************************************************
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def reset(self):
        self.count = 0
counter = Counter()
counter.increment()
counter.increment()
print("Count:", counter.count)
counter.decrement()
print("Count:", counter.count)
counter.reset()
print("Count:", counter.count)
Count: 2
Count: 1
Count: 0
***************************************************************************
import re
def is_valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
input_url = input("Enter a URL: ")
if is_valid_url(input_url):
    print("Valid URL")
else:
    print("Invalid URL")
Enter a URL: https://abc.com
Valid URL
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************

