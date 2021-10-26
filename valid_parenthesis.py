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
