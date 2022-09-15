class Solution:
    def searchInsert(nums, target):
        mid = len(nums)//2
        high = len(nums)-1
        low = 0
        while nums[mid] != target and low <= high:
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return mid+1 if target not in nums else mid
nums = [1,3,5,6]
target = 7
print(Solution.searchInsert(nums, target))
nums = [1,3,5,6]
target = 5
print(Solution.searchInsert(nums, target))
OUTPUT:
4
2
