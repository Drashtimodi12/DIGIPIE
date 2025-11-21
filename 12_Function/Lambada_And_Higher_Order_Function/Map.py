# Using map():
# Use map() with a lambda function to double each number in the list.

a = [1, 2, 3, 4, 5]
result = list(map(lambda x : x * 2, a))
print(result)