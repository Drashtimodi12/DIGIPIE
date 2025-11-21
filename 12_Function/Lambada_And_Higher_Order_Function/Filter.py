# Using filter():
# Use filter() with a lambda function to select only even numbers from the list.

a = [1, 2, 3, 4, 5]
result = list(filter(lambda x : x % 2 == 0, a))
print(result)