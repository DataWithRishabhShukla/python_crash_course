"""
Functions

Passing Arbitrary number of arguments 
    - Sometimes you won't know ahead of time how many arguments a fucntion needs to accept .
      Fortunetaly , Python allows a function to collect and arbitrary number of 
      arguments from the calling statement.
    
    - The * asterisk in the parameter name *toppings tells python to make a tuple called 
    toppings , containing all the values this function recieves 
"""
import os 
os.system('clear')

def make_pizza(*toppings):
    """ Printing the list of things that have been requested."""
    print(f"Making a pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('mushroom', 'corn', 'paneer')