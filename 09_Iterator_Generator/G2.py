# Q9. Use a generator expression to get only odd numbers from a list.
def odd(a):
    for i in a:
        if i % 2 != 0:
            yield i
b = [1, 2, 3, 4, 5]
gen = odd(b)
print(next(gen))
print(next(gen))
print(next(gen))
# OP:
# 1
# 3
# 5



# Q11. Write a generator expression to compute the sum of cubes of numbers 1 to 5.
# a = sum(x ** 3 for x in range(1, 7) )

def s(c):
    for i in range(1, c+1):
        yield i**3

ge = s(2)
print(sum(ge))
# OP:9

print("\n=============================\n")


# Q12. Write a generator that yields numbers divisible by both 3 and 5 (up to 100).
def divide():
    for i in range(1, 50):
        if i % 3 == 0 or i % 5 == 0:
            yield i
result = divide()
print(list(result))
# OP: [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30, 33, 35, 36, 39, 40, 42, 45, 48]