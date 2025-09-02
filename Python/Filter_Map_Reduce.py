numbers = [1, 2, 3, 4, 5, 6 ]
sqr = map(lambda x:x**2, numbers)
print(list(sqr))

even_num = filter(lambda x:x%2==0, numbers) 
print(list(even_num))

from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  
[1, 4, 9, 16, 25, 36]
[2, 4, 6]
24
*******************************************************************
list1 = [1,2,3,4,5,6,7,8,9,10]
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

f = list(filter(is_even, list1))
print(f)

OUTPUT   [2, 4, 6, 8, 10]
**********************************************************************
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_obj = map(lambda s:s[0] == 'A', fruit)
print(list(map_obj))
**********************************************************************
from functools import reduce
fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_obj = map(lambda s:s[0] == 'A', fruit)
print(list(map_obj))
filter_obj = filter(lambda s:s[0] == 'A', fruit)
print(list(filter_obj))
reduce_obj = reduce(lambda x,y:x+ " " +y, fruit)
print(reduce_obj)
**********************************************************************
