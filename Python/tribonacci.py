# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2, n3 = 0, 1, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2 + n3
       # update values
       n1 = n2
       n2 = n3
       n3 = nth
       count += 1

******************************************************************
My solution - 
def tribonacci(signature, n) :
    if n == 0 or n < 1:
        return
    for i in range(2,n-1):
        signature.append(signature[i] + signature[i-1] + signature[i-2]) 
    print(signature)
    

signatures = [[1,1,1], [0, 0, 1], [0, 1, 1], [1, 0, 0], [1, 2, 3], [3, 2, 1], [1, 1, 1], [0.5, 0.5, 0.5]]
for signature in signatures:
    tribonacci(signature, 10)
    print(" ", end = "\n")
******************************************************************
def tribonacci(signature, n) :
    for i in range(3, n):
        signature.append(signature[i-1] + signature[i-2] + signature[i-3]) 
    return signature[:n]
  ******************************************************************
  
def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res
******************************************************************
def tribonacci(signature,n):
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
    
    return signature[:n]
******************************************************************
def tribonacci(s, n):
    for i in range(3, n): s.append(s[i-1] + s[i-2] + s[i-3])
    return s[:n]
******************************************************************
def tribonacci(signature, n):
    output = signature[:n]
    while len(output) < n:
        output.append(sum(output[-3:]))
    return output
  ******************************************************************
  def tribonacci(signature,n):
    result = []
    if n > 3:
        result = signature
        for i in range(0,n-3):
            nextTrib = result[0+i] + result[1+i] + result[2+i]
            print(nextTrib)
            result.append(nextTrib)
    elif n == 3:
        result = signature
    elif n == 2:
        result = [signature[0],signature[1]]
    elif n == 1:
        result = [signature[0]]
    return result
