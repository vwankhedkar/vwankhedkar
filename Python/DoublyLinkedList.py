class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

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
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()
------------------------------------------------------------------------------------------
Not working 
class Node:
   def __init__(self, val=None, prev=None, next=None, child=None):
      self.val = val
      self.prev = prev
      self.next = next
      self.child = child
   null = None
   def makeLists(lists):
      head = None
      prev = None
      i = 0
      while i < len(lists):
         if lists[i] != None:
            node = Node(val=lists[i], prev=prev)
            if prev is None:
               head = prev = node
            else:
               prev.next = node
               prev = node
            i += 1
         else:
            node = head
            end = False
            while lists[i] == null:
               if node.next is None:
                  end = True
               else:
                  node = node.next
               i += 1
            if end:
               node.child = makeLists(lists[i:])
            else:
               node.prev.child = makeLists(lists[i:])
         break
      return head

   def strLists(head, lsts):
      if head is None:
         return
      nodes = []
      while head:
         nodes.append(str(head.val))
         if head.child is not None:
            nodes.append('|')
            strLists(head.child, lsts)
         head = head.next
      lsts.append(nodes)

   def printList(head):
      lists = []
      Node.strLists(head, lists)
      if lists == []:
         print(None)
         return
      previndent = 0
      for j, l in enumerate(lists[::-1]):
         count = -1
         indent = 0
         s = []
         for i in range(len(l)):
            if l[i] != '|':
               s.append(l[i])
               count += 1
            else:
               indent = count * 4
               child = count
            print('---'.join(s))
            if len(lists) > 1 and j < len(lists)-1:
               previndent += indent
               indentation = ''.join([' ']*previndent)
               if len(l[0]) > 1:
                  indentation += ''.join('' * child)
               print(indentation + '|')
               print(indentation, end='')

   def checkLinks(head, lists=None):
      if head is None:
         return True
      if lists is None:
         lists = []
      stack = []
      result = True
      node = head
      while node is not None:
         if node.child is not None:
            checkLinks(node.child, lists)
         stack.append(node)
         prev = node
         node = node.next
      while prev is not None:
         if len(stack) == 0 or stack.pop() != prev:
            result = False
         prev = prev.prev
      lists.append(result)
      return all(lists) 

lists = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
head = Node.makeLists(lists)
Node.printList(head)
print(Node.checkLinks(head))
