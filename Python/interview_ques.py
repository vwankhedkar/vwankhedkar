Your function should print the pair numbers from the array that add up to the integer parameter.
def find_sum_pair(arr, sum_val):
    arr = list(set(arr))
    ans = []
    for i in range(len(arr)):
        for j in range(1,len(arr)-1):
            if arr[i] + arr[j] == sum_val:
                ans.append((arr[i], arr[j]))
    return ans
arr = [1, 0, 3, 5, 2, 3, 6]
print(find_sum_pair(arr, 5))
[(0, 5), (2, 3), (3, 2)]
****************************************************************************************
Find the second largest number in the set of array 
lst = [12, 34, 67, 89, 54, 32, 12, 89, 89, 76, 67]
max_val = 0
sec_max = 0
for no in lst:
    if no > max_val:
        sec_max = max_val
        max_val = no
    elif no > sec_max and no != max_val:
        sec_max = no
print(f"max : {max_val}, Second max : {sec_max}")
max : 89, Second max : 76
******************************************************************************************
s1 = input("Enter s1:") #lazy
s2 = input("Enter s2:") #zaly
if sorted(s1) == sorted(s2):
    print("Strings are anagram")
else:
    print("Strings are not anagram")
OUTPUT:
Enter s1:lazy
Enter s2:zaly
Strings are anagram
***********************************************************************************************
def ispalin(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
        return True
s = "malayalam"
ans = ispalin(s)
if (ans):
    print("String is Panildrome")
else:
    print("String is not Panildrome")

def ispalin(str):
    return str == str[::-1]

PS C:\Users\VWankhedkar\PycharmProjects\Robot\TestCase> python.exe .\Hello.py
String is Panildrome

*************************************************************

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s).lower()
        left = 0
        right = len(s) - 1

        while (left < right):
            if (s[left] != s[right]):
                return False
            left += 1
            right -= 1
        return True

string = "A man, a plan, a canal: Panama"
b = Solution()
print(b.isPalindrome(string))
**********************************************************
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern = r'[^A-Za-z0-9]+'
        s = re.sub(pattern, '', s).lower()
        rev = ""
        for i in range(len(s)):
            rev += s[i]
            i -= 1
        return rev == s

string = "A man, a plan, a canal: Panama"
b = Solution()
print(b.isPalindrome(string))
