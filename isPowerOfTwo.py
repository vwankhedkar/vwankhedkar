class Solution:
    def isPowerOfTwo(n):
        count = 0
        if n == 0:
            return False
        while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
            count += 1
        return count, True

if(Solution.isPowerOfTwo(31)):
    print('Yes')
else:
    print('No')
if(Solution.isPowerOfTwo(64)):
    print('Yes')
else:
    print('No')
    
OUTPUT :
No
Yes
-------------------------------------------------
import math
def Log2(x):
    return math.log10(x)/math.log10(2)

def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) == math.floor(Log2(n)))

if(isPowerOfTwo(31)):
    print("Yes");
else:
    print("No");
 
if(isPowerOfTwo(64)):
    print("Yes");
else:
    print("No");
----------------------------------------------------------
def isPowerOfTwo(x):
    return (x and (not (x & (x-1))))

if(isPowerOfTwo(31)):
    print("Yes");
else:
    print("No");
 
if(isPowerOfTwo(64)):
    print("Yes");
else:
    print("No");
 --------------------------------------------------------------
OUTPUT:
  No
  Yes
 
