# Q1. Create a list of squares of numbers from 1 to 10 using list comprehension.

result = [i**2 for i in range(1, 21)]
print(result)

# OP: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

print("\n=========================\n")

# Q2. Extract all even numbers from a list using list comprehension.
a = [i for i in range(1, 10+1) if i %2 == 0 ]
print(a)
# OP: [2, 4, 6, 8, 10]