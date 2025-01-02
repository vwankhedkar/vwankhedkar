import pickle
class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eddr = eaddr
    def display(self):
        print('Eno: {}, Ename: {}, Esal: {}, Eaddr: {}'.format(self.eno, self.ename, self.esal, self.eddr))
e = Employee(100,'Vais',1000,'Bangalore')

# Serialization or pickling
with open('emp.ser','wb') as f:
    pickle.dump(e, f)
print("Pickling of Employee object completed")

#Deserialization or unpickling
with open('emp.ser','rb') as f:
    newobj = pickle.load(f)
print("Unpickling of employee object completed")
print("Printing Employee information...")
newobj.display()
OUTPUT
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
Pickling of Employee object completed
Unpickling of employee object completed
Printing Employee information...
Eno: 100, Ename: Vais, Esal: 1000, Eaddr: Bangalore

Process finished with exit code 0
