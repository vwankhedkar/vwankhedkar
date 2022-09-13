class Solution:
    def fourSum(nums, target):
        nums.sort()
        n, res = len(nums), set()
        for i in range(n):
            for j in range(i + 1, n):
                low, high = j + 1, n - 1
                while low < high:
                    if nums[i] + nums[j] + nums[low] + nums[high] == target:
                        res.add((nums[i], nums[j], nums[low], nums[high]))
                        low += 1
                        high -= 1
                    elif nums[i] + nums[j] + nums[low] + nums[high] < target:
                        low += 1
                    else:
                        high -= 1

        return res
nums = [1,0,-1,0,-2,2]
target = 0
print(Solution.fourSum(nums, target))
OUTPUT: {(-2, -1, 1, 2), (-1, 0, 0, 1), (-2, 0, 0, 2)}
