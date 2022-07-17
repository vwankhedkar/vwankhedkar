parens  = { '(' : ')',
          '[' : ']',
          '{' : '}'}

def isValid(s):
   if len(s) <= 0 or len(s)%2 != 0:
      return False
   stack = []
   for i in range(len(s)):
      if s[i] in parens.keys():
         stack.append(s[i])
      else:
         leftBracket = stack.pop()
         correctBracket = parens[leftBracket]
         if (s[i] != correctBracket):
            return False
   return len(stack) == 0
******************************************************************   
string = "{()[]}()"
print(isValid(string))

def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string: string = string.replace("()", "")
    return not string
******************************************************************
def valid_parentheses(string):
    cnt = 0
    for char in string:
        if char == '(' or char == '[' or char == '{': cnt += 1
        if char == ')' or char == ']' or char == ']': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False
  
# Driver Code 
if __name__ == "__main__": 
    string = "[[]][]()"
    string = list(string) 
  
    print("Yes") if valid_parentheses(string) else print("No") 
*********************************************************************
class Stack:
    """
    This is an implementation of a Stack.
    The "right" or "top" of this stack the end of the list.
    """

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

def valid_parentheses(symbol_string):
    """
    This is a practice problem.
    It checks to see if parenthesis's are balanced
    :param symbol_string: String
    :return Bool:
    """

    stack = Stack()
    for char in symbol_string:
        if char == "(":
            stack.push("(")
        elif char == ")":
            if stack.is_empty():
                return False
            else:
                stack.pop()

    if not stack.is_empty():
        return False
    else:
        return True
*********************************************************************

def valid_parentheses(string):
    dict = {'(':')','{':'}','[':']'}
    stack = []
    for ch in string:
        if ch in dict.keys():
            stack.append(ch) 
        elif ch in dict.values():
            if stack == []:
                return False
            stack.pop()

    return stack == []

elements = ["ed(k)(ymkar(auo)mf)crfxbff(vg)m", "()", ")(()))", "(", "(())((()())())", "(g)xq(go()duwomo)(qzhtuainkmabgw(j)dsb("]
for ele in elements:
    print(valid_parentheses(ele))
    
******************************************************************************************

def valid_parentheses(string):
    if len(string) % 2 !=0:
        return False
    dict = {'(':')'}
    stack = []
    for i in string:
        if i in dict.keys():
            stack.append(i)
        else:
            if stack == []:
                return False
            a = stack.pop()
            if i != dict[a]:
                return False

    return stack == []

elements = ["()", ")(()))", "(", "(())((()())())"]
for ele in elements:
    print(valid_parentheses(ele))
******************************************************************

# Python3 implementation of the approach 
  
# These are defined as global because they 
# are passed by reference 
count = 0
i = 0
j = -1
  
# This helper function is called whenever 
# closing bracket is encountered. 
# Hence count is decremented 
# j and i points to opening and closing 
# brackets to be matched respectively 
# If brackets at i and j is a match 
# replace them with "#" character and decrement j 
# to point next opening bracket to * be matched 
# Similarly, increment i to point to next closing 
# bracket to be matched 
# If j is out of bound or brackets 
# did not match return 0 
def helperFunc(s, tocom): 
    global i, j, count 
    count -= 1
    if j > -1 and s[j] == tocom: 
        s[i] = '#'
        s[j] = '#'
        while j >= 0 and s[j] == '#': 
            j -= 1
        i += 1
        return 1
    else: 
        return 0
  
# Function that returns true if s is a 
# valid balanced bracket string 
def isValid(s): 
    global i, j, count 
  
    # Empty string is considered balanced 
    if len(s) == 0: 
        return True
    else: 
  
        # Increments for opening bracket and 
        # decrements for closing bracket 
        result = False
        while i < len(s): 
            if s[i] == '}': 
                result = helperFunc(s, '{') 
                if result == 0: 
                    return False
            elif s[i] == ')': 
                result = helperFunc(s, '(') 
                if result == 0: 
                    return False
            elif s[i] == ']': 
                result = helperFunc(s, '[') 
                if result == 0: 
                    return False
            else: 
                j = i 
                i += 1
                count += 1
  
        # count != 0 indicates unbalanced parentheses 
        # this check is required to handle cases where 
        # count of opening brackets > closing brackets 
        if count != 0: 
            return False
        return True
  
# Driver Code 
if __name__ == "__main__": 
    string = "[[]][]()"
    string = list(string) 
  
    print("Yes") if isValid(string) else print("No") 
