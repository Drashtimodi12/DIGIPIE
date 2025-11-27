# 9. Lambda Function (Anonymous Function)
a = lambda x: x + 5
print(a(10))
# Output: 15

print("\n================\n")

a = lambda x, y : x * y
print(a(5, 6))
# Output: 30

print("\n================\n")

# Use lambda to sort a list of tuples by the second element.
data = [(4, 10), (1, 5), (9, 2)]
result = sorted(data, key=lambda x : x[1])
print(list(result))

print("\n================\n")

re = sorted(data, key=lambda x : x)
print(list(re))





