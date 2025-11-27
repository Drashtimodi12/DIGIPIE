"""    -------1. map() Function------
Applies a function to every element in an iterable (like a list or tuple).
A map object (which you usually convert to a list using list()).

Syntax: map(function, iterable)

Why use map?    “Apply this function to every element.”
"""
# Given a list [1, 2, 3, 4], use map() and lambda to square each number.

a = [1, 2, 3, 4]
squ = list(map(lambda x : x * x, a))
print(squ)

print("\n=====================\n")

squ = lambda x : x * x
x = [1, 2, 3, 4]
print(list(map(squ, x)))

print("\n=====================\n")


# Use map() with a lambda function to double each number in the list.

a = [1, 2, 3, 4, 5]
result = list(map(lambda x : x * 2, a))
print(result)

print("\n=====================\n")

# Use map() with lambda to convert a list of temperatures from Celsius to Fahrenheit.
C = [40.1, 20, 0, 100]
result = list(map(lambda c : (9 / 5) * c + 32  , C ))
print(result)


print("\n=====================\n")

f = [104.18, 68.0, 32.0, 212.0]
re = lambda f : (f - 32) * 5 / 9
print(list(map(re, f)))

print("\n=====================\n")

# Use map() to convert each word in a sentence to its length.
S = 'My name is drashti'
result = list(map(lambda x : len(x), S.split()))
print(result)
