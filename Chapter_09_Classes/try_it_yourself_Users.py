import os 
os.system('clear')

class User:
    """ A simple attempt to model user."""

    def __init__(self, first_name, last_name):
        """ Intialize the attributes first_name, last_name"""
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        """ Displays the detials about the user."""
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")
    
    def greet_user(self):
        """ Greets the user."""
        print(f"Welcome {self.first_name.title()}!!")
    

user_1 = User('Rishabh', 'Shukla')
user_1.describe_user()
user_1.greet_user()