# Convert dictionary into list of tuples

a = {"a":1, "b":2}

b = list(tuple(a.items()))
print(b)        # [('a', 1), ('b', 2)]

