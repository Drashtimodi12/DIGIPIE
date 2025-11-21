class Car:
    # Class Attribute
    wheels = 4

    # Constructor → defines instance attributes
    def __init__(self, name, color):
        self.name = name      # Instance Attribute
        self.color = color    # Instance Attribute

    # Method to print info
    def info(self):
        print(f"Brand: {self.name}, Color: {self.color}, Wheels: {Car.wheels}")

# Creating objects with instance attributes
C1 = Car('XUV700', 'Black')
C2 = Car('I20', 'White')

C1.info()
C2.info()



