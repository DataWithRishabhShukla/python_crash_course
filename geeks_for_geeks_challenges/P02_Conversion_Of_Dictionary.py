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

print('\n\n')
print(test_list[::2])
print(test_list[1::2])
print([pair for pair in zip(test_list[::2],test_list[1::2])])