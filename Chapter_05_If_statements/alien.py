
import os 
os.system('clear')
alien_color = 'red'

if alien_color =='red' :
    print("You've earned 5 points.")

requested_toppings = ['mushroom','corn']

if requested_toppings :
    for toppings in requested_toppings:
        print(f'Adding {toppings} to your pizza.')
    print('\nFininshed making your pizza !')
else :
    print('Are you sure you want empty pizza ?')