"""
Functions

Return Value 
    - A function can return a value or set of value 

returning a simple vlaue 
    - return 'hello'

making an arrgument optional 
    - give the defualt value to the some parameters

returning a dictionary 
    - 
"""
import os
os.system('clear')

def get_formatted_name(first_name,last_name):
    """ Returns full name , neatly formatted """
    full_name = f"{first_name} {last_name}"
    return full_name.title()

name = get_formatted_name('rishabh','shukla')
print(name)

# making an argument optional  
def get_formatted_name(fname, lname,mname = ''):
    """ Returns full name , neatly formatted """
    if mname:
        full_name = f"{fname} {mname} {lname}"
    else:
        full_name = f"{fname} {lname}"
    return full_name.title()

print(get_formatted_name('rishabh', 'shukla', 'kumar'))
print(get_formatted_name('rishabh', 'shukla'))

# returning a dictionary
def build_person(first_name, last_name, age=None):
    """ Return a dictionary about person information."""
    person = {'first':first_name, 'last':last_name}
    if age:
        person['age'] = age
    return person

print(build_person('jimmy', 'hendrix'))
print(build_person('jimmy', 'hendrix',30))