*************************************************************************
			*** Leetcode *****  https://leetcode.com/progress/?page=1&status=&sortBy=frontendId-asc
*************************************************************************
class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            steps += 1
        return steps
		
Input: num = 14
Output: 6
Explanation: 
Step 1) 14 is even; divide by 2 and obtain 7. 
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3. 
Step 4) 3 is odd; subtract 1 and obtain 2. 
Step 5) 2 is even; divide by 2 and obtain 1. 
Step 6) 1 is odd; subtract 1 and obtain 0.
*************************************************************************
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        values = []
        while head:
            values.append(head.val)
            head = head.next
        return values == values[::-1]
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
s = Solution()
print(s.isPalindrome(head))		==>	True
*************************************************************************
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        StringBuilder values = new StringBuilder();
        ListNode temp = head;
        while (temp != null) {
            values.append(temp.val);
            temp = temp.next;
        }
        String original = values.toString();
        String reversed = new StringBuilder(original).reverse().toString();
        return original.equals(reversed);
    }
}	====>		true
*************************************************************************
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return i, j
s = Solution()
nums = [2,7,11,15]
target = 9
num1, num2 = s.twoSum(nums, target)
print(f"{nums[num1]} + {nums[num2]} = {target} at position [{num1} and {num2}]")
OUTPUT:
2 + 7 = 9 at position [0 and 1]
*************************************************************************
Brute - force solution : Update two-sum-brute-force.py
Brute - force solution : Update two-sum-brute-force.py
---------------------
def find_sum_twonum(nums, target):    
    for p1 in range(len(nums)):
        num_to_find = target - nums[p1]
        for p2 in range(p1+1, len(nums)):
            if (num_to_find == nums[p2]):
                return p1, p2, nums[p1], nums[p2] 
nums = [1,3,7,9,2]
target = 11
loc_P1, loc_p2, n1, n2 = find_sum_twonum(nums, target)
print("Sum of numbers {} {} found at locations nums[{}] nums[{}]".format(n1, n2, loc_P1, loc_p2))

OUTPUT : Sum of numbers 9 2 found at locations nums[3] nums[4]
*************************************************************************
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = []
        longest = ""
        for ch in strg:
            if ch not in st:
                st.append(ch)
            else:
                if len(st) > len(longest):
                    longest = "".join(st)
                while ch in st:
                    st.pop(0)
                st.append(ch)
        if len(st) > len(longest):
            longest = "".join(ch)
        return longest
b = Solution()
strg = "pwwkeopdfvw"
lng_str = b.lengthOfLongestSubstring(strg)
print(f"Longest substring : {lng_str} with lenth is : {len(lng_str)}")
Longest substring : wkeopdfv with lenth is : 8
---------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        last_idx = {}
        max_len = 0
        start_idx = 0
        for i in range(0, len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]]+1)
            max_len = max(max_len, i-start_idx+1)
            last_idx[s[i]] = i
        print(start_idx)
        print(last_idx)
        return max_len                
b = Solution()
strg = "pwwkeopdfvw"
print(b.lengthOfLongestSubstring(strg))
---------------------------------------------------
class Solution:
    def lengthOfLongestSubstring(self, s):
        strlen = len(s)
        seenChar = {}
        substr = ""
        longest = 0
        finalList = []
        if (strlen <= 0):
            return strlen
        for L in range(strlen):
            if len(substr) > 0:
                finalList.append(substr)
            currLongest = 0
            substr = ""
            seenChar = {}
            for R in range(L, strlen):
                currChar = s[R]
                if currChar not in seenChar:
                    seenChar[currChar] = 1
                    substr += currChar
                    currLongest += 1
                    longest = max(currLongest, longest)
            else:
                break
        return longest
b = Solution()
strg = "pwwkehw"
print(b.lengthOfLongestSubstring(strg))	====>		5
*************************************************************************
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        len1, len2 = len(nums1), len(nums2)
        left, right = 0, len1
        while left <= right:
            part1 = (left + right) // 2
            part2 = (len1 + len2 + 1) // 2 - part1
            max_left1 = float('-inf') if part1 == 0 else nums1[part1 - 1]
            min_right1 = float('inf') if part1 == len1 else nums1[part1]
            max_left2 = float('-inf') if part2 == 0 else nums2[part2 - 1]
            min_right2 = float('inf') if part2 == len2 else nums2[part2]
            if max_left1 <= min_right2 and max_left2 <= min_right1:

                # Even total length
                if (len1 + len2) % 2 == 0:
                    return (
                        max(max_left1, max_left2) +
                        min(min_right1, min_right2)
                    ) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = part1 - 1
            else:
                left = part1 + 1
*************************************************************************
Approach 1: Brute Force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
s = Solution()
st = "babadda"
print(s.longestPalindrome(st))		==>	adda
*************************************************************************
class Solution(object):
    def rotated_arr(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        rotated_arr = [0] * n
        for i in range(n):
            rotated_arr[(i + k) % n] = nums[i]
        nums[:] = rotated_arr
        return nums
arr = [1, 2, 3, 4, 5]
d = 2
s = Solution()
print("Original array : ", arr)
result = s.rotated_arr(arr, d)
print("Rotated array : ", result)
------------------------------------------
n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
Original array :  [1, 2, 3, 4, 5]
Rotated array :  [4, 5, 1, 2, 3]
*************************************************************************
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        maxArea = 0
        while left < right:
            distance = right - left
            area = min(height[left], height[right]) * distance
            maxArea = max(maxArea, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
height = [1,8,6,2,5,4,8,3,7]
s = Solution
print(Solution.maxArea(s, height))
OUTPUT: 49
*************************************************************************
def isPalindrome(x):
    if x < 0:
        return False
    digit, n = 0, x
    while n:
        n, r = divmod(n, 10)
        print(n, r)
        digit = digit * 10 + r
    return digit == x
print(isPalindrome(121))
-------------------------------------
def isPalindrome(x):
    if x < 0:
        return False
    reverse = 0
    temp = x
    while temp:
        reverse = reverse * 10 + temp % 10
        temp = temp // 10
        print(reverse, temp)
    return reverse == x
print(isPalindrome(121))
OUTPUT : True
*************************************************************************
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        stack = []
        while s or p:
          if len(p) > 1 and p[1] == '*':
            while (s and p) and ((p[0] == '.') or (s[0] == p[0])):
              stack.append((s, p[2:]))
              s = s[1:]
            p = p[2:]
          elif (p and s and (p[0] == '.')) or (p and s and (p[0] == s[0])):
            p = p[1:]
            s = s[1:]
          elif len(stack) > 0:
            s, p = stack.pop(-1)
          else:
            return False
        return (not s) and (not p)
s = Solution()
print(s.isMatch("aa","a*"))
print(s.isMatch("aa","a"))
print(s.isMatch("ab",".*"))

True
False
True
*************************************************************************
class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1000 : 'M',
            900 : 'CM',
            500 : 'D',
            400 : 'CD',
            100 : 'C',
            90 : 'XC',
            50 : 'L',
            40 : 'XL',
            10 : 'X',
            9 : 'IX',
            5: 'V',
            4 : 'IV',
            1 : 'I'
        }
        ans = ""
        for key in dict.keys():
            val = num // key #Floor devide
            ans += val * dict[key]
            num -= val * key
        return ans
OUTPUT : 3
"III"
*************************************************************************
class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = 0
        while i < len(s):
            if i < len(s)-1 and d[s[i]] < d[s[i+1]]:
                ans += d[s[i+1]] - d[s[i]]
                i += 1
            else:
                ans += d[s[i]]
            i += 1
        return ans
OUTPUT: III
3
*************************************************************************
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for a, b in zip(s, s[1:]):
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                res += roman[a]
        return res + roman[s[-1]]
*************************************************************************
class Solution:
    def longestCommonPrefix(strs):
        prefix = ''
        L = min([len(s) for s in strs])
        for i in range(L):
            ci = strs[0][i]
            for s in strs[1:]:
                if ci != s[i]:
                    return prefix
            prefix += ci
        return prefix
strs = ["flower","flow","flght"]
print(Solution.longestCommonPrefix(strs))
OUTPUT: ["flower","flow","flight"]
"fl"
*************************************************************************
class Solution:
    def longestCommonPrefix(strs):
        ans = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans
strs = ["flower","flow","flght"]
print(Solution.longestCommonPrefix(strs))
*************************************************************************
class Solution:
    def threeSum(nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))
----------------------------------------------------------------
class Solution:
    def threeSum(nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))
-----------------------------------------------------
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res
nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))
OUTPUT : {(-1, 2, -1), (-1, 1, 0)}
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
					Hackerrank
*************************************************************************
#!/bin/python3
import math
import os
import random
import re
import sys
# 'getRemovableIndices' function below.
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING str1
#  2. STRING str2

def getRemovableIndices(str1, str2):
    result = []
    for i in range(len(str1)):
        new_str = str1[:i] + str1[i+1:]
        if new_str == str2:
            result.append(i)
    if not result:
        return [-1]
    return result
if __name__ == '__main__':
    str1 = input()
    str2 = input()
    result = getRemovableIndices(str1, str2)
    print('\n'.join(map(str, result)))
aabbb
aabb
2
3
4

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************

*************************************************************************
