# Given a list of numbers, create a new list containing only even numbers using a loop.


a = [1, 2, 3, 4, 5, 6]

for i in a:
    if i % 2 != 0:
        a.remove(i)
print(a)