def findTwoSum(arr, target):
    
    for p1 in range(len(arr)):
        numToFond = target - arr[p1]
        for p2 in range(p1+1, len(arr)):
            if (numToFond == arr[p2]):
                return p1, p2
 
arr = [9, 7, 2, 4, 6, 8, 2, 1, 5]
target = 14
print(findTwoSum(arr, target))

****************************************

