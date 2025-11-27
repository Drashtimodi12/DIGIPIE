"""
yield is like a temporary return in a function. It produces a value and pauses the function, 
remembering where it left off.  When the function is called again, it resumes from that point.

Functions with yield are called generator functions.

They don’t return all values at once, they generate them one by one.
"""

# Q8. Create a generator expression that yields squares of numbers from 1 to 10.
def sq():
    for i in range(1, 11):
        yield i ** 2

print(list(sq()))
# OP: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("\n=====================\n")

gen = sq()
print(next(gen))
print(next(gen))
# OP:
# 1
# 4


print("\n=============================\n")

# Q10. Create a generator that yields characters from a string one by one.
import time
def name(s):
    for i in s:
        yield i
        time.sleep(1)

gen1 = name('Drashti')
for ch in gen1:
    print(ch)
# OP:
# D
# r
# a
# s
# h
# t
# i

print("\n=============================\n")
