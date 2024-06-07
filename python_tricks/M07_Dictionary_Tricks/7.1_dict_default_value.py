
"""
Dictionary default value 
    - get() proveides us the option of , giving the default value when key does not exist
    - user_names.get(12121, 'Key Not Found') 
"""
import os 
os.system('clear')

user_names = {
    876:'rishabh',
    103:'charu'
}

print(user_names.keys())



print(user_names.get(12121, 'Key Not Found'))

# will throw key error
print(user_names[12121])