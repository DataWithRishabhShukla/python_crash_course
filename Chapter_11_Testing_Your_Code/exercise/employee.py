class Employee:
    """A calss to represent employee."""

    def __init__(self, first_name, last_name, sal):
        """Function to initialize the first_name, last_name,sal"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = sal

    def give_raise(self,amount=5000):
        """Function to give raise to salary."""
        self.salary += amount
   
