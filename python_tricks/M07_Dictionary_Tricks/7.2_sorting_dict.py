"""
Sorting dictionary for fun and profit:
    - sort based on the keys or values or some derived properties
    - 
    sorted(xs.items(), key= lambda x: x[0])
    sorted(xs.items(), key= lambda x: x[1])
    sorted(xs.items(), key= lambda x: x[1], reverse= True )




"""
import os 
os.system('clear')

xs = {'a': 4, 'b': 4, 'd': 2, 'c': 6}

# Sorting based on the key/value pair
print(sorted(xs.items()))

# Converting it back to dictionary 
print(dict(sorted(xs.items())))

# Sorting based on the key 
print(sorted(xs.items(), key= lambda x: x[0]))

# Sorting based on the values
print(sorted(xs.items(), key= lambda x: x[1]))

# Sorting based on the values but in reverse order 
print(sorted(xs.items(), key= lambda x: x[1], reverse= True ))
