# Print all distinct elements of a given integer array

def printAllDistinctEle(Arr, n):
    print("The distinct elements of the array are:", end=" ")
    for i in range(0, n):
        d = 0
        for j in range(0, i):
            if (Arr[i] == Arr[j]):
                d = 1
                break
        if (d == 0):
            print(Arr[i], end=" ")


Arr = []
n = int(input("Input the array size\n"))
print("Input the integers in the array:")
for i in range(0, n):
    ele = int(input())
    Arr.append(ele)
printAllDistinctEle(Arr, n)

# Print all distinct elements of a given integer array

def printAllDistinctEle(Arr, n):
    print("The distinct elements of the array are:",end=" ")
    hashset = dict();
    for i in range(n):
        if (Arr[i] not in hashset.keys()):
            hashset[Arr[i]] = Arr[i];
            print(Arr[i], end = " ");
     
Arr = []
n = int(input("Input the array size\n"))
print("Input the integers in the array:")
for i in range(0, n):
    ele = int(input())
    Arr.append(ele)
printAllDistinctEle(Arr, n)

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\moveZeros.py 
Input the array size
5
Input the integers in the array:
12
7
8
12
7
The distinct elements of the array are: 12 7 8 
Process finished with exit code 0

