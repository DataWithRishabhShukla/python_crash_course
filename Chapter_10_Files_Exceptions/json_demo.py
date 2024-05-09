"""
Json module 

json.dumps():
    - This function takes one arguments: a piece of data that should be converted to the json format.
    - The function returns a string, which can be written to a data file.

json.loads()
    - Takes the one arguments -  json formatted string .
    - Returns a python object - (in this case list).
"""

import os
import json
from pathlib import Path

os.system('clear')

numbers = [1,2,3,4,5,6]
base_path = "/Users/rishabhshukla/git_projects/python_crash_course/Chapter_10_Files_Exceptions/"

content = json.dumps(numbers)
print(type(content))
print(content)

path = Path(base_path+"json_dump.json")
path.write_text(content)


#Reading from a json file 
import json
from pathlib import Path
import os 

os.system('clear')

path = Path(base_path+'json_dump.json')
data = path.read_text()
print(data)
print(type(data))

numbers = json.loads(data)
print(numbers)
print(type(numbers))