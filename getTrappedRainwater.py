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
def getTrappedRainwater(heights):
    left=0
    right=len(heights)-1
    totalWater, maxLeft, maxRight = 0, 0, 0
    while(left < right):
        if (heights[left] <= heights[right]):
            if heights[left] >= maxLeft:
                maxLeft = heights[left]
            else:
                totalWater += maxLeft - heights[left]
            left += 1
        else:
            if heights[right] >= maxRight:
                maxRight = heights[right]
            else:
                totalWater += maxRight - heights[right]
            right -= 1 
    return totalWater
elevationArray = [0, 1, 0, 2, 1, 0, 3, 1, 0, 1, 2]
print(getTrappedRainwater(elevationArray))
