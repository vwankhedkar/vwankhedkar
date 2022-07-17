# Time:  O(C(n, c)), try out all possible substrings with the minimum c deletion.
# Space: O(c), the depth is at most c, and it costs n at each depth
#
# Remove the minimum number of invalid parentheses in order to
# make the input string valid. Return all possible results.
#
# Note: The input string may contain letters other than the
# parentheses ( and ).
#
# Examples:
# "()())()" -> ["()()()", "(())()"]
# "(a)())()" -> ["(a)()()", "(a())()"]
# ")(" -> [""]
#

# DFS solution.
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Calculate the minimum left and right parantheses to remove
        def findMinRemove(s):
            left_removed, right_removed = 0, 0
            for c in s:
                if c == '(':
                    left_removed += 1
                elif c == ')':
                    if not left_removed:
                        right_removed += 1
                    else:
                        left_removed -= 1
            return (left_removed, right_removed)

        # Check whether s is valid or not.
        def isValid(s):
            sum = 0
            for c in s:
                if c == '(':
                    sum += 1
                elif c == ')':
                    sum -= 1
                if sum < 0:
                    return False
            return sum == 0

        def removeInvalidParenthesesHelper(start, left_removed, right_removed):
            if left_removed == 0 and right_removed == 0:
                tmp = ""
                for i, c in enumerate(s):
                    if i not in removed:
                        tmp += c
                if isValid(tmp):
                    res.append(tmp)
                return
    
            for i in xrange(start, len(s)):
                if right_removed == 0 and left_removed > 0 and s[i] == '(':
                    if i == start or s[i] != s[i - 1]:  # Skip duplicated.
                        removed[i] = True
                        removeInvalidParenthesesHelper(i + 1, left_removed - 1, right_removed)
                        del removed[i]
                elif right_removed > 0 and s[i] == ')':
                    if i == start or s[i] != s[i - 1]:  # Skip duplicated.
                        removed[i] = True
                        removeInvalidParenthesesHelper(i + 1, left_removed, right_removed - 1);
                        del removed[i]

        res, removed = [], {}
        (left_removed, right_removed) = findMinRemove(s)
        removeInvalidParenthesesHelper(0, left_removed, right_removed)
        return res
==============================================================
class Solution(object):
  def minRemoveToMakeValid(self, s: str) -> str:
        removed_ind = set()
        stack_ind = []
        for ind, char in enumerate(s):
            if char not in "()":
                continue
            if char == '(':
                stack_ind.append(ind)
            elif stack_ind == []:
                removed_ind.add(ind)
            else:
                stack_ind.pop()
        removed_ind = removed_ind.union(set(stack_ind))
        output = ""
        for ind, char in enumerate(s):
            if ind in removed_ind:
                continue
            output += char
        return output

string1 = "abc"
print(Solution().minRemoveToMakeValid(string1))
string1 = "a)b(c)d"
print(Solution().minRemoveToMakeValid(string1))
string1 = "a))c((b"
print(Solution().minRemoveToMakeValid(string1))
string1 = "a)b(c)d"    
print(Solution().minRemoveToMakeValid(string1))
string1 = "lee(t(c)o)de)"
print(Solution().minRemoveToMakeValid(string1))
string1 = "))(("
print(Solution().minRemoveToMakeValid(string1))


****************************************************
class Solution(object):
  def minRemoveToMakeValid(self, s: str) -> str:
        remove_ind = set()
        stack_ind = []
        for ind, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                stack_ind.append(ind)
            elif stack_ind == []:
                remove_ind.add(ind)
            else:
                stack_ind.pop()
        for ind, char in enumerate(s):
            if char not in "[]":
                continue
            if char == "[":
                stack_ind.append(ind)
            elif stack_ind == []:
                remove_ind.add(ind)
            else:
                stack_ind.pop()
        for ind, char in enumerate(s):
            if char not in "{}":
                continue
            if char == "{":
                stack_ind.append(ind)
            elif stack_ind == []:
                remove_ind.add(ind)
            else:
                stack_ind.pop()
        remove_ind = remove_ind.union(set(stack_ind))
        output = ""
        for ind, char in enumerate(s):
            if ind in remove_ind:
                continue
            output+=char
        return output

# s = "lee(t(c)o)de)"
s = "}a)]b[(c)]{d}{"
l = Solution()
print(l.minRemoveToMakeValid(s))

==============================================
class Solution:
   def minRemoveToMakeValid(self, s):
      stack = []
      res = list(s)
      output = ''
      for i in range(len(s)):
         if s[i] == '(' and len(s)>=0:
            stack.append(i)
         elif s[i] == ')' and len(stack)>0:
            stack.pop()
         elif s[i] == ')':
            res[i] = ""
            output = "".join(res)

      while len(stack):
         curIndx = stack.pop()
         res[curIndx] = ""
         output = "".join(res)
      return output 

string1 = "a))c((b"
# string1 = "a)b(c)d"    
# string1 = "lee(t(c)o)de)"
# string1 = "))(("
# print(string1.replace(')', ""))
print(Solution().minRemoveToMakeValid(string1))

OUPUT :
ab(c)d
PS D:\ESH_AUTOMATION> & C:/Programs/Python/Python39/python.exe d:/ESH_AUTOMATION/webUI/try.py
lee(t(c)o)de
PS D:\ESH_AUTOMATION> & C:/Programs/Python/Python39/python.exe d:/ESH_AUTOMATION/webUI/try.py
acb
============================================================================================
class Solution:
   def minRemoveToMakeValid(self, s):
      stack = []
      res = list(s)
      output = ''
      for i in range(len(s)):
         if s[i] == '(' and len(s)>=0:
            stack.append(i)
         elif s[i] == ')' and len(stack)>0:
            stack.pop()
         elif s[i] == ')':
            res[i] = ""
            output = "".join(res)
         elif s[i] != '(' or s[i] != ')':
            output = "".join(res)
      while len(stack):
         curIndx = stack.pop()
         res[curIndx] = ""
         output = "".join(res)
      return output 

string1 = "abc"
# string1 = "a)b(c)d"
# string1 = "a))c((b"
# string1 = "a)b(c)d"    
# string1 = "lee(t(c)o)de)"
# string1 = "))(("
# print(string1.replace(')', ""))
print(Solution().minRemoveToMakeValid(string1))
