#Convert Key-Value list Dictionary to List of Lists
"""
The original dictionary is : {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
The converted list is : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]
"""


test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

print(f"Orginal dict is: {test_dict}")

final_list = []
for k,v in test_dict.items():
    v.insert(0,k)
    final_list.append(v)

print(f'Final List is :{final_list}')


#Using the list comprehension

print('\n')
print(test_dict)
print([[key]+value for key,value in test_dict.items()])


##################################################################################################################################

#Convert List to List of dictionaries
"""
Input : test_list = [“Gfg”, 3, “is”, 8], key_list = [“name”, “id”] 
Output : [{'name': 'Gfg', 'id': 3}, {'name': 'is', 'id': 8}] 
Explanation : Values mapped by custom key, “name” -> “Gfg”, “id” -> 3.
"""
import os 
os.system('clear')

# initializing lists
test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

# initializing key list 
key_list = ["name", "number"]

res =[]

for x in range(0,len(test_list),2):
    res.append({key_list[0]: test_list[x], key_list[1]: test_list[x+1]})

print(res)

##################################################################################################################################

# Lists of List to Dictionary
"""
The original list is : [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
The mapped Dictionary : {('a', 'b'): (1, 2), ('c', 'd'): (3, 4), ('e', 'f'): (5, 6)}
"""
import os 
os.system('clear')

test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]


# Dictionary in Python Using Loop
op_dict={}
for element in test_list:
    op_dict[tuple(element[:2])] = tuple(element[2:])

print(op_dict)

# Using Dictionary Comprehension
mapped_dict = {tuple(element[:2]): tuple(element[2:]) for element in test_list}
print(mapped_dict)

# Using Dictionary Comprehension - tuple()
mapped_dict = {(element[0],element[1]):tuple(element[2:]) for element in test_list}
print(mapped_dict)

##################################################################################################################################

#Python – Convert List of Dictionaries to List of Lists

"""
Input: test_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}] 
Output : [['Gfg', 'best'], [123, 10], [51, 7]] 

Input : test_list = [{'Gfg' : 12}] 
Output : [['Gfg'], [12]]

Explanation: In This, we are converting list of dictionaries to list of lists in Python.
"""

import os 
os.system('clear')

test_list = [{'Gfg': 123, 'best': 10}, {'Gfg': 51, 'best': 7}]
#test_list = [{'Gfg' : 12}] 

print([element for element in test_list])

print('\n')
print([[keys for keys in test_list[0].keys()], *[list(element.values()) for element in test_list]])
print([[keys for keys in test_list[0].keys()], [list(element.values()) for element in test_list]])