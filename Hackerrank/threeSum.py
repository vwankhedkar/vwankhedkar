class Solution:
    def threeSum(nums):
        res = set()
        m = {}
        nums.sort()
        for i in range(len(nums)):
            target = - nums[i]
            m.clear()
            for j in range(i + 1, len(nums)):
                if nums[j] in m:
                    candidate = (nums[i], nums[j], nums[m[nums[j]]])
                    res.add(candidate)
                else:
                    m[target - nums[j]] = j
        return res

nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))
----------------------------------------------------
class Solution:
    def threeSum(nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))
----------------------------------------------------------------
class Solution:
    def threeSum(nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return res
nums = [-1,0,1,2,-1,-4]
print(Solution.threeSum(nums))

OUTPUT : {(-1, 2, -1), (-1, 1, 0)}
*************************************************************************
import math
class Solution:
    def threeSumClosest(nums, target):
        nums.sort()
        diff = math.inf
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]
                if abs(three_sum - target) < diff:
                    ans = three_sum
                    diff = abs(three_sum - target)
                if diff == 0:
                    break
                if three_sum < target:
                    j += 1
                else:
                    k -= 1
        return ans
nums = [-1,2,1,-4]
print(Solution.threeSumClosest(nums, 1))
OUTPUT: 2
