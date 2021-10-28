import math
def getMaxWaterContainer(heights):
    maxArea = 0
    for p1 in range(len(heights)):
        for p2 in range(p1+1, len(heights)):
            height = min(heights[p1], heights[p2])
            width = p2 - p1
            area = height * width
            maxArea = max(maxArea,area)
    return maxArea
 
heightsArray = [9, 7, 2, 4, 6, 8, 2, 1, 5]
print(getMaxWaterContainer(heightsArray))
**********************************************

l1 = [6, 9 ,2, 3, 5, 8]
max_area= 0

#bruit force approach 
for i in range(0,len(l1)):
	for j in range(1, len(l1)):
		height = min(l1[j] ,l1[i])
		#print (height)
		width = j - i
		area = height * width
		max_area = max(area, max_area)
print (max_area)

***********************************************
#Optimal approach
l1 = [6, 9 ,2, 3, 5, 8]
p1= 0 
p2 = len(l1) - 1
max_a = 0

while (p1 < p2 ):
	height = min(l1[p1], l1[p2])
	width = p2 - p1
	area = height * width
	max_a = max(max_a, area)
	if (l1[p1] <= l1[p2]) :
		p1+=1
	else: p2-=1
print(max_a) 
