"""    -------2. filter() Function------
Filters elements from an iterable based on a condition (True/False).
A filter object (convert to list to see results).
Syntax: filter(function, iterable)
"""

# Use filter() and lambda to get even numbers from a list.

num = [1, 2, 3, 4, 5]
a = list(filter(lambda x : x % 2 == 0, num))
print(a)

a = lambda x : x % 2 == 0
x = [1, 2, 3, 4, 5]
print(list(filter(a, x)))