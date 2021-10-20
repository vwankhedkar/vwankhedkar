***************************************************************************
					Bubble Sort
***************************************************************************
def bubble_sort(elements):
    size = len(elements)
    for j in range(size-1):
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp

if __name__ == '__main__':
    elements = [5, 9, 2, 1, 67, 34, 88, 34]
    # elements = [1, 2, 3, 4]
    # elements = ["mona", "dhaval", "Aamir", "tine", "chang"]

    bubble_sort(elements)
    print(elements)
***************************************************************************
def bubble_sort(elements):
    size = len(elements)
    swapped=True
    while(swapped):
        swapped = False
        for i in range(size-1):
            if elements[i] > elements[i+1]:
                tmp = elements[i]
                elements[i] = elements[i+1]
                elements[i+1] = tmp
                swapped=True

if __name__ == '__main__':
    # elements = [5, 9, 2, 1, 67, 34, 88, 34]
    elements = [1, 2, 3, 4]
    # elements = ["mona", "dhaval", "Aamir", "tine", "chang"]

    bubble_sort(elements)
    print(elements)
***************************************************************************
class bubble_sort:
    def __init__(self,elements):
        self.elements = elements
    
    def sort(self):
        for i in range(len(self.elements)-1):
            for j in range(len(self.elements)-i-1):
                if (self.elements[j] < self.elements[j+1]):
                    self.swap(j, j+1)

    def swap(self, i, j):
        self.elements[i], self.elements[j] = self.elements[j], self.elements[i] 

if __name__ == '__main__':
    elements = [51, 32, 23, 14, 5, 66, 27, 28, 19]
    b = bubble_sort(elements)
    b.sort()
    print(b.elements)
***************************************************************************
# you can use this to sort strings too
def bubble_sort(elements):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    elements = [5,9,2,1,67,34,88,34]
    elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    bubble_sort(elements)
    print(elements)
***************************************************************************
def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size-1):
        swapped = False
        for j in range(size-1-i):
            a = elements[j][key]
            b = elements[j+1][key]
            if a > b:
                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True

        if not swapped:
            break

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort(elements, key='transaction_amount')
    print(elements)
