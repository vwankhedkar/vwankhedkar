def builtString(s):
   buildString = []
   for p in range(len(s)):
      if s[p] != '#':
         buildString.append(s[p])
      elif len(buildString)!=0:
         buildString.pop()
   return buildString  

class Solution:
    def backspaceCompare(s, t):
      finalS = builtString(s)
      finalT = builtString(t)
      if len(finalS) != len(finalT):
         return False
      elif len(finalS)>0:
         for p in range(len(finalS)):
            if finalS[p] != finalT[p]:
               return False
      return True

s = "a#c"
t = "b"
print(Solution.backspaceCompare(s, t))

-----------------------------------------------
def buildString(str):
   lst = []
   for i in range(len(str)):
      if str[i] != '#':
         lst.append(str[i])
      elif len(lst)>0:
          lst.pop()   
   return lst

str1 = "abc##z"
str2 = "ab#z"
res1 = buildString(str1)
res2 = buildString(str2)
print(res1, res2)
if res1 == res2:
   print("True")
else:
   print("False")
------------------------------------------
Failing with given o/p 
def backspaceCompare(s, t):
   p1 = len(s)-1
   p2 = len(t)-1
   while (p1 >= 0 or p2 >= 0):
      if (s[p1] == '#' or t[p2] == '#'):
         if s[p1] == '#':
            backCount = 2
            while (backCount > 0):
               p1 -= 1
               backCount -= 1
               if (s[p1] == '#'):
                  backCount += 2
         if (t[p2] == '#'):
            backCount = 2
            while (backCount > 0):
               p2 -= 1
               backCount -= 1
               if (t[p2] == '#'):
                  backCount += 2
      else:
         if (s[p1] != t[p2]):
            return False
         else:
            p1 -= 1
            p2 -= 1   
   return True

s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))
*********************************************************
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
           for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return i, j

            
s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums, target))
