"""
Method Resolution Order:- MRO defines the order in which Python searches for a method or attribute when it
 is called in a class with inheritance.

Python follows a specific path to decide which class’s method should run.

This is mainly used in:
    Multiple inheritance
    Hybrid inheritance

Important Notes
    MRO is very important in multiple inheritance.
    Python uses C3 Linearization Algorithm to avoid ambiguity.
    Always left to right in class definition.
    The last class is always object, the base of all classes.
    Prevents the diamond problem by a consistent search order.
"""

# Parent classes
class A:
    def show(self):
        print("Method from class A")

class B:
    def show(self):
        print("Method from class B")

# Child class inheriting from A and B
class C(A, B):  # C inherits from A first, then B
    pass

# Creating object of child class
obj = C()

# Calling method 'show' - Python follows MRO
obj.show()  # Output: Method from class A

# Checking Method Resolution Order
print(C.mro())  
# Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
