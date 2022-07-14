Not efficient solution :
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
        return max_len                

b = Solution()
strg = "pwwkew"
print(b.lengthOfLongestSubstring(strg))
********************************************************************
def areDistinct(strg, i, j):
   visited = [0] * 26
   for k in range(i, j+1):
      if (visited[ord(strg[k]) - ord('a')] == True):
         return False

      visited[ord(strg[k]) - ord('a')] = True
   return True 
def longestUniqueSubsttr(strg):
   n  = len(strg)
   res = 0
   for i in range(n):
      for j in range(i, n):
         if areDistinct(strg, i, j):
            res = max(res, j-i+1)
   return res

strg = "geeksforgeeks"
print("The input is ", strg)
len = longestUniqueSubsttr(strg)
print("The length of the longest "
      "non-repeating character substring is ", len)
********************************************************************************
# Here, we are planning to implement a simple sliding window methodology
  
def longestUniqueSubsttr(string):
      
    # Creating a set to store the last positions of occurrence
    seen = {}
    maximum_length = 0
  
    # starting the initial point of window to index 0
    start = 0
      
    for end in range(len(string)):
  
        # Checking if we have already seen the element or not
        if string[end] in seen:
 
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, seen[string[end]] + 1)
  
        # Updating the last seen value of the character
        seen[string[end]] = end
        maximum_length = max(maximum_length, end-start + 1)
    return maximum_length
  
# Driver Code
string = "geeksforgeeks"
print("The input string is", string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", length)

*****************************************************************************
class Solution:

    def lengthOfLongestSubstring(self, s):
        size = len(s)
        if size <= 1:
            return size

        for left in range(size):
            longest = 0
            seenChar = {}
            currentLength = 0
            sub = ""
            for right in range(left, size):
                currentChar = s[right]
                if currentChar not in seenChar:
                    currentLength += 1
                    seenChar[currentChar] = True
                    longest = max(longest, currentLength)
                    sub += currentChar
                else:
                    break
            return longest, sub

b = Solution()
strg = "abcdeabcbb"
print(b.lengthOfLongestSubstring(strg))
***************************************************************************
def lengthOfLongestSubstring(s):
    size = len(s)
    longest = 0

    if size <= 1:
        return size

    for left in range(size):
        seenChars = {}
        currentLength = 0
        for right in range(left, size):
            currentChar = s[right]

            if currentChar in seenChars:
                break
            else:
                currentLength += 1
                seenChars[currentChar] = True
                longest = max(longest, currentLength)
    return longest

if __name__ == '__main__':
    s = "abcdabcbb"
    print(lengthOfLongestSubstring(s))
--------------------------------------------------------------------
class Solution:
   def lengthOfLongestSubstring(self, s):
      strlen = len(s)
      seenChar = {}
      substr= ""
      longest = 0
      finalList = []
      if (strlen <= 0):
         return strlen

      for L in range(strlen):
         if len(substr) > 0:
               finalList.append(substr)                  
         currLongest = 0
         substr =""
         for R in range(L, strlen):
            currChar = s[R]
            if currChar not in seenChar:
               seenChar[currChar] = 1
               substr += currChar
               currLongest += 1
               longest = max(currLongest, longest)              
            else:       
               break 
      return finalList, longest
b = Solution()
string = "abccabbdrew"
substring, length = b.lengthOfLongestSubstring(string)
print("Substring '{}' is having maximum length as : {}".format(substring[-1], length))

string = "abcdtabcbbuesmnk"
substring, length = b.lengthOfLongestSubstring(string)
print("Substring '{}' is having maximum length as : {}".format(substring[-1], length))

OUTPUT :
Substring 'drew' is having maximum length as : 4
Substring 'uesmnk' is having maximum length as : 6    
--------------------------------------------------------------------------------------
class Solution:
   def lengthOfLongestSubstring(self, s):
      strlen = len(s)
      seenChar = {}
      substr= ""
      longest = 0
      finalList = []
      if (strlen <= 0):
         return strlen

      for L in range(strlen):
         if len(substr) > 0:
               finalList.append(substr)                  
         currLongest = 0
         substr =""
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
      return longest, finalList                     

b = Solution()
strg = "abdtdaaoprnq"
length, substr = b.lengthOfLongestSubstring(strg)
maxlen = 0
max = ""
for ele in substr:
    if len(ele) > maxlen:
      max = ele
      maxlen = len(ele)
print("Inside string '{}' Substring '{}' is having maximum length as : {}".format(strg, max, maxlen)) 
OUTPUT :
Inside string 'abdtdaaoprnq' Substring 'aoprnq' is having maximum length as : 6
Inside string 'pwwkew' Substring 'wke' is having maximum length as : 3
