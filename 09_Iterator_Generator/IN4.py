# Q7. Flatten a nested list using a single list comprehension.

mylist = [[1,2], [3,4], [5,6]]
a = [i for l in mylist for i in l]
print(a)
# OP: [1,2,3,4,5,6]

