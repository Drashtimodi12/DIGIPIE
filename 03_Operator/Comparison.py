# Comparison Operators:   ==, !=, >, <, >=, <=


a = 10
b = 5
c = 10

print(f"{a} == {c}: {a == c}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{b} < {a}: {b < a}")
print(f"{a} >= {c}: {a >= c}")
print(f"{b} <= {a}: {b <= a}")

print("\n===========================\n")

# Take 2 numbers and print which one is greater.
x = float(input("Enter Num1: "))
y = float(input("Enter Num2: "))
if x > y:
    print(f"{x} is greater number")
else:
    print(f"{y} is greater number")

print("\n===========================\n")


# Check if user’s age is equal to 18 or not.
age = int(input("Enter your age: "))
if age == 18:
    print("You are exactly 18")
else:
    print("You are NOT 18")

print("\n===========================\n")

# Check if three numbers are in ascending order.

e = 1
f = 5
g = 6
if e < f < g:
    print("Numbers are in ascending order")
else:
    print("Number is not ascending order")