import os
os.system('clear')

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model,year) -> None:
        """Initialize the attributes make model year."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Returns a neatly formatted descriptive name."""
        
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing car's mileage."""
        print(f"\nThis car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the new value."""

        if self.odometer_reading < mileage:
            self.odometer_reading = mileage
        else:
            print("Warning: Odometer reading can't be rolled back.")

    def increment_odometer(self,mileage):
        """ This function updates the mileage by incrementing it."""
        self.odometer_reading +=mileage


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

#Changing the attribute directly 
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

#Changing the attribute by defining a function 
my_new_car.update_odometer(200)
my_new_car.read_odometer()

#Changing the attribute by incrementing it by a value
my_new_car.increment_odometer(200)
my_new_car.read_odometer()
 
