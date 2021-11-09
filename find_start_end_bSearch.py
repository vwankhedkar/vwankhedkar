class Solution(object):
    def binarySearch(self, nums, l, r, target):
        if len(nums) <= 0:
            return None
        while (l <= r):
            mid = (l + r) // 2
            foundVal = nums[mid]
            if (foundVal == target):
                return mid
            elif (foundVal < target):
                l = mid+1
            else:
                r = mid -1
        return -1

    def searchRange(self, nums, target):
        if len(nums) < 1: return [-1, -1]
        firstPos = self.binarySearch(nums, 0, len(nums)-1, target)
        if (firstPos == -1): return [-1, -1]
        endPos = firstPos
        startPos = firstPos
        # tmp1, tmp2 = 0, 0
        while (startPos != -1):
            tmp1 = startPos
            startPos = self.binarySearch(nums, 0, startPos-1, target)
        startPos = tmp1

        while (endPos != -1):
            tmp2 = endPos
            endPos = self.binarySearch(nums, endPos + 1, len(nums)-1, target)
        endPos = tmp2
        return [startPos, endPos]

s = Solution()
arr = [1,2,3,4,7,7,8,10]
n = len(arr)
print(s.searchRange(arr, 7))
