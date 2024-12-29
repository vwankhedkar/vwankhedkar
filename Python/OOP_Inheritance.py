Single inheritance
class A:
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B(A):
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")
a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature3()
b1.feature4()
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
Feature1 working
Feature2 working
Feature3 working
Feature4 working
********************************************************************************************************************************
Multilevel inheritance
class A:
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B(A):
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")
class C(B):
    def feature5(self):
        print("Feature5 working")
a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
c1 = C()
c1.feature5()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
OUTPUT
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
Feature1 working
Feature2 working
Feature1 working
Feature2 working
Feature3 working
Feature4 working
Feature5 working
Feature1 working
Feature2 working
Feature3 working
Feature4 working
************************************************************************************************************************************
Multiple inheritance
class A:
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B:
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")
class C(A,B):
    def feature5(self):
        print("Feature5 working")
a1 = A()
a1.feature1()
a1.feature2()
b1 = B()
b1.feature3()
b1.feature4()
c1 = C()
c1.feature5()
c1.feature1()
c1.feature2()
c1.feature3()
c1.feature4()
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
Feature1 working
Feature2 working
Feature3 working
Feature4 working
Feature5 working
Feature1 working
Feature2 working
Feature3 working
Feature4 working
********************************************************************************************************************************
Constructor
class A:
    def __init__(self):
        print("In A Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B(A):
    def __init__(self):
        print("In B Init ...")
    def feature3(self):
        print("Feature3 working")
    def feature4(self):
        print("Feature4 working")
a1 = A()
a2 = B()
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
In A Init ...
In B Init ...
*****************************************************************************************************************************************
Calling constructor of parent in child with super
class A:
    def __init__(self):
        print("In A Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B(A):
    def __init__(self):
        super().__init__()
        print("In B Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature4(self):
        print("Feature4 working")
a2 = B()
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
In A Init ...
In B Init ...
************************************************************************************************************************************
class A:
    def __init__(self):
        print("In A Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B:
    def __init__(self):
        print("In B Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature4(self):
        print("Feature4 working")
class C(A,B):
    def __init__(self):
        print("In C init ...")
a2 = C()
In C init ...
*****************************************************************************************************************************
class A:
    def __init__(self):
        print("In A Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature2(self):
        print("Feature2 working")
class B:
    def __init__(self):
        print("In B Init ...")
    def feature1(self):
        print("Feature1 working")
    def feature4(self):
        print("Feature4 working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init ...")
a2 = C()
In A Init ...
In C init ...
***********************************************************************************************************************
Method Resolution Order (MRO)
class A:
    def __init__(self):
        print("In A Init ...")
    def feature1(self):
        print("Feature1-A working")
    def feature2(self):
        print("Feature2 working")
class B:
    def __init__(self):
        print("In B Init ...")
    def feature1(self):
        print("Feature1-B working")
    def feature4(self):
        print("Feature4 working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init ...")
a1 = C()
a1.feature1()
In A Init ...
In C init ...
Feature1-A working
*******************************************************************************************************************
class A:
    def __init__(self):
        print("In A Init ...")
    def feature1(self):
        print("Feature1-A working")
    def feature2(self):
        print("Feature2 working")
class B:
    def __init__(self):
        print("In B Init ...")
    def feature1(self):
        print("Feature1-B working")
    def feature4(self):
        print("Feature4 working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init ...")
    def feat(self):
        super().feature2()
a1 = C()
a1.feat()
In A Init ...
In C init ...
Feature2 working
********************************************************************************************************************
Duck Typing
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class Laptop:
    def code(self,ide):
        ide.execute()
ide = Pycharm()
lap1 = Laptop()
lap1.code(ide)
OUTPUT :
Compiling
Running
********************************************************************************************************
class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")
class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self,ide):
        ide.execute()
ide = MyEditor()
lap1 = Laptop()
lap1.code(ide)
OUTPUT
Spell Check
Convention Check
Compiling
Running
*************************************************************************************************************
  Operator overloading
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
    def __str__(self):
    #    return self.m1, self.m2
        return ' {} {} '.format(self.m1, self.m2)
s1 = Student(58, 69)
s2 = Student(69, 65)
s3 = s1 + s2
if (s1 > s2):
    print("s1 wins")
else:
    print("s2 wins")
a = 9
print(a.__str__())
print(s1.__str__())
print(s2.__str__())
print(s1)
print(s2)
OUTPUT
s2 wins
9
 58 69 
 69 65 
 58 69 
 69 65 
********************************************************************************************************
Method overloading (doesn't support in python
class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a + b
        else:
            s = a
        return s
s1 = Student(58,69)
print(s1.sum(5,9,6))
print(s1.sum(5,9))
print(s1.sum(5))
20
14
5
***********************************************************************************************
Method overriding
class A:
    def show(self):
        print("In A Show")
class B(A):
    pass
a1 = B()
a1.show()
OUTPUT - In A Show

class A:
    def show(self):
        print("In A Show")
class B(A):
    def show(self):
        print("In B Show")
a1 = B()
a1.show()
OUTPUT - In B Show

