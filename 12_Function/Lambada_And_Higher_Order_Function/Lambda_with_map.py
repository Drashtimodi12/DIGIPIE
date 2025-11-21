"""    -------1. map() Function------
Applies a function to every element in an iterable (like a list or tuple).
A map object (which you usually convert to a list using list()).
Syntax: map(function, iterable)
"""
# Given a list [1, 2, 3, 4], use map() and lambda to square each number.

a = [1, 2, 3, 4]
squ = list(map(lambda x : x * x, a))
print(squ)


squ = lambda x : x * x
x = [1, 2, 3, 4]
print(list(map(squ, x)))
