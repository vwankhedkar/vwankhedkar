in_file = "file1.txt"
out_file = "file2.txt"

fin = open(in_file, "r")
fout = open(out_file, "w")

line = set()
for statment in fin:
    print("Duplicates -> ",statment)
    if str not in line:
        fout.write("*********File After removing Duplicates*********\n")
        fout.write(statment)
        line.add(str)

fout.close()
fin.close()
