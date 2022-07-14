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
