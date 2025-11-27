#    *
#   ***
#  *****
# *******
row = 4
for i in range(1, 5):
    print(" " * (row-i), "*" * (2 * i - 1)) 

print("\n=======================\n")

# *******
#  *****
#   ***
#    *
r = 4
for i in range(r, 0, -1):
    print(" " * (row - i) + "*" * (2 * i - 1))

print("\n=======================\n")


#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(1, 5):
    print(" " * (row - i) + "*" * (2 * i - 1))
for j in range(3, 0, -1):
    print(" " * (row - j) + "*" * (2 * j - 1))

