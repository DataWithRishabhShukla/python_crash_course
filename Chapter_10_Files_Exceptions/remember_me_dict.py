import json,os
from pathlib import Path

os.system('clear')

# Reading from the json 
path = Path(os.getcwd()+'/Chapter_10_Files_Exceptions/'+'user_info.json')
content = path.read_text()

data = json.loads(content)
print(data)
print(type(data))

user_info = {}
print(os.getcwd())

name = input("Please enter your name: ")
fav_city = input("Please enter your favorite city: ")
age = int(input("Please enter your age: "))

user_info['name'] = name
user_info['favorite_city'] = fav_city
user_info['age'] = age

print(user_info)

content = json.dumps(user_info)
print(content)
print(type(content))

path = Path(os.getcwd()+'/Chapter_10_Files_Exceptions/'+'user_info.json')
path.write_text(content)
