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
