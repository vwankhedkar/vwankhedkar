# defining a function with variable number of arguments
def arguments(*args, **kwargs):
    print("Positional arguments: (args) :")
    for arg in args:
        print(arg)

    print("\nKeyword arguments (kwargs) :")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Passing normal arguments and key-word arguments in the function test.
arguments(1,2,3, name="abc", age=30, city="New York")
OUTPUT
Positional arguments: (args) :
1
2
3

Keyword arguments (kwargs) :
name: abc
age: 30
city: New York
**************************************************************************
from copy import copy, deepcopy
l1 = [1, 2, [3, 5], 4]
# Shallow copy
l2 = copy(l1)
l2[3] = 7
l2[2].append(6)
print(l2)
print(l1)

# Deep copy
l3 = deepcopy(l1)
l3[3] = 8
l3[2].append(7)
print(l3)
print(l1)
OUTPUT
[1, 2, [3, 5, 6], 7]
[1, 2, [3, 5, 6], 4]
[1, 2, [3, 5, 6, 7], 8]
[1, 2, [3, 5, 6], 4]
