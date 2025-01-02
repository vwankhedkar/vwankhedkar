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

