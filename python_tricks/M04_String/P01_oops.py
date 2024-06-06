import os 
os.system('clear')

class Car:
    """Representing the car object."""
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.color!r}, {self.mileage!r})"
        #return f"Car({self.color}, {self.mileage})"
    
    def __str__(self):
        return f"A {self.color} color car."

my_car = Car('blue', 32323)
print(my_car)
print(repr(my_car))

# a blue color car.
# Car(blue, 32323)
# Car('blue', 32323)