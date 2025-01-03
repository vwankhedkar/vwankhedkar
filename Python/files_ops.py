Files copy
f1 = open('file1.txt','r')
f2 = open('file2.txt','w')
data = f1.read()
f2.write(data)
f1.close()
f2.close()
print("Data copied successfully ....")
Data copied successfully ....
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

