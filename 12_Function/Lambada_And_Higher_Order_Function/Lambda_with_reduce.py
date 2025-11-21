"""    -------3. reduce() Function------
Applies a rolling computation to pairs of elements in a sequence —
i.e., it reduces the iterable to a single value.

Its available inside the functools module, so you must import it:
from functools import reduce


Syntax: reduce(function, iterable)
"""
# Use reduce() and lambda to find the product of all numbers in a list.

from functools import reduce

num = [1, 2, 3, 4, 5, 6]
a = reduce(lambda x, y : x + y, num)
print(a)


b = lambda x, y : x * y
num = [1, 2, 3, 4, 5, 6]
print(reduce(b, num))