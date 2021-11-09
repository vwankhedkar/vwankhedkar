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
*********************************************************************
QuickSelect:-
--------------
def kthSmallest(arr, l, r, k):
    if (k > 0 and k <= r - l + 1):
        index = partition(arr, l, r)

        if (index - l == k - 1):
            return arr[index]

        if (index - l > k - 1):
            return kthSmallest(arr, l, index-1, k)
        
        if (index - l < k - 1):
            return kthSmallest(arr, l, index-1, k)

        return kthSmallest(arr, index+1, r, k - index + l - 1)
    print("Index out of bound")

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

arr = [ 10, 4, 5, 8, 6, 11, 26 ]
n = len(arr)
k = 3
print("Kth smallest element is: ", end="")
print(kthSmallest(arr, 0, n-1, k))
