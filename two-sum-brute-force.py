def findTwoSum(arr, target):
    
    for p1 in range(len(arr)):
        numToFond = target - arr[p1]
        for p2 in range(p1+1, len(arr)):
            if (numToFond == arr[p2]):
                return p1, p2
 
arr = [9, 7, 2, 4, 6, 8, 2, 1, 5]
target = 14
print(findTwoSum(arr, target))

OUTPUT : (0, 8)
******************************************
lst = []
def sum(l, target):
    for i in range(len(l)):
        for j in range(i+1, len(l)-1):
            if target == l[i] + l[j]:
                lst.append([i,j]) 
    return lst
l = [1,3,7,9,2]
target = 10
l1, l2 = sum(l, target)
print(sum(l, target))
print(l1, l2)
print("sum of numbers: {} = {} and {} location ".format(target, l1, l2))


****************************************

def find_sum_twonum(nums, target):    
    for p1 in range(len(nums)):
        num_to_find = target - nums[p1]
        for p2 in range(p1+1, len(nums)):
            if (num_to_find == nums[p2]):
                return p1, p2, nums[p1], nums[p2] 
nums = [1,3,7,9,2]
target = 11
loc_P1, loc_p2, n1, n2 = find_sum_twonum(nums, target)
print("Sum of numbers {} {} found at locations nums[{}] nums[{}]".format(n1, n2, loc_P1, loc_p2))

OUTPUT :-
    Sum of numbers 9 2 found at locations nums[3] nums[4]
****************************************************************************************************
leetcode :
    
# Count ways to calculate a target from elements of a specified list
def countWays(nums, n, target):
 
    # base case: if a target is found
    if target == 0:
        return 1
    # base case: no elements are left
    if n < 0:
        return 0
    # 1. ignore the current element
    exclude = countWays(nums, n - 1, target)
    # 2. Consider the current element
    #    2.1. Subtract the current element from the target
    #    2.2. Add the current element to the target
    include = countWays(nums, n - 1, target - nums[n]) + countWays(nums, n - 1, target + nums[n])
 
    # Return total count
    return exclude + include 
if __name__ == '__main__':
 
    # input list and target number
    nums = [5, 3, -6, 2]
    target = 6
    print(countWays(nums, len(nums) - 1, target), 'ways')
	
OUTPUT : 4 ways
*************************************************************************
efficient way
--------
dir = {}
def sum(l, target):
    for i in range(len(l)):
        # dir1.setdefault(i,[]).append(l[i])
        lst = dir.get(l[i],0)
        if (lst > 0):
            return (lst, i)
        else:
            num_find = target - l[i]
            dir[num_find] = i

l = [1,3,7,9,2]
target = 11
l1, l2 = sum(l, target)
print("sum of numbers: {} = {} + {} at location l[{}] and l[{}]]".format(target, l[l1], l[l2], l1, l2))

