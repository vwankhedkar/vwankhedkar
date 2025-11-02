Files copy
f1 = open('file1.txt','r')
f2 = open('file2.txt','w')
data = f1.read()
f2.write(data)
f1.close()
f2.close()
print("Data copied successfully ....",f1.closed)
OUTPUT - Data copied successfully .... True
***************************************************************************************
file = open("D:\\python-webtraining\\scripts\\Algorithms\\temp_file.txt", 'r')
dir = {}
for line in file:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for w in words:
        # w = w.strip()
        if w in dir:
            dir[w] = dir[w] + 1
        else:
            dir[w] = 1
print(dir)
*********************************************************************************
def readAll():
    phones = {}
    githubs = {}
    
    with open('datafile.txt', 'r') as df:
        for line in df:
            parts = line.strip().split()
            if len(parts) < 3:
                continue  # skip incomplete lines
            # Handle names with spaces — join everything except last 2 items
            name = ' '.join(parts[:-2])
            phone = parts[-2]
            github = parts[-1]
            
            phones[name] = phone
            githubs[name] = github

    print("Phone Numbers:")
    for name, phone in phones.items():
        print(f"{name}: {phone}")

    print("\nGitHub Usernames:")
    for name, gh in githubs.items():
        print(f"{name}: {gh}")
readAll()
**************************************************************************************
i = 0
with open('file3.txt', 'w') as f:
    for i in range(5):
        f.write(f"This is line {i}\n")  # Use f-string for formatting and add a newline
        print("Is file closed", f.closed)
print("Is file closed", f.closed)
OUTPUT - Is file closed False
Is file closed False
Is file closed False
Is file closed False
Is file closed False
Is file closed True
**************************************************************************************
tell current position of curser in the file
f = open('file3.txt','r')
print(f.tell())
OUTPUT - 0
**************************************************************************************
f = open('file3.txt','r')
print(f.tell())
print(f.read(2))    #Read 2 characters
print(f.tell())     # tell current cursor position
print(f.read(3))
print(f.tell())
OUTPUT 
0
Th
2
is 
5
********************************************************************************
f = open('file3.txt','r')
print(f.tell())
f.seek(3)
print(f.tell())
print(f.read(2))
f.seek(10)
print(f.read())
f.seek(0)
print(f.read())
OUTPUT
0
3
s 
ne 0
This is line 1
This is line 2

This is line 0
This is line 1
This is line 2
*********************************************************************************
f=open('file4.txt','w')
f.write('Iam an indian ')
with open('file4.txt','r+') as f:
    text = f.read()
    print("Data before modification....")
    print(text)
    print("The current curser position:",f.tell())
    f.seek(14)
    f.write('And in Bangalore')
    f.seek(0)
    text=f.read()
    print("Data after modification....")
    print(text)
OUTPUT
Data before modification....
Iam an indian 
The current curser position: 14
Data after modification....
Iam an indian And in Bangalore
*************************************************************************************
import os
fname = input("Enter filename: ")
if (os.path.isfile(fname)):
    print('File exists: ',fname)
    print('The content of the file is: ')
    f = open(fname,'r')
    text=f.read()
    print('*'*40)
    print(text)
    print('*' * 40)
    f.close()
else:
    print('File doesnot exist',fname)
OUTPUT
Enter filename: file4.txt
File exists:  file4.txt
The content of the file is: 
****************************************
Iam an indian And in Bangalore
****************************************
Enter filename: abc
File doesnot exist abc
***************************************************************************************
Copy image file
f = open('Me1.JPG','rb')
f1 = open('Me2.JPG','wb')
for i in f:
    f1.write(i)
***************************************************************
try:
    f = open('myfile.txt','r')
    print(f.read())
    print(f.readline())
    print(f.readlines())
finally:
    f.close()
f.read()        #read total file
user        city        email
jake        Lucas       jake@mymail.com
lucas       London      lucas@mymail.com
Barcelona   Doha        Barcelona@mymail.com
f.readline() # read line by line
user        city        email
(f.readlines()        # read whole file and return list
['user        city        email\n', 'jake        Lucas       jake@mymail.com\n', 'lucas       London      lucas@mymail.com\n', 'Barcelona   Doha        Barcelona@mymail.com']
*************************************************
try:
    f = open('myfile.txt','r')
    line = f.readline()
    while (line):
        print(line)
        line = f.readline()
finally:
    f.close()
user        city        email
jake        Lucas       jake@mymail.com
lucas       London      lucas@mymail.com
Barcelona   Doha        Barcelona@mymail.com
**********************************************
with open("myfile.txt",'r') as f:
    print(f.readline())
    list2 = f.read().split("\n")
    print(list2)
user        city        email

['jake        Lucas       jake@mymail.com', 'lucas       London      lucas@mymail.com', 'Barcelona   Doha        Barcelona@mymail.com']

**************************************************
with open("myfile.txt",'r') as f:
    for line in f:
        print(line.strip())
user        city        email
jake        Lucas       jake@mymail.com
lucas       London      lucas@mymail.com
Barcelona   Doha        Barcelona@mymail.com
***************************************************
with open("logfile.txt", "w") as file:
    file.write("Starting application....\n")
with open("logfile.txt", "a") as file:
    file.write("Another log entry...\n")
with open("logfile.txt", "r") as file:
    for line in file:
        if "error" not in line.lower():
            print(line)
Starting application....
Another log entry...
*********************************************************
Replace file contents with user input in same file
s = input("Enter text to replace the existing contents:")
f = open("input.txt", "r+")
f.truncate(0)
f.write(s)
f.close()
with open("input.txt","r") as fh:
    print(fh.readlines())
print("Text replaced ....")
*********************************************************
import sys
import fileinput
x = input("Enter text to be replaced:")
y = input("Enter replacement text")
for l in fileinput.input(files = "file.txt"):
    l = l.replace(x, y)
    sys.stdout.write(l)
*********************************************************
with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()
print(data)
data[1] = "Here is modified Line 2 \n"
with open('input.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)
*********************************************************
try:
    with open('example.txt', 'w') as file:
        file.write("Hello, Python ! \n")
        file.write("Writing to files is essential.")
    with open('example.txt', 'a') as file:
        file.write("\n Appending new line.")
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
*********************************************************
import csv
# Writing to CSV file
with open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "age"])
    writer.writerow(["Alice", "30"])
    writer.writerow(["Bob", 25])
# Reading from CSV file
with open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
['Name', 'age']
['Alice', '30']
['Bob', '25']
*********************************************************
import json
data = {
    "name" : "John",
    "age"   : 28,
    "city" : "New York"
}
# Writing to JSON file
with open('data.json','w') as file:
    json.dump(data, file)
# Reading from JSON file
with open('data.json','r') as file:
    data = json.load(file)
    print(data)
{'name': 'John', 'age': 28, 'city': 'New York'}
*********************************************************
import os
file_path = os.path.join('example.txt','loc1','loc2')
try:
    with open('example.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())
except FileNotFoundError:
    print("File Not Found!")
except Exception as e:
    print(f"An weeor occured : {e}")
*********************************************************
fp = open("data.txt", "w")
print("Dayalu Dean", file=fp)
fp.seek(7)
print("in Deen Dayal Nagar.", file=fp)
fp.close()
Dayalu in Deen Dayal Nagar.
*********************************************************

*********************************************************

*********************************************************

*********************************************************
