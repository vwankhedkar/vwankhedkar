lst = [1,2,3,4,5,6]
target = 9
lst1 = []
dict = {}
for i in range(len(lst)):
    remain=target-lst[i]
    for j in range(i+1,len(lst)):
        if lst[j] == remain:
            lst1.append([lst[i],lst[j]])
            print("target {} = {} + {} located at locations {} and {}".format(target, lst[i],lst[j], i, j))
print(lst1)
OUTPUT:
target 9 = 3 + 6 located at locations 2 and 5
target 9 = 4 + 5 located at locations 3 and 4
[[3, 6], [4, 5]]
