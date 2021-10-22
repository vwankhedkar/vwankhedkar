from typing import Counter


class Node:
    def __init__(self, data=None, next=None, pos=None):
        self.data = data
        self.next = next
        self.pos = pos

class linked_list:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        listr = ''

        while(itr):
            listr += str(itr.data) + '-->'
            itr = itr.next
        print(listr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while(itr.next):
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count
        
if __name__ == '__main__':
    ll = linked_list()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(11)
    ll.print()
    ll.insert_at_end(33)
    ll.insert_at_end(44)
    ll.print()
    ll.insert_values(["Banana", "Mango", "Grapes", "Orange", "Jackfruit", "Mosambi"])
    ll.print()
    ll.insert_at(1,"blueberry")
    ll.print()
    ll.get_length()
    ll.remove_at(2)
    ll.print()
    ll.insert_values([45,7,12,567,99])
    ll.insert_at_end(67)
    ll.print()
