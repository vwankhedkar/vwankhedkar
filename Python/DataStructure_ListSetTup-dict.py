cities = ["Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai"]
cities.append("Bangalore")
print(cities)
cities.insert(1,"Pune")
print(cities)
cities.remove("Pune")
print(cities)
cities.pop(2)
print(cities.index("Mumbai"))
print(cities)
print(cities.count("Mumbai"))
cities.sort()
print(cities)
cities.reverse()
print(cities)
new_cities=cities.copy()
print(cities)
print(new_cities)
updatedlist = new_cities.clear()
print(updatedlist)

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
['Delhi', 'Mumbai', 'Melbourn', 'Sydney', 'Kolkata', 'Mumbai', 'Bangalore']
['Delhi', 'Pune', 'Mumbai', 'Melbourn', 'Sydney', 'Kolkata', 'Mumbai', 'Bangalore']
['Delhi', 'Mumbai', 'Melbourn', 'Sydney', 'Kolkata', 'Mumbai', 'Bangalore']
1
['Delhi', 'Mumbai', 'Sydney', 'Kolkata', 'Mumbai', 'Bangalore']
2
['Bangalore', 'Delhi', 'Kolkata', 'Mumbai', 'Mumbai', 'Sydney']
['Sydney', 'Mumbai', 'Mumbai', 'Kolkata', 'Delhi', 'Bangalore']
['Sydney', 'Mumbai', 'Mumbai', 'Kolkata', 'Delhi', 'Bangalore']
['Sydney', 'Mumbai', 'Mumbai', 'Kolkata', 'Delhi', 'Bangalore']
None

****************************************************************************************************************
demo_set1 = {10,20,20,30,40,30,40}
demo_set2 = {10,20,"30",40,45.5}
demo_set3 = {"10","30"}
demo_set4 = {45,45,67,60,50}
print(demo_set1)
print(set(demo_set4))
print(len(demo_set4))
print(20 in demo_set1)
print("10" in demo_set1)
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
{40, 10, 20, 30}
{50, 67, 60, 45}
4
True
False
*****************************************************************************************************************

demo_set1 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai"}
demo_set2 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai", "NewYork", "California"}

demo_set1.add("Gold Coast")
print(demo_set1)
demo_set1.remove("Mumbai")   # will return error if element not present
print(demo_set1)
demo_set1.discard("Delhi")  # will discard if element is present no error
print(demo_set1)
demo_set1.pop()
print(demo_set1)
demo_set3 = demo_set1.union(demo_set2)
print(demo_set3)
demo_set1.update(demo_set2) # do not update in new set update in set1 only
print(demo_set1)
demo_set4 = demo_set1.intersection(demo_set2)
print(demo_set4)
demo_set1.intersection_update(demo_set2)
print(demo_set1)
demo_set1 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai"}
demo_set2 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai", "NewYork", "California"}
demo_set5 = demo_set1.symmetric_difference(demo_set2)
print(demo_set5)
demo_set1.symmetric_difference_update(demo_set2)
print(demo_set1)
demo_set1 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai", "NewYork", "California"}
demo_set6 = demo_set2.difference(demo_set1)
print(demo_set6)
demo_set2.difference_update(demo_set1)
print(demo_set2)
demo_set1 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai", "NewYork", "California"}
demo_set7 = demo_set1.issubset(demo_set2)
print(demo_set7)
demo_set7 = demo_set1.issuperset(demo_set2)
print(demo_set7)

C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
{'Gold Coast', 'Sydney', 'Kolkata', 'Melbourn', 'Mumbai', 'Delhi'}
{'Gold Coast', 'Sydney', 'Kolkata', 'Melbourn', 'Delhi'}
{'Gold Coast', 'Sydney', 'Kolkata', 'Melbourn'}
{'Sydney', 'Kolkata', 'Melbourn'}
{'California', 'NewYork', 'Melbourn', 'Delhi', 'Sydney', 'Kolkata', 'Mumbai'}
{'California', 'NewYork', 'Melbourn', 'Delhi', 'Sydney', 'Kolkata', 'Mumbai'}
{'California', 'NewYork', 'Melbourn', 'Delhi', 'Sydney', 'Kolkata', 'Mumbai'}
{'California', 'NewYork', 'Melbourn', 'Delhi', 'Sydney', 'Kolkata', 'Mumbai'}
{'California', 'NewYork'}
{'California', 'NewYork'}
{'California', 'NewYork'}
{'California', 'NewYork'}
True
False
***************************************************************************************************************************
demo_tuple1 = (1,2,3,4)
demo_tuple2 = ("Delhi", "Mumbai", "Melbourn", "Sydney", "Kolkata", "Mumbai") #allow duplicates
demo_tuple3 = (True,False,True,False)
demo_tuple4 = (True,1,"Delhi",23.56)
print(demo_tuple1[0])
# print(demo_tuple1.append("abc")) # cant update AttributeError: 'tuple' object has no attribute 'append'
print(len(demo_tuple1))
print(type(demo_tuple1))
print(demo_tuple2[1:4])
print(demo_tuple2.count("Mumbai"))
print(demo_tuple2.index("Sydney"))
for x in demo_tuple1:
    print(x)
join = demo_tuple1 + demo_tuple2 + demo_tuple3
print(join)
print(type(join))
print(demo_tuple2[-1])
OUTPUT
1
4
<class 'tuple'>
('Mumbai', 'Melbourn', 'Sydney')
2
3
1
2
3
4
(1, 2, 3, 4, 'Delhi', 'Mumbai', 'Melbourn', 'Sydney', 'Kolkata', 'Mumbai', True, False, True, False)
<class 'tuple'>
Mumbai
**********************************************************************************************************************
demo_dict1 = {}
demo_dict1 = {1:20, 2:30, 3:40, 4:67}
demo_dict2 = {"qa":"testurl", "uat":"uaturl"}
demo_dict3 = {'qa':34, 3:"uaturl"}
print(type(demo_dict1))
print(demo_dict1[1])
print(demo_dict2['uat'])
demo_dict2['prod']='produrl'
print(demo_dict2)
demo_dict2[1]=56
print(demo_dict2)
demo_dict2.pop(1)
print(demo_dict2)
C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\venv\Scripts\python.exe C:\Users\VWankhedkar\PycharmProjects\Practise-Proj\sel.py 
<class 'dict'>
20
uaturl
{'qa': 'testurl', 'uat': 'uaturl', 'prod': 'produrl'}
{'qa': 'testurl', 'uat': 'uaturl', 'prod': 'produrl', 1: 56}
{'qa': 'testurl', 'uat': 'uaturl', 'prod': 'produrl'}
*************************************************************************************************
demo_dict1 = {"qa":"testurl", "uat":"uaturl", "Prepod":"Prepodurl"}
demo_dict2 = {"qa":"testurl", "uat":"uaturl", "Prepod":"Prepodurl"}
print(demo_dict2.get("qa"))
print(demo_dict2.keys())
print(demo_dict2.values())
print(demo_dict2.items())
print(demo_dict2.pop("uat"))
print(demo_dict2.popitem())
demo_dict2.update({"prod":"produrl"})
print(demo_dict2)
demo_copy = demo_dict2.copy()
print(demo_dict2)
print(demo_copy)
demo_copy.clear()
print(demo_copy)
OUTPUT
testurl
dict_keys(['qa', 'uat', 'Prepod'])
dict_values(['testurl', 'uaturl', 'Prepodurl'])
dict_items([('qa', 'testurl'), ('uat', 'uaturl'), ('Prepod', 'Prepodurl')])
uaturl
('Prepod', 'Prepodurl')
{'qa': 'testurl', 'prod': 'produrl'}
{'qa': 'testurl', 'prod': 'produrl'}
{'qa': 'testurl', 'prod': 'produrl'}
{}
*****************************************************************************
list_of_dicts = [{'name': 'John', 'age': 30}, {'name': 'Jane','age': 25}, {'name': 'Bob', 'age': 35}]
sorted_list = sorted(list_of_dicts, key=lambda x:x['age'])
print("Sorted list of dictionaries : ", sorted_list)
Sorted list of dictionaries :  [{'name': 'Jane', 'age': 25}, {'name': 'John', 'age': 30}, {'name': 'Bob', 'age': 35}]
**************************************************************************************
lst, dct, tup = [], {}, ()
print(bool(lst), bool(dct), bool(tup))
lst, dct, tup = [0], {'a':1}, (1,)
print(bool(lst), bool(dct), bool(tup))
lst, dct, tup = [0.0], {'a':1.0}, (1.0,)
print(bool(lst), bool(dct), bool(tup))
a,b,c=0,3.14,'Hello Program'
print(bool(lst), bool(dct), bool(tup))
statement = None
print(bool(None))
true = True
print(bool(true))
False False False
True True True
True True True
True True True
False
True
**************************************************************************************
**************************************************************************************
**************************************************************************************
**************************************************************************************
**************************************************************************************

