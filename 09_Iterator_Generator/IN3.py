# Q5. Create a list of tuples (number, cube) for numbers 1 to 10.


num = range(1, 11)
result = [(i, i**3) for i in num]
print(result)
# OP: [(1, 1), (2, 8), (3, 27), (4, 64), (5, 125), (6, 216), (7, 343), (8, 512), (9, 729), (10, 1000)]