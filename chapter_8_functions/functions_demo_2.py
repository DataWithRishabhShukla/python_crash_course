"""
Functions

Return Value 
    - A function can return a value or set of value 

returning a simple vlaue 
    - return 'hello'

making an arrgument optional 
    - give the defualt value to the some parameters

returning a dictionary 
    - return <dictionar_name>

Passing a List

Modifying a list 
    - When you pass list as arguments to function it will get full access to the list 
    - It can modify the list 
    - def print_models(unprinted_models, completed_models):

Preventing a function from modifying list 
    - In here instead of passing a list you can pass a copy of the list 
    - While calling the function you can pass the copy of the list instead of orginal list 
    - Using "list_name[:]"
    - print_models(unprinted_models[:], completed_models):
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

# Passing a List 
def greet_user(user_names):
    """ Prints a simple greetings to each user in the list."""
    for name in user_names:
        print(f"Hello, {name.title()}!")

users = ['rishabh','ayush','charu']
greet_user(users)


# Modifying a list
def print_models(unprinted_models, completed_models):
    """ Simulate printing each design until none are left."""
    print('\n\n')
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model: {current_model}")
        completed_models.append(current_model)

def display_models(completed_model):
    """ Displays models in the list."""
    print(f"\nFollowing models have been printed: ")
    for model in completed_model:
        print(model)
    
unprinted_design = ['phone case','robot','dodo']
completed_model = []
print_models(unprinted_design,completed_model)
display_models(completed_model)

# Modifying a list
def print_models(unprinted_models, completed_models):
    """ Simulate printing each design until none are left."""
    print('\n\n')
    while unprinted_models:
        current_model = unprinted_models.pop()
        print(f"Printing model: {current_model}")
        completed_models.append(current_model)

unprinted_design = ['phone case','robot','dodo']
print_models(unprinted_design[:],completed_model)
print(unprinted_design)
