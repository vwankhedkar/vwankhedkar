import keyword
keywordlist = keyword.kwlist
print(keywordlist)
print(keyword.iskeyword("try"))

OUTPUT
['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
True
****************************************************************************
x = "This \'is\' a string"
y = "This is string in \'single\' quotes"
z= """
This is 
multiline comment
"""
c = '''
This is also multiline comment
'''
print("is" in c)
print(x)
print(y[5])
print(z)
print(c)
OUTPUt-
True
This 'is' a string
i

This is 
multiline comment


This is also multiline comment
