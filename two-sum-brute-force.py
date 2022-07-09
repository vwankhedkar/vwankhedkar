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
