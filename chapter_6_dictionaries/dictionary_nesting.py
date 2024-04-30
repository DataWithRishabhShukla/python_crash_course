"""
Nesting of dictionary:
    - mutilple dictionary in a list 
    - list of items in a dictionary 
    - dictionary inside a dictionary

List of dictionary 
    [{'color': 'green', 'points': 5, 'speed': 'slow'}, {'color': 'green', 'points': 5, 'speed': 'slow'}]

List in dictionary 
    - you can nest list inside a dictionary when you more than value to be associated with a key.
    - favorite_laguage ={
        'rishabh':['python','java'],
        'charu':['c++','go']
    }
Dictionary in dictionary

"""

# dictionary in a dictionary
import os , time
os.system('clear')

users ={
    'rshuk3':{
        'first': 'rishabh',
        'last': 'shukla' ,
        'location': 'mumbai'
    },
    'charu3':{
        'first': 'charu',
        'last': 'sharma',
        'location':'delhi'
    }
}

for username, user_info in users.items():
    print(f'UserName: {username}')
    full_name = user_info['first'] +' ' +user_info['last']
    location = user_info['location']

    print(f'\nFull name : {full_name}')
    print(f'Location :{location}')




time.sleep(30)
print('***********************************************************************************************')
import os 
os.system('clear')

# List inside a dictionary
# store the information of the pizza ordered 
pizza = {
    'crust': 'cheese_burst',
    'toppings': ['mushroom','corn','paneer'],
}

# summerize the order 
print(f"You ordered {pizza['crust']} crust pizza . With following toppings")

for topping in pizza['toppings']:
    print(topping)

import time
time.sleep(30)


print('***********************************************************************************************')
import os 
os.system('clear')

#making empty list for storing alien
aliens = []

#createing 30 alien
for alien_numbner in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)

#show first 5 alien 
print(aliens[:5])


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'fast'


for alien in aliens:
    print(alien)
