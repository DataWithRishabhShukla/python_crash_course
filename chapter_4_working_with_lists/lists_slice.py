"""
slicing a list 
traversing a subset of list 
copying a list
    list1= list2 -> this will not copy list . It will be second variable pointing to the same list .
"""

import os 
os.system('clear')
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[:-4:-1])


nums = list(range(1,11))
print(nums)
nums.sort(reverse=True)
print(nums)

my_foods = ['pizza','burger','pasta']
friends_food= my_foods[:]

print(f'\nMy food : {my_foods}\n')
print(f'Friends food :{friends_food}\n')

my_foods.append('ice_cream')
friends_food.append('noodles')

print(f'\nMy food : {my_foods}\n')
print(f'Friends food :{friends_food}\n')
