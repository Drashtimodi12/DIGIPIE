"""
What is Abstraction?    
    Abstraction hides the internal details of a class and shows only the essential features to the user.
    Users don’t need to know how it works internally; they only use the functionality.
    In Python, abstraction is achieved using abstract classes and abstract methods from the abc module.

Think of it like a TV remote: you press buttons (essential feature), but you don’t see the circuits inside.

Abstract Class
    A class that cannot be instantiated directly.
    Used as a base class for other classes.
    Can contain abstract methods (methods without implementation) and concrete methods (methods with implementation).

Syntax:
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_method(self):
        pass  # abstract method has no body

        
Abstract Method
    A method declared in an abstract class without any body.
    Must be implemented in the child class.
    Declared using @abstractmethod decorator.


Important Notes (Easy to Remember)
    Abstract Class → cannot create object   v = Vehicle()  # Error
    Abstract Method → must be implemented in child class, otherwise it becomes abstract too.
    Concrete Method in Abstract Class → can be used by children
    Acts as a blueprint / template for child classes
    Provides abstraction → hides internal details, shows only essential features
    Can be used with multiple inheritance and polymorphism.
"""


# Importing ABC and abstractmethod from the abc module
# ABC -> Used to create Abstract Base Classes
# abstractmethod -> Used to declare abstract methods
from abc import ABC, abstractmethod


# Creating an abstract class named Vehicle
# Because it inherits from ABC, it becomes an abstract class
class Vehicle(ABC):

    # Declaring an abstract method
    # Abstract methods do NOT have a body (only function definition)
    # Any class that inherits Vehicle MUST implement this method
    @abstractmethod
    def start(self):
        pass  # 'pass' is used as a placeholder since abstract method cannot have implementation


    # Concrete method - has body
    def stop(self):
        print("Vehicle stopped")

class Car(Vehicle):  # Child class inherits abstract class
    # Implement abstract method
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):    # Child class inherits abstract class
    # Implement abstract method
    def start(self):
        print("Bike starts with a kick")

# Create objects of child classes
c = Car()
b = Bike()

c.start()  # Output: Car starts with a key
c.stop()   # Output: Vehicle stopped

b.start()  # Output: Bike starts with a kick
b.stop()   # Output: Vehicle stopped
