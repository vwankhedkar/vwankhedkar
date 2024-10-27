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

