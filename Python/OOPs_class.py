class Computer:
	def config(self):
		print("i5, 16gb, 1TB")
com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
i5, 16gb, 1TB
i5, 16gb, 1TB
i5, 16gb, 1TB
i5, 16gb, 1TB
**********************************************************************************************************************************
class computer:
	def __init__(self,cpu,ram):
		print("In Init ...")
		self.cpu=cpu
		self.ram=ram

	def config(self):
		print("Config is: ", self.cpu, self.ram)

com1 = computer('i5',16)
com2 = computer('Ryzen 3',8)
com1.config()
com2.config()
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
In Init ...
In Init ...
Config is:  i5 16
Config is:  Ryzen 3 8
******************************************************************************************************************************
class computer:
	def __init__(self):
		self.name = "Vais"
		self.age = 28
	def update(self):
		self.age = 30
	def compare(self, other):
		if self.age == other.age:
			return True
		else:
			return False

c1 = computer()
c2 = computer()
if c1.compare(c2):
	print("They are same")
else:
	print("They are different")
OUTPUT - They are same
****************************************************************************************************************************
class car:
	wheels = 4
	def __init__(self):
		self.mil = 10
		self.com = "BMW"

c1 = car()
c2 = car()
c1.mil = 8
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
OUTPUT
BMW 8 4
BMW 10 4
*******************************************************************************************************
class car:
	wheels = 4
	def __init__(self):
		self.mil = 10
		self.com = "BMW"

c1 = car()
c2 = car()
c1.mil = 8
car.wheels = 5
print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)
BMW 8 5
BMW 10 5
**********************************************************************************************
class student:
	school = 'Modern'
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	@classmethod
	def info(cls):
		return cls.school
s1 = student(12,34,56)
s2 = student(89,32,12)
print(s1.avg())
print(student.info())
34.0
Modern
************************************************************************************
Static and class methods
class student:
	school = 'Modern'
	def __init__(self,m1,m2,m3):
		self.m1 = m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	@classmethod
	def getschool(cls):
		return cls.school
	@staticmethod
	def info():
		print("This is student static class")
s1 = student(12,34,56)
s2 = student(89,32,12)
print(s1.avg())
print(student.info())
student.info()
34.0
This is student static class
None
This is student static class
**************************************************************************************
  class within class
class student:
	def __init__(self,name,rollno):
		self.name = name
		self.rollno = rollno
		self.lap = self.Laptop()

	def show(self):
		print(self.name, self.rollno)
		self.lap.show()

	class Laptop:

		def __init__(self):
			self.brand = 'HP'
			self.cpu = 'i5'
			self.ram = 8

		def show(self):
			print(self.brand, self.cpu, self.ram)

s1 = student('Vais',2)
s2 = student('Wankh',3)
s1.show()
lap1 = student.Laptop()
Vais 2
HP i5 8
********************************************************************************************
Instance Method
class student:
    school = "Modern"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self): # instance
        return (self.m1 + self.m2 + self.m3) / 3
    def get_m1(self):       # Accessor Methods
        return self.m1
    def set_m1(self, value):       # Mutator method
        self.m1 = value

s1 = student(45, 60, 30)
s2 = student(30, 40, 50)
print(s1.avg())
print(s2.avg())
OUTPUT - 45.0
40.0
*************************************************************************************************
ClassMethod
class student:
    school = "Modern"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self): # instance
        return (self.m1 + self.m2 + self.m3) / 3
    @classmethod
    def getschool(cls):
        return cls.school

s1 = student(45, 60, 30)
s2 = student(30, 40, 50)
print(s1.avg())
print(student.getschool())
OUTPUT - 45.0
Modern
*********************************************************************************************
Static Method
class student:
    school = "Modern"
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self): # instance
        return (self.m1 + self.m2 + self.m3) / 3
    @classmethod
    def getschool(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is student class in info module")

s1 = student(45, 60, 30)
s2 = student(30, 40, 50)
print(s1.avg())
print(student.getschool())
student.info()
OUTPUT	45.0
Modern
This is student class in info module
