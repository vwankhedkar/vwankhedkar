class balance_parenthe:
    def __init__(self, word):
        self.word = word
    
    def isValid(self, word):
        if len(word) % 2 !=0:
            return False
        dict = {'(':')','{':'}','[':']'}
        stack = []
        for i in word:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == []:
                    return False
                a = stack.pop()
                if i != dict[a]:
                    return False

        return stack == []

elements = ["(())", "()[}", "()", ")(()))", "(", "(())((()())())"]
for ele in elements:
    s = balance_parenthe(ele)
    print(s.isValid(ele))
******************************************************************************

def matchClosing(X, start, end,
                   open, close):
 
    c = 1
    i = start + 1
    while (i <= end):
        if (X[i] == open):
            c += 1
        elif (X[i] == close):
            c -= 1
        if (c == 0):
            return i
        i += 1
    return i
 
# Function1 to match opening bracket
def matchingOpening(X, start, end,
                      open, close):
 
    c = -1
    i = end - 1
 
    while (i >= start):
        if (X[i] == open):
            c += 1
        elif (X[i] == close):
            c -= 1
        if (c == 0):
            return i
        i -= 1
 
    return -1
 
# Function to check balanced
# parentheses
def isBalanced(X, n):
 
    for i in range(n):
         
        # Handling case of opening
        # parentheses
        if (X[i] == '('):
            j = matchClosing(X, i, n - 1, '(', ')')
        elif (X[i] == '{'):
            j = matchClosing(X, i, n - 1, '{', '}')
        elif (X[i] == '['):
            j = matchClosing(X, i, n - 1, '[', ']')
 
        # Handling case of closing
        # parentheses
        else :
            if (X[i] == ')'):
                j = matchingOpening(X, 0, i, '(', ')')
            elif (X[i] == '}'):
                j = matchingOpening(X, 0, i, '{', '}')
            elif (X[i] == ']'):
                j = matchingOpening(X, 0, i, '[', ']')
 
            # If corresponding matching opening
            # parentheses doesn't lie in given
            # interval return 0
            if (j < 0 or j >= i):
                return False
 
            # else continue
            continue
 
        # If corresponding closing parentheses
        # doesn't lie in given interval, return 0
        if (j >= n or j < 0):
            return False
 
        # if found, now check for each opening and
        # closing parentheses in this interval
        start = i
        end = j
 
        for k in range(start + 1, end) :
            if (X[k] == '(') :
                x = matchClosing(X, k, end, '(', ')')
                if (not(k < x and x < end)):
                    return False
             
            elif (X[k] == ')'):
                x = matchingOpening(X, start, k, '(', ')')
                if (not(start < x and x < k)):
                    return False
 
            if (X[k] == '{'):
                x = matchClosing(X, k, end, '{', '}')
                if (not(k < x and x < end)):
                    return False
 
            elif (X[k] == '}'):
                x = matchingOpening(X, start, k, '{', '}')
                if (not(start < x and x < k)):
                    return False
                 
            if (X[k] == '['):
                x = matchClosing(X, k, end, '[', ']')
                if (not(k < x and x < end)):
                    return False
                 
            elif (X[k] == ']'):
                x = matchingOpening(X, start, k, '[', ']')
                if (not(start < x and x < k)):
                    return False
 
    return True
 
# Driver Code
if __name__ == "__main__":
     
    X = "[()]()"
    n = 6
    if (isBalanced(X, n)):
        print("Yes")
    else:
        print("No")
 
    Y = "[[()]])"
    n = 7
    if (isBalanced(Y, n)):
        print("Yes")
    else:
        print("No")
