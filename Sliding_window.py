import sys
print "GFG"
# O(n * k) solution for finding
# maximum sum of a subarray of size k
INT_MIN = -sys.maxsize - 1
 
# Returns maximum sum in a
# subarray of size k.
 
 
def maxSum(arr, n, k):
 
    # Initialize result
    max_sum = INT_MIN
 
    # Consider all blocks
    # starting with i.
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
 
        # Update result if required.
        max_sum = max(current_sum, max_sum)
 
    return max_sum
 
 
# Driver code
arr = [1, 4, 2, 10, 2,
       3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))

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
 
