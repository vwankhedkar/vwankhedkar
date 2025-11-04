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
************************************************************************
# Function to modify mutable object -> list
def modify_list(l):
    l.append(4)
    print("Inside modify list: ", l)

# Function to modify immutable object -> integer
def modify_number(num):
    num += 10
    print("Inside modify number: ", num)

# Passing mutable object
l = [1, 2, 3]
print("Before modify list : ", l)
modify_list(l)
print("After modify list : ", l)

# Passing immutable object
num = 5
print("Before modify number : ", num)
modify_number(num)
print("After modify number : ", num)
OUTPUT
Before modify list :  [1, 2, 3]
Inside modify list:  [1, 2, 3, 4]
After modify list :  [1, 2, 3, 4]
Before modify number :  5
Inside modify number:  15
After modify number :  5
******************************************************************************
def func(**args):
    for key in args:
        print(key,":",args[key])
func(Micoorganism='Aspergillus niger', Substrate='Molasses', Product='Inulinase', Fermentation_mode='Batch', Activity='1800 U/mL')
Micoorganism : Aspergillus niger
Substrate : Molasses
Product : Inulinase
Fermentation_mode : Batch
Activity : 1800 U/mL

******************************************************************************
