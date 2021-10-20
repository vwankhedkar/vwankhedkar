class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        listr = ''

        while(itr):
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

if __name__ == '__main__':
    ll = Linked_list()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(6)
    ll.print()
    ll.insert_at_end(55)
    ll.insert_at_end(66)
    ll.print()
    ll.insert_values(["Banana", "Mango", "Grapes", "Orange"])
    ll.print()
