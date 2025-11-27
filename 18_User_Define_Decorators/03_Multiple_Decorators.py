# 3. Multiple Decorators (Stacked Decorators) You can apply more than one decorator to the same function.

def star_decorator(func):
    def wrapper():
        print("*****")
        func()
        print("*****")
    return wrapper

def hash_decorator(func):
    def wrapper():
        print("#####")
        func()
        print("#####")
    return wrapper


@star_decorator      # applied second
@hash_decorator      # applied first
def greet():
    print("Hello, Drashti!")


greet()

# OP:
# *****
# #####
# Hello, Drashti!
# #####
# *****