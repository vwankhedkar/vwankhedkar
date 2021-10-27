def BinarySearch(array, element):
    start, mid, step = 0, 0, 0
    end = len(array)

    while(start <= end):
        print("Subarray in step {}: {}".format(step, str(array[start:end+1])))
        step = step + 1
        mid = (start + end) // 2
        print("Mid element at position: {} is {}: ".format(mid, array[mid]))
        if element == array[mid]:
            return mid
        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

array = [ 1,2,4,6,8,9,10, 14, 20, 24, 30]
element = 24
print (BinarySearch(array, element))

OUTPUT --->

Subarray in step 0: [1, 2, 4, 6, 8, 9, 10, 14, 20, 24, 30]
Mid element at position: 5 is 9: 
Subarray in step 1: [10, 14, 20, 24, 30]
Mid element at position: 8 is 20:
Subarray in step 2: [24, 30]
Mid element at position: 10 is 30:
Subarray in step 3: [24]
Mid element at position: 9 is 24:
9
*******************************************************************************
def BinarySearch(array, element, start, end):
	step =0
	if start > end :
		return -1
	mid = (start + end) // 2

	if element == array[mid]:
		return mid
	if element < array[mid]:
		print("Sub Array", array[start: mid-1])
		return BinarySearch(array, element , start , mid-1)
	else :
		step = step +1
		print("Sub Array ",  array[mid+1: end])
		return BinarySearch(array, element, mid+1, end)

array = [ 1,2,4,6,8,9,10, 14, 20, 24, 30]
element = 6
print (BinarySearch(array, element,0, len(array)))
********************************************************************
