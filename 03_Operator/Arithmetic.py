# Arithmetic Operators:-  + , - , * , / , % , // , **


a = float(input("Enter first number: "))
b = float(input("Enter Second number: "))

print("Addition: ", a + b)
print("Subtraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Modulo: ", a % b)
print("Floor Division: ", a // b)
print("Exponent: ", a ** b)

"""
OP:
Enter first number: 12
Enter Second number: 3
Addition:  15.0
Subtraction:  9.0
Multiplication:  36.0
Division:  4.0
Modulo:  0.0
Floor Division:  4.0
Exponent:  1728.0
"""

# Write a program to find the area of a circle using **.
PI = 3.14
area = PI * (a ** 2)
print("Area of circle = ", area)

print("\n===========================\n")

# Find cube of a number without using * two times (use **).
print(f"Cube of {a}: {a**3}.")