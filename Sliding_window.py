def maxSum(arr, n, k):
    max_sum = 0
    current_sum = 0
    lst = []
    for i in range(n - k + 1):
        current_sum = 0
        lst.clear()
        for j in range(k):
            current_sum = current_sum + arr[i + j]
            lst.append(arr[i+j])
        max_sum = max(current_sum, max_sum)
    return max_sum, lst
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(f"Maximum sum with {k} elements is : ", maxSum(arr, n, k))
Maximum sum with 4 elements is :  (24, [3, 1, 0, 20])   
*********************************************************
# O(n) solution for finding
# maximum sum of a subarray of size k
 
 
def maxSum(arr, k):
    # length of the array
    n = len(arr)
 
    # n must be greater than k
    if n < k:
        print("Invalid")
        return -1
 
    # Compute sum of first window of size k
    window_sum = sum(arr[:k])
 
    # first sum available
    max_sum = window_sum
 
    # Compute the sums of remaining windows by
    # removing first element of previous
    # window and adding last element of
    # the current window.
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum
 
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))

*************************************************
# Python program to find the maximum for
# each and every contiguous subarray of
# size k
 
# Method to find the maximum for each
# and every contiguous subarray of s
# of size k
def printMax(arr, n, k):
    max = 0
   
    for i in range(n - k + 1):
        max = arr[i]
        for j in range(1, k):
            if arr[i + j] > max:
                max = arr[i + j]
        print(str(max) + " ", end = "")
 
# Driver method
if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3
    printMax(arr, n, k)
***************************************************
def printKMax(a, n, k):
     
    # If k = 1, prall elements
    if (k == 1):
        for i in range(n):
            print(a[i], end=" ");
        return;
         
    # Using p and q as variable pointers
    # where p iterates through the subarray
    # and q marks end of the subarray.
    p = 0;
    q = k - 1;
    t = p;
    max = a[k - 1];
 
    # Iterating through subarray.
    while (q <= n - 1):
 
        # Finding max
        # from the subarray.
        if (a[p] > max):
            max = a[p];
        p += 1;
 
        # Printing max of subarray
        # and shifting pointers
        # to next index.
        if (q == p and p != n):
            print(max, end=" ");
            q += 1;
            p = t + 1;
            t = p;
 
            if (q < n):
                max = a[q];
 
# Driver Code
if __name__ == '__main__':
    a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
    n = len(a);
    K = 3;
 
    printKMax(a, n, K);
 **************************************************
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

 
