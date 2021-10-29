# Python3 implementation of the approach
class Block:
     
    # A block has two elements
    # as components  (i.e. value and localMax)
    def __init__(self, value, localMax):
        self.value = value
        self.localMax = localMax
 
class Stack:
    def __init__(self, size):
         
        # Setting size of stack and
        # initial value of top
        self.stack = [None] * size
        self.size = size
        self.top = -1
 
    # Function to push an element
    # to the stack
    def push(self, value):
 
        # Don't allow pushing elements
        # if stack is full
        if self.top == self.size - 1:
            print("Stack is full")
        else:
            self.top += 1
             
            # If the inserted element is the first element
            # then it is the maximum element, since no other
            # elements is in the stack, so the localMax
            # of the first element is the element itself
            if self.top == 0:
                self.stack[self.top] = Block(value, value)
 
            else:
                 
                # If the newly pushed element is less
                # than the localMax of element below it,
                # Then the over all maximum doesn't change
                # and hence, the localMax of the newly inserted
                # element is same as element below it
                if self.stack[self.top - 1].localMax > value:
                    self.stack[self.top] = Block(
                        value, self.stack[self.top - 1].localMax)
 
                # Newly inserted element is greater than
                # the localMax below it, hence the localMax
                # of new element is the element itself
                else:
                    self.stack
                    self.stack[self.top] = Block(value, value)
                     
            print(value, "inserted in the stack")
             
    # Function to remove an element 
    # from the top of the stack         
    def pop(self):
         
        # If stack is empty
        if self.top == -1:
            print("Stack is empty")
 
        # Remove the element if the stack
        # is not empty
        else:
            self.top -= 1
            print("Element popped")
             
    # Function to find the maximum 
    # element from the stack 
    def max(self):
         
        # If stack is empty
        if self.top == -1:
            print("Stack is empty")
        else:
             
            # The overall maximum is the local maximum
            # of the top element
            print("Maximum value in the stack:",
                  self.stack[self.top].localMax)
 
# Driver code
 
# Create stack of size 5
stack = Stack(5)
stack.push(2)
stack.max()
stack.push(6)
stack.max()
stack.pop()
stack.max()
*******************************************************
# Python program for tha above approach
 
# Function to split the array into K
# subarrays such that the sum of
# maximum of each subarray is maximized
def partitionIntoKSegments(arr, N, K):
    # If N is less than K
    if (N < K):
        print(-1)
        return
    # Map to store the K
    # largest elements
    mp = {}
 
    # Auxiliary array to
    # store and sort arr[]
    temp = [0]*N
 
    # Stores the maximum sum
    ans = 0
 
    # Copy arr[] to temp[]
    for i in range(N):
        temp[i] = arr[i]
 
    # Sort array temp[] in
    # descending order
    temp = sorted(temp)[::-1]
 
    # Iterate in the range [0, K - 1]
    for i in range(K):
        # Increment sum by temp[i]
        ans += temp[i]
 
        # Increment count of
        # temp[i] in the map mp
        mp[temp[i]] = mp.get(temp[i], 0) + 1
 
    # Stores the partitions
    P = []
 
    # Stores temporary subarrays
    V = []
 
    # Iterate over the range [0, N - 1]
    for i in range(N):
        V.append(arr[i])
 
        # If current element is
        # one of the K largest
        if (arr[i] in mp):
 
            mp[arr[i]] -= 1
            K -= 1
 
            if (K == 0):
                i += 1
                while (i < N):
                    V.append(arr[i])
                    i += 1
            # print(V)
 
            if (len(V) > 0):
                P.append(list(V))
                V.clear()
 
    # Print ans
    print(ans)
 
    # Print partition
    for u in P:
        for x in u:
            print(x,end=" ")
        print()
# Driver code
if __name__ == '__main__':
    # Input
    A = [5, 3, 2, 7, 6, 4]
    N = len(A)
    K = 3
 
    # Function call
    partitionIntoKSegments(A, N, K)
