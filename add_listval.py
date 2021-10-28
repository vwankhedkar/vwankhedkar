class Solution:
    def addTwoNumbers(self, l1, l2):
        if len(l1) != len(l2):
            return -1
        lst = []
        for lst in [l1, l2]:
            self.sort(lst)
            print(lst)

        for i in range(len(l1)):
            lst[i] = l1[i] + l2[i]
        return lst

    def sort(self, lst):
        for i in range(len(lst)-1):
            for j in range(len(lst)-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        
s = Solution()
l1 = [5, 6, 4, 8]
l2 = [3, 1, 7, 2]
print(s.addTwoNumbers(l1, l2))
# print(s.sort(l1, l2))
******************************************************************
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

        
def printList(nodeStart):
    print(nodeStart.val)
    if nodeStart.next == None:
        return
    else:
        printList(nodeStart.next)

class Solution(object):
    def addTwoNumbers(self, l1, l2):
            
        if l1 == None:
            return l2
            
        if l2 == None:
            return l1
            
        sval = l1.val + l2.val
        if sval < 10:
            ansNode = ListNode(sval)
            ansNode.next = self.addTwoNumbers(l1.next, l2.next)
            return ansNode
        else:
            rval = l1.val + l2.val-10
            ansNode = ListNode(rval)
            ansNode.next = self.addTwoNumbers(ListNode(1), self.addTwoNumbers(l1.next, l2.next))
            return ansNode
   *******************************************************************************************
  # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        carry = 0
                
        while l1 or l2 or carry:            
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            carry, out = divmod(val1+val2 + carry, 10)    
                      
            result_tail.next = ListNode(out)
            result_tail = result_tail.next                      
            
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
               
        return result.next
      
   ****************************************************************
  class Solution:
    def addTwoNumbers(self, l1, l2 ,c = 0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10 ) 
        
        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next,l2.next,c)
        return ret
      
