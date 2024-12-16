l = [8, 4, 0, 2, 5, 0, 1, 0, 7, 0]
for i in l:
    if i == 0:
        l.remove(i)
        l.append(i)
print(l)
OUTPUT - [8, 4, 2, 5, 1, 7, 0, 0, 0, 0]

arr = [8, 4, 0, 2, 5, 0, 1, 0, 7, 0]
def no_zer(arr):
    no_zer = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[no_zer],arr[i] = arr[i],arr[no_zer]
            no_zer += 1
    return arr
print(no_zer(arr))

arr = [8, 4, 0, 2, 5, 0, 1, 0, 7, 0]
def no_zer(arr):
    res = []
    c = 0
    for i in arr:
        if i == 0:
            c = c + 1
        else:
            res.append(i)
    for i in range(c):
        res.append(0)
    return res
print(no_zer(arr))

arr = [8, 4, 0, 2, 5, 0, 1, 0, 7, 0]
out = []
count = 0
for i in arr:
    if i != 0:
        out.append(i)
    else:
        count += 1
for i in range(count):
    out.append(0)
print(out)

