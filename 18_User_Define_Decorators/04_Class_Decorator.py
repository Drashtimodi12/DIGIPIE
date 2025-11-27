# 4. Class Decorator      A class can also act as a decorator.

class MyDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("Before")
        self.func()
        print("After")

@MyDecorator
def greet():
    print("Hello!")

greet()

# OP:
# Before
# Hello!
# After