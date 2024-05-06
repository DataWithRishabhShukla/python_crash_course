
# Online Python - IDE, Editor, Compiler, Interpreter



myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
        
print(sorted(myDict))
print(sorted(myDict.values()))
print(sorted(myDict.items()))


keys = list(myDict.keys())
print(keys)

sorted_dict = {i:myDict[i] for i in sorted(keys)}
print(sorted_dict)

x, y, z = 10, 20, 30
d = {}

d[x,y,z] = x+y-10
print(d)

d = {'a': 100, 'b':200, 'c':300}
print(sum(d.values()))


#Get Size of dictionary
import sys
print(f"\nSize in Bytes: {sys.getsizeof(d)}")


#Ways to sort list of dictionaries by values in Python – Using lambda function

list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]


print("\nThe list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))
print(sorted(list, key=lambda i:(i['age'],i['name'])))


import os
os.system('clear')

# Merging two Dictionaries

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

print({**dict1,**dict2})
dict1.update(dict2)
print(dict1)