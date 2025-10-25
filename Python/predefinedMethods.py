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
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************
***************************************************************************

