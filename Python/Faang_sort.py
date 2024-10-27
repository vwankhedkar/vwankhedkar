Bubble Sort :
def BubbleSort(numbers):
    lng = len(numbers)
    for i in range(lng):
        for j in range(lng-1):
            if numbers[j] > numbers[j+1]:
                tmp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = tmp
    return numbers
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(BubbleSort(numbers))
----------------------------------------------------
Selection Sort :
def selectionSort(numbers):
    lng = len(numbers)
    for i in range(lng):
        min = i
        tmp = numbers[i]
        for j in range(i+1, lng):
            if numbers[j] <= numbers[min]:
                min = j
        numbers[i] = numbers[min]
        numbers[min] = tmp
    return numbers
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selectionSort(numbers))
----------------------------------------------------
def insertionSort(numbers):
    lng = len(numbers)
    for i in range(lng):
        anchor = numbers[i]
        j = i-1
        while j >= 0 and anchor < numbers[j]:
            numbers[j+1] = numbers[j]
            j = j - 1
        numbers[j+1] = anchor
    return numbers
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(insertionSort(numbers))
-------------------------------------------------
def mergeSort(arr):
    if len(arr) > 1:
  
         # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        # Sorting the first half
        mergeSort(L)
  
        # Sorting the second half
        mergeSort(R)
  
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
# Code to print the list
    return numbers 
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(mergeSort(numbers))
---------------------------------------------------
def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

def quicksort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quicksort(elements, start, pi-1)
        quicksort(elements, pi+1, end)

def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
    
        while elements[end] > pivot:
            end -= 1
        
        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)
    return end

if __name__ == '__main__':
    elements = [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    quicksort(elements, 0, len(elements)-1)
    print(elements)
----------------------------------------------------
OUTPUT : [0, 1, 2, 4, 5, 6, 44, 63, 87, 99, 283]
----------------------------------------------------
