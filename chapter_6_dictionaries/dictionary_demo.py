"""
Dictionary 
    - allows you connect pieces of related information .
    - Nesting 
        - dictionary inside a list 
        - list inside a dictionary
        - dictionary inside a dictionary 

Python dictionary 
    - a dictionary in python is collection of key-value pairs 
    - each key is connected to a value . you can use key to access the value .
    - a key's value can be string, number , list , or another dictionary 
    - you can use any object that you can create in python as a value in dictionary 
    - every key is associated to value by ':' 
    - individual key-value pairs are seperated by ','

Accessing Value in a dictioanary 
    - dictionary_name[<key_name>]

Adding New key-value Pairs 
    - dictionary are dynamic structures 
    - you can add new key value pairs at any time 
    - dictionary  with new_key name wrapped in square brackets along with new value 

Creating empty dictionary 
    - <dictionary_name> = {}

Modifying value in the dictionary 
    - alien_0['color'] = 'green'

Removing a key-value pairs 
    - del alien_0['color']

using get to to access the dictionary element
    - alien_0 = {'color': 'green', 'speed':'slow'}
    - print(alien_0['x_pos']) # Throws key-error
    - print(alien_0.get('x_pos','This key does not exist !'))
    - If you 
"""

import os 
os.system('clear')

# Simple Dictioanary 
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# adding the new element to dictionary 
alien_0['x_position'] = 25
alien_0['y_position'] = 0
print(f'alien_0 : {alien_0}')
print(type(alien_0))


print(f"\nOriginal dictionary :{alien_0}")
del alien_0['color']
print(f"After removing the color key value pair :{alien_0}\n")

# using the del to access element
alien_0 = {'color': 'green', 'speed':'slow'}
#print(alien_0['x_pos']) # Throws key-error
print(alien_0.get('x_pos','This key does not exist !'))