class Solution:
    def findDisappearedNumbers(nums):
        l = []
        for i in range(1,len(nums)):
            if i not in nums:
                l.append(i)
            else:
                continue
        return l
nums = [4,3,2,7,8,2,3,1]
print(Solution.findDisappearedNumbers(nums))

OUTPUT: [5, 6]
