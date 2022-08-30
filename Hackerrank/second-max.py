list1 = [-1, 4, 5, 12, 34, 67, 45, 22, 22, 0, 0, -1, 69, 79, 100]
max1 = list1[0]
max2 = list1[1]
if max1 < max2:
    max1, max2 = max2, max1
for i in range(2,len(list1)):
    if list1[i] > max1:
        max2 = max1
        max1 = list1[i]
    elif list1[i] > max2 and list1[i] < max1:
        max2 = list1[i]
print("First Highest Number: ", max1)
print("Second Highest Number: ", max2)

First Highest Number:  100
Second Highest Number:  79
----------------------------------------------------------
list1 = [-1, 69, 79, 4, 5, 12, 34, 67, 45, 22, 22, 0, 0, -1]

mx = max(list1[0], list1[1])
secondmax = min(list1[0], list1[1])
n = len(list1)
for i in range(2, n):
    if list1[i] > mx:
        secondmax = mx
        mx = list1[i]
    elif list1[i] > secondmax and \
            mx != list1[i]:
        secondmax = list1[i]
    elif mx == secondmax and \
            secondmax != list1[i]:
        secondmax = list1[i]

print("Second highest number is : ", \
      str(secondmax))
----------------------------------------------------------------

if __name__ == '__main__':
    n = int(input())
    a = input().split()
    l = list(set(a))
    for i in range(len(l)):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    print(l[-2])
    OUTPUT:
    5
    2 3 6 6 5
    5
