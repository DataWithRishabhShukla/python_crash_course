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
    - If you don't define the mesage it will return None .

Looping through dictionary :
    - dict.items()
    - dict.keys()  is default behaviour . 
IMP      - [for key in dict.keys()] is same as [for key in dict] 
    - dict.values()
    - looping in an order 
        - sorted(dict.keys())
        - for name in sorted(favorite_laguage):

list -> []
tuple -> ()
dictianary -> {}
set -> {}

set 
    - can be defined using {}
    - contains only unique value 
    - you use set() function also to creare set 
    - Unlike list and dictionaries , sets do not maintain element in specific order 
    - Both dictiaries and sets use {} ,
        - if it has key-value then dictionary .
        - If it has only values then sets 

      
"""

languages = {'python' ,'c','java','c'}
print(languages)
print(type(languages))


# import os 
# os.system('clear')

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


#looping thorugh dict in particular order

favorite_laguage ={
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

for name in sorted(favorite_laguage):
    print(f'\nName: {name}')
    print(f'Favorite language: {favorite_laguage[name]}')

#Looping thorough the values 

print('Following lagauge have been mentioned !!')
for language in favorite_laguage.values():
    print(language.title())