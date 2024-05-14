import os 
os.system('clear')

# Merging two dictionaries
x = {'x': 1, 'y': 2}
y = {'a': 10, 'b': 20}
z= {**x, **y}
print(z)