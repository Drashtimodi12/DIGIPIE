# Iterate over a dictionary and print keys only.

d = {'a' : 'apple', 'b' : 'banana', 'c' : 'cherry'}

for k in d.keys():
    print(k, end = ", ")


print("\n\n======================\n")


# Iterate over a dictionary and print values only.

d = {'a' : 'apple', 'b' : 'banana', 'c' : 'cherry'}
for v in d.values():
    print(v, end = ", ")

print("\n\n======================\n")

# Iterate over a dictionary and print key → value pairs.
d = {'a' : 'apple', 'b' : 'banana', 'c' : 'cherry'}
for k, v in d.items():
    print(k, v)