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
