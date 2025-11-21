"""
A static method is a method inside a class that does not access or modify instance attributes (self) or 
class attributes (cls).
It behaves like a regular function, but logically belongs to the class.
Declared with the @staticmethod decorator.
Can be called using the class name or an instance.
Cannot access instance variables or class variables directly.

Syntx:
class MyClass:
    
    @staticmethod
    def greet(name):
        print(f"Hello, {name}!")

Here, greet is a static method.
It doesn’t use self or cls.
"""

# Task 11: Create a class Maths with:
# static method: add(a, b) → return sum
# static method: mul(a, b) → return product
# Use these methods without creating an object.


class Math():
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def mul(c, d):
        return c * d
    
print(Math.add(2, 3))

m = Math()
print(m.mul(4, 7))