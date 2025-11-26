# Assignment Operators:   =, +=, -=, *=, /=, %=, //=, **=


x = 10
print(x)

x += 5
print(x)

x -= 2
print(x)

x *= 2
print(x)

x /= 2
print(x)

x %= 4
print(x)

x //= 2
print(x)

x **= 3
print(x)

print("\n===========================\n")

# Take number from user and keep adding 10 using += until number > 50.

a = float(input("Enter number: "))
total = 0
while a <= 50:
    total += a
    print("Current value: ", total)
    a += 10
print("Loop ended. Final Value is ", total)