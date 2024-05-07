import os 
os.system('clear')

class Dog:
    """ A simple attempt to model a dog."""

    def __init__(self, name,age):
        """Intialize the name and age attribute."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting response to a command."""
        print(f"{self.name} is now sitting.")
    
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 2)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()