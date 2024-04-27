"""
List:

    A list is collection of items in a particular order.
    Since list mostly contains more than one element . It is good practise to name it plurals .  items , names .

Accessing a list :
    Using a index , starts with 0 []
    You can use the -ve index . -1 represents the last element .

    
"""
import os 

os.system('clear')
bicycles = ['trek' , 'cannondale', 'redline', 'specialzed']
print(bicycles)

print(bicycles[0].title())
print(bicycles[2])
print(bicycles[3])

print(bicycles[-1])

message = f'My first bicycle was {bicycles[0].title()}'
print(message)