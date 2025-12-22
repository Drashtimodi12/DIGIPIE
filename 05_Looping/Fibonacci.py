# Input N and print first N Fibonacci numbers using a loop.

num = int(input("Enter a number: "))

a = 0
b = 1
print(a, b, end = " ")

for i in range(2, num + 1):
    c = a + b
    print(c, end = " ")
    a = b
    b = c

print("\n====================\n")

num = int(input("Enter a number: "))

a = 0
b = 1
print(a, b, end = " ")

while num > 2:
    c = a + b
    print(c, end=" ")
    a = b
    b = c
    num -= 1
    