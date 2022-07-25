class Solution:
    def findDisappearedNumbers(nums):
        for n in nums:
            i = abs(n) -1 
            nums[i] = -1 * abs(nums[i])
            print(i, nums[i])
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i+1)
        return res
nums = [4,3,2,7,8,2,3,1]
print(Solution.findDisappearedNumbers(nums))
-------------------------------------------------
def missing_elements(vec):
    # Vector to store the list
    # of missing elements
    mis = []
    # For every given element
    for i in range(len(vec)): 
        # Find its index
        temp = abs(vec[i]) - 1
        # Update the element at the found index
        if vec[temp] > 0:
            vec[temp] = -vec[temp]
    for i in range(len(vec)):
        # Current element was not present
        # in the original vector
        if (vec[i] > 0):
            mis.append(i + 1)
    return mis

nums = [4,3,2,7,8,2,3,1]
print(missing_elements(nums))

OUTPUT: [5, 6]
