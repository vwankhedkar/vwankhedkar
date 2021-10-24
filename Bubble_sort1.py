class bubble_sort:
    def __init__(self,elements,key):
        self.elements = elements
        self.key = key
    
    def sort(self):
        for i in range(len(self.elements)-1):
            for j in range(len(self.elements)-i-1):
                if (self.elements[j][self.key] > self.elements[j+1][self.key]):
                    self.elements[j][self.key], self.elements[j+1][self.key] = self.elements[j+1][self.key], self.elements[j][self.key]

if __name__ == '__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    b = bubble_sort(elements,key='transaction_amount')
    b.sort()
    print(b.elements)
