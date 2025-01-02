import csv
with open('emp.csv','w') as f:
    w = csv.writer(f)
    print(type(w))
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    while True:
        eno=int(input('Enter Employee Number: '))
        ename = input('Enter Employee Name: ')
        esal = float(input('Enter Employee Salary: '))
        eaddr = input('Enter Employee Address: ')
        w.writerow([eno,ename,esal,eaddr])
        option=input('Do u want to insert more records: [Yes/No]: ')
        if option.lower()=='no':
            break
print("Total employees data written successfully to csv files...")

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
<class '_csv.writer'>
Enter Employee Number: 3
Enter Employee Name: abc
Enter Employee Salary: 3000
Enter Employee Address: pqr
Do u want to insert more records: [Yes/No]: no
Total employees data written successfully to csv files...

Process finished with exit code 0


ENO	ENAME	ESAL	EADDR
			
3	abc	3000	pqr
******************************************************************************
import csv	# Writing to CSV file
with open('emp.csv','w',newline='') as f:
    w = csv.writer(f)
    print(type(w))
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    while True:
        eno=int(input('Enter Employee Number: '))
        ename = input('Enter Employee Name: ')
        esal = float(input('Enter Employee Salary: '))
        eaddr = input('Enter Employee Address: ')
        w.writerow([eno,ename,esal,eaddr])
        option=input('Do u want to insert more records: [Yes/No]: ')
        if option.lower()=='no':
            break
print("Total employees data written successfully to csv files...")

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
<class '_csv.writer'>
Enter Employee Number: 1
Enter Employee Name: abc
Enter Employee Salary: 1000
Enter Employee Address: bca
Do u want to insert more records: [Yes/No]: Yes
Enter Employee Number: 2
Enter Employee Name: xyz
Enter Employee Salary: 2000
Enter Employee Address: zyx
Do u want to insert more records: [Yes/No]: Yes
Enter Employee Number: 3
Enter Employee Name: pqr
Enter Employee Salary: 3000
Enter Employee Address: rqp
Do u want to insert more records: [Yes/No]: no
Total employees data written successfully to csv files...

ENO	ENAME	ESAL	EADDR
1	abc	1000	bca
2	xyz	2000	zyx
3	pqr	3000	rqp

*********************************************************************************************************
import csv    # Reading CSV file
with open('emp.csv','r') as f:
    r = csv.reader(f)
    print(type(r))
    data = list(r)
    print(data)
    for row in data:
        for column in row:
            print(column,'\t',end='')
        print()

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
<class '_csv.reader'>
[['ENO', 'ENAME', 'ESAL', 'EADDR'], ['1', 'abc', '1000.0', 'bca'], ['2', 'xyz', '2000.0', 'zyx'], ['3', 'pqr', '3000.0', 'rqp']]
ENO 	ENAME 	ESAL 	EADDR 	
1 	abc 	1000.0 	bca 	
2 	xyz 	2000.0 	zyx 	
3 	pqr 	3000.0 	rqp 	
***********************************************************************************************************
from zipfile import *
f = ZipFile('file221.zip','w',ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
f.close()
print('zip file created successfully...')

# Unzip operation
f = ZipFile('file221.zip','r',ZIP_STORED)
names = f.namelist()
print("These files are zipped", names)

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
zip file created successfully...
These files are zipped ['file1.txt', 'file2.txt', 'file3.txt']
*************************************************************************************************************
from zipfile import *
f = ZipFile('file221.zip','w',ZIP_DEFLATED)
f.write('file1.txt')
f.write('file2.txt')
f.write('file3.txt')
f.close()
print('zip file created successfully...')

# Unzip operation
f = ZipFile('file221.zip','r',ZIP_STORED)
names = f.namelist()
print("These files are zipped", names)
for name in names:
    print("File Name: ", name)
    print("The content of file is :")
    f1 = open(name,'r')
    print(f1.read())
	
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\try.py 
zip file created successfully...
These files are zipped ['file1.txt', 'file2.txt', 'file3.txt']
File Name:  file1.txt
The content of file is :
nu_words = 0
with open(r'file1.txt', 'r') as file:

File Name:  file2.txt
The content of file is :
uasge of api how to do coding
oops concepts


File Name:  file3.txt
The content of file is :
Sql - basic questions queries
API - response , reuest how we get
