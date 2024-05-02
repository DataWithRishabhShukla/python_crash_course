"""
Functions
    
    - Functions to display some values 
    - Function to return some values or set of values 
    - Functions in seperate files called modules 

Defining the function 
    - function definition 
    - function parathensis
    - docstring 
    - function body 
    - function call

Passing parameters to a function 

Paremeter Vs Arguements
    - Variable defined in the function definition is call - function parameter
    - When we call the funciton pass value to parameter that is called arguments .

Passing Arguemnts 
    - positional arguments - which needs to be in the same order the parameters were written 
    - keyword arguments    -  where each argumens consists of a variable name and value 
    - list and dictionaries of value 

"""
import os 
os.system('clear')


# defining a simple function
def greet_user():
    """ Function prints hello """
    print('hello')

greet_user()

# function with parameter
def greet_user(user_name):
    """ Display a simple greeting."""
    print(f'Hello ,{user_name.title()}')

greet_user('rishabh')

# positional arguments 
