# Using reduce():
# Use reduce() with a lambda function to find the product of all numbers in the list.

from functools import reduce

a = [1, 2, 3, 4, 5]
product = reduce(lambda x, y : x * y, a)
print(product)
