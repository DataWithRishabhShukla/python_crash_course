"""
List:

    A list is collection of items in a particular order.
    Since list mostly contains more than one element . It is good practise to name it plurals .  items , names .

Accessing a list :
    Using a index , starts with 0 []
    You can use the -ve index . -1 represents the last element .

Modifying , Adding and Removing Elements :
    Modifying -> Same as accessing the element
    
    Adding 
        At the end using the append function . motorcycles.append('ducati')
        At any location we can do using . motorcycles.insert(0,'hero') . This will shift all the elements to the right .

    Remove
        Using Index : del motorcycles[1] 
        
        Using pop method : This will remove the last element form the list 
            popped_motorcycles = motorcycles.pop()
            We can use index with pop to remove the items from the list.
        
        Remove using the value :
            motorcycles.remove('ducati')
            Gives error if element is not present in the list .
            Also removes only the first occurance of the element.


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

# Modifying

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'bajaj'
print(motorcycles)

# Adding 

motorcycles.append('ducati')
print(motorcycles)


motorcycles.insert(0,'hero')
print(motorcycles)


# Removing Element
print(motorcycles)
del motorcycles[1]
print(motorcycles)

# pop without index 
os.system('clear')
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

# pop with index 
os.system('clear')
motorcycles = ['honda','yamaha','suzuki']

first_motorcycle = motorcycles.pop(1)
print(f'First motorcycle which I owned was: {first_motorcycle.title()}')

# Removing using value 
os.system('clear')
motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
if too_expensive in motorcycles:
    motorcycles.remove(too_expensive)
    print(f'{too_expensive.title()} is too expensive for me !!')
print(motorcycles)