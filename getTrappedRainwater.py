def getTrappedRainwater(heights):
    totalWater = 0
    for p in range(len(heights)):
        leftp, rightp, maxLeft, maxRight = p, p, 0, 0
        while(leftp >= 0):
            maxLeft = max(maxLeft, heights[leftp])
            leftp -= 1
        while(rightp < len(heights)):
            maxRight = max(maxRight, heights[rightp])
            rightp += 1
        currentWater = min(maxLeft, maxRight) - heights[p]
        if currentWater >= 0:
            totalWater += currentWater

    return totalWater

elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(getTrappedRainwater(elevationArray))
*****************************************************************
class Solution:
    def trap(height):
        left=0
        right=len(height)-1
        totalWater, maxLeft, maxRight = 0, 0, 0
        while(left < right):
            if (height[left] <= height[right]):
                if height[left] >= maxLeft:
                    maxLeft = height[left]
                else:
                    totalWater += maxLeft - height[left]
                left += 1
            else:
                if height[right] >= maxRight:
                    maxRight = height[right]
                else:
                    totalWater += maxRight - height[right]
                right -= 1 
        return totalWater
elevationArray = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution.trap(elevationArray))
