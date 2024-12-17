class FirstClass:
    def __init__(self):
        pass
    def something_useful(self,string):
        return string

class Decorator:

    def __init__(self,wrapped):
        self._wrapped = wrapped

    def withUnderscores(self,string):
        return "_".join(string.split())

    def __getattr__(self,name):
        return getattr(self._wrapped,name)

def div(a,b):
    print(a/b)

def smart(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart(div)
div1(2,4)

OUTPUT - 2.0
