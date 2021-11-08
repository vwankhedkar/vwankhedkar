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

# s = "lee(t(c)o)de)"
s = "a)b(c)d"
l = Solution()
print(l.minRemoveToMakeValid(s))

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
