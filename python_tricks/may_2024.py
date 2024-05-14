

# Merging two dictionaries
print(f"\n\n{'*'*20} Merging two dictionaries {'*'*20}")
def merge_two_dict(x,y):
    return {**x, **y}

x = {'x': 1, 'y': 2}
y = {'a': 10, 'b': 20}

print(merge_two_dict(x,y))

# how to create list using the dict method
z = dict([('v', 30)])
new_dict = dict(c=10,z=120)
print(new_dict)

z = dict(**x,**y)
print(z)

#----------------------------------------------------------------------

# Methods to Flatten a List of Lists in Python
print(f"\n\n{'*'*20} Flatten a List of Lists {'*'*20}")
nested_list = [[1,2,3], [4,5,6], [7,8,9]]

def flatten_list(nested_list):
    """Nested iterator to flatten a nested list."""
    flat_list = []
    [flat_list.extend(element)for element in nested_list]
    return flat_list

print(f'Nested List: {nested_list}')
print(f'Flatten List: {flatten_list(nested_list)}')

