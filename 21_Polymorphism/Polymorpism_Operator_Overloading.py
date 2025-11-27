"""
Operator Polymorphism: Operator Polymorphism means the same operator behaves differently 
    based on the type of data it is used with.      Same operator, multiple forms = polymorphism.

Example:
5 + 10 → performs addition
"A" + "B" → performs string join (concatenation)
[1, 2] + [3, 4] → performs list merge

Because of this flexible behavior, Python supports polymorphism with operators.
"""



# Integer addition
a = 10
b = 20
print("Integer addition:", a + b)

# String concatenation
s1 = "Hello "
s2 = "World"
print("String concatenation:", s1 + s2)

# List joining
l1 = [1, 2, 3]
l2 = [4, 5]
print("List joining:", l1 + l2)
