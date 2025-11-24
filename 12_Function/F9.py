# Write a function that takes a list and returns a new list with only even numbers.

def myfun(lst):
    return [x for x in lst if x % 2 == 0]

print(myfun([3,6,2,9,1]))