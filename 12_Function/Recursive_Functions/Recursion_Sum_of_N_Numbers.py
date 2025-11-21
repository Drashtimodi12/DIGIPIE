# Return the sum of numbers from 1 to n using recursion.

def num(a):
    if a <= 1:
        return 1
    else:
        return a + num(a-1)
print(num(8))
    