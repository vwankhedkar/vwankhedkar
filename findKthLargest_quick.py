class Solution(object):
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def getPartition(self, nums, left, right):
        pivotElement = nums[right]
        partitionIdx = left

        for j in range(left, right):
            if nums[j] <= pivotElement:
                self.swap(nums, partitionIdx, j)
                partitionIdx += 1
        self.swap(nums, partitionIdx, right)
        return partitionIdx


    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        indexToFind = len(nums)-k
        self.quickSort(nums, 0, (len(nums)-1))
        return nums[indexToFind]

    def quickSort(self, nums, left, right):
        if (left < right):
            partitionIndex = self.getPartition(nums, left, right)
            self.quickSort(nums, left, partitionIndex-1)
            self.quickSort(nums, partitionIndex+1, right)


s = Solution()
nums = [5,3,1,6,4,2]
print(s.findKthLargest(nums, 4))
