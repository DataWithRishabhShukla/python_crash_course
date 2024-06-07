"""
Dictionary pretty printing 

    - using str
    - using json.dumps
    - using pprint 

json function 
    - dump  - This function is used to serialize a Python object into a JSON file. It takes two parameters: the Python object to be serialized and the file object where the JSON data will be written. 
    - dumps - This function is used to serialize a Python object into a JSON string. It takes one parameter: the Python object to be serialized. 
    - loads - This function reads the JSON data from a file-like object and parses it into a Python object.

"""
import os 
os.system('clear')

mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(str(mapping))

import json 
print(json.dumps(mapping, indent=4, sort_keys= True))

from pprint import pprint as pp
pp(mapping)


# Open the JSON file
with open('data.json', 'r') as file:
    # Load the JSON data into a Python object
    data = json.load(file)

# Access the data
print(data)

