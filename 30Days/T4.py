# Print odd numbers 1–50

# a = 1
# while a <= 50:
#     if a % 2 != 0:
#         print(a, end = ", ")
#     a += 1


def odd():
    for i in range(1, 51):
        i % 2 != 0
        print(i, end = ", ")
odd()