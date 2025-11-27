# Q27. Write a decorator that prints: 
# function name 
# execution time 
# arguments passed 

import time

def info_decorator(func):

    def wrapper(*args, **kwargs):
        # Print function name
        print(f"Function Name: {func.__name__}")

        # Print arguments passed
        print(f"Arguments Passed: {args} {kwargs}")

        # Start time
        start = time.time()

        # Call the actual function
        result = func(*args, **kwargs)

        # End time
        end = time.time()

        # Execution time
        print(f"Execution Time: {end - start:.5f} seconds")

        return result

    return wrapper


@info_decorator
def addition(a, b):
    time.sleep(1)   # Just to show time difference
    return a + b


print("Result:", addition(10, 20))
print("\n=======================\n")
print("Result:", addition(a= 10, b= 20))


# OP:
# Function Name: addition
# Arguments Passed: (10, 20) {}
# Execution Time: 1.01448 seconds
# Result: 30

# =======================

# Function Name: addition
# Arguments Passed: () {'a': 10, 'b': 20}
# Execution Time: 1.00082 seconds
# Result: 30

"""
args = (10, 20)
kwargs = {} (no keyword arguments given)

args = () (no positional arguments)
kwargs = {'a': 10, 'b': 20} (two keyword arguments)
"""