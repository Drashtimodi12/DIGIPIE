# Identity Operators: is, is not

# Compare two lists using == and is, explain result.
a = [1, 2, 3]
b = [1, 2, 3]
print("Using == :", a == b)
print("Using is operator: ", a is b)

print("\n===========================\n")

# Check if two variables point to same memory location.
x = [10, 20, 30]
y = x   

print("x == y :", x == y)     
print("x is y :", x is y)    