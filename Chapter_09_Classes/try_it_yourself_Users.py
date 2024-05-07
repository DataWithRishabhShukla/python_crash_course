import os 
os.system('clear')

class User:
    """ A simple attempt to model user."""

    def __init__(self, first_name, last_name):
        """ Intialize the attributes first_name, last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        """ Displays the detials about the user."""
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")
    
    def greet_user(self):
        """ Greets the user."""
        print(f"Welcome {self.first_name.title()}!!")
    
    def increment_login_attempts(self):
        """Updates the login_attempts attribute."""
        self.login_attempts +=1
    
    def reset_login_attempts(self):
        """ Resets the login_attempts attribute to 0. """
        self.login_attempts = 0
    

user_1 = User('Rishabh', 'Shukla')
user_1.describe_user()
user_1.greet_user()

print(user_1.login_attempts)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)
