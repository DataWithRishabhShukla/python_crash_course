"""
Functions

Return Value 
    - A function can return a value or set of value 

returning a simple vlaue 
    - return 'hello'

making an arrgument optional 
    - give the defualt value to the some parameters
"""

def get_formatted_name(first_name,last_name):
    """ Returns full name , neatly formatted """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name('rishabh','shukla')
print(name)

# Making 