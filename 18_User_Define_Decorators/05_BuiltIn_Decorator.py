"""
5. Built-in Decorators in Python:-
    Python provides decorators for functions, classmethods, readonly properties, etc.

✔ @staticmethod
✔ @classmethod
✔ @property
"""



"""
==============================@classmethod============================================
A class method is a method that belongs to the class rather than an instance.
It can access class attributes but cannot access instance attributes directly, because it doesn’t operate 
on a particular object.

Decorator: @classmethod
First parameter: cls (refers to the class itself, not the object)

Syntax:
class ClassName:
    @classmethod
    def method_name(cls, other_parameters):
        # code

cls is a reference to the class, not an object.
Can modify class attributes or create alternative constructors.
"""

class Class_name:
    name = 'Drashti'

    @classmethod
    def Class_varibale_changed(cls,new_name):
        Class_name.name = new_name
        print(f"My name is {Class_name.name}.")

c1 = Class_name()

c1.Class_varibale_changed('Sejal')

# OP: My name is Sejal.

print("\n======================================================\n")










"""
==============================@staticmethod============================================
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
# OP:
# 5
# 28