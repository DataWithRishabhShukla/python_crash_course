"""
Functions

Passing Arbitrary number of arguments 
    - Sometimes you won't know ahead of time how many arguments a fucntion needs to accept .
      Fortunetaly , Python allows a function to collect and arbitrary number of 
      arguments from the calling statement.
    
    - The * asterisk in the parameter name *toppings tells python to make a tuple called 
    toppings , containing all the values this function recieves 

Mixing Positional and Arbitrary number
    - def make_pizza(size, *toppings)
    - The parameter that accepts arbitatry number of arguments must be placed 
    last in the function definiton .
    - In the function first value it recieved is assigned to size 
    remaning all are assigned to tuple toppings.
   - you will see generally  *args as arbitrary arguments name 

Using arbitrary keyword arguments 
    - you can write function that accepts as many key-value pairs as the calling statement provides.
    - The definition of build_profile() expects a first and last name and then it allows the user
    to pass in as many name-value pairs as they want . 
    - The ** before the parameter **user_info cause pythont to create a dictionary called 
    user_info containing all the extra name-value pairs the function recieves.
    - you can mix positional , keyword and arbitrary values in many different ways when
      writing your own functions.
    
    - **kwargs - default in many cases 

"""
import os 
os.system('clear')

def make_pizza(*toppings):
    """ Printing the list of things that have been requested."""
    print(f"Making a pizza with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('mushroom', 'corn', 'paneer')

# Mixing Positional and Arbitrary number
def make_pizza(size, *toppings):
    """ Printing the list of things that have been requested."""
    print('\n\n')
    print(type(toppings))
    print(f"Making a pizza of {size}-inch with following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(20,'corn','mushroom')


def build_profile(first_name,last_name , **user_info):
    """ Builds a dictionary contianing all the information about user. """
    user_info['first'] = first_name
    user_info['last'] = last_name

    return user_info

print(f"\n\n User profile :")
print(build_profile('rishabh', 'shukla',company='Atlassian' , year='2024'))