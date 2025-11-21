"""
Hierarchical Inheritance  
One parent → multiple children  
Example: Vehicle → (Car, Bike)
All children inherit from the same parent class
"""

# Parent class
class vehical:
    # Common method for all vehicles
    def start(self):
        print("\nVehical Starts.")

# Child class 1 → inherits from vehical
class car(vehical):
    # Method specific to car
    def car_info(self):
        print("Red color car.")

# Child class 2 → inherits from vehical
class Bike(vehical):
    # Method specific to bike
    def bike_info(self):
        print("2 wheel bike.")

# Creating object of Car class
c = car()
c.start()        # Using parent class method
c.car_info()     # Using child class method

# Creating object of Bike class
b = Bike()
b.start()        # Using parent class method
b.bike_info()    # Using child class method
