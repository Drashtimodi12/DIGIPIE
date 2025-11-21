"""
Definition: A decorator is a special function that adds extra functionality to another function without 
            modifying its actual code.
        A decorator wraps another function and allows you to run code before or after the main function executes

Why Do We Use Decorators? 
    Add extra behavior to functions
    Avoid rewriting the same code again and again
    Keep code clean and reusable
    Implement logging, authentication, timing, access control, etc.
"""


# Decorator function
def greet(fx):
    # Inner function that will wrap the original function
    def mfx(*arge, **kwargs):
        print("Good Morning!")              # Code before calling actual function
        fx(*arge, **kwargs)                 # Calling the original function
        print("Thanks for using Function...\n")    # Code after calling the function
    return mfx                               # Returning the modified function

# Applying the greet decorator to hello()
@greet
def hello():
    print("Hello World")                     # Original function

# Applying the greet decorator to add()
@greet
def add(a, b):
    print(a + b)                              # Function that prints the sum

# Calling decorated hello()
hello()

# Calling decorated add()
add(3, 6)
