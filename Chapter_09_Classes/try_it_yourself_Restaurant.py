import os 
os.system('clear')

class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cusine_type):
        """Initializing the attribute restaurant_name, cusine_type."""
        self.restaurant_name = restaurant_name
        self.cusine_type = cusine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Prints the attributes."""
        print(f"Restaurant name: {self.restaurant_name.title()} with cuisine: {self.cusine_type}.")
    
    def open_restaurant(self):
        """ Tells if restaurant is open. """
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, customers_served):
        """ Updated the customers_served attribute"""
        self.number_served = customers_served
    
    def
    
restaurant = Restaurant('pizz_house', 'Italian')
print(restaurant.cusine_type)
restaurant.describe_restaurant()
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)