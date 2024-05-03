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

positional arguments
    - order matters in the positional arguments

keyword arguments
    - A keyword argument is name-value pair that you pass to a function 
    - Order of keyword arguments does not matter 
    - Positional argument follows keyword argument

default values 
    - When defining a function we can define a default value to arguments 
    - when you use default values , any parameter with default value needs to be listed after all the parameter that don't have default value .
    - This allows python to continue iterpreting positional arguments correctly 

equivalent function calls 
    - Since you can use multiple combination of the positional , keyword parameters 
    - There are multiple ways you can call a function 

avoiding arguments errors 
    - unmatched arguments - when you provide fewer or more arguemts than a function needs to do its work.

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
def describe_pet(animal_type,pet_name):
    """ Displays the pet information."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet('dog','charu')

# Using the keyword argument
describe_pet(animal_type='cat',pet_name='lily')

# defualt values 
def describe_pet(pet_name,animal_type='dog'):
    """ Displays the pet information."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('charu','wolf')
describe_pet('charu')
