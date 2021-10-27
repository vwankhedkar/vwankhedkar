			Selection Sort
***************************************************************************
def selection_sort(elements):
    size = len(elements)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1, size):
            if elements[j] < elements[min_index]:
                min_index = j
            
        if i != min_index:
            elements[i], elements[min_index] = elements[min_index], elements[i]

if __name__ == '__main__':
    # elements = [72, 3, 66, 1, 9, 21, 45, 67, 72]
    tests = [
        [78, 9, 55, 32, 21],
        [],
        [1, 5, 8, 9],
        [72, 3, 66, 1, 9, 21, 45, 67, 72],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)
***************************************************************************
class selection_sort():
    def __init__(self, elements):
        self.elements = elements

    def selection_sort(self):
        for i in range(len(elements)):
             min = i
             print("Minimum element is: ", min, self.elements)
             print("*************Outer loop -> ", i)
             for j in range(len(elements)-1):
                 print("*************Inner loop -> ", j)
                 if self.elements[j] < self.elements[min]:
                     min = j
                     print("Minium after swap: ", min, self.elements[min])
               
                 if min != i: 
                     self.elements[min], self.elements[i] = self.elements[i], self.elements[min]

if __name__ == '__main__':
    elements = [33, 44, 21, 78, 90, 100, 1, 2, 3]
    s = selection_sort(elements)
    s.selection_sort()
    print(s.elements)
*************************************************************************************************
def selection_sort(arr):
    size = len(arr)
    for i in range(size-1):
        min_index = i
        for j in range(min_index+1,size):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
    for elements in tests:
        selection_sort(elements)
        print(elements)
