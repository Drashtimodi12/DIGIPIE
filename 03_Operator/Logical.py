# Logical Operators:  and, or, not



# Check if a person can vote: Age ≥ 18   And must be Indian (country == "India")
a = int(input("Enter your age: "))
c = input("Country: ").upper()

if a >= 18 and c == 'INDIAN':
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("\n===========================\n")
# Check if a number is positive AND even.
e = float(input("Enter Number: "))
if e >= 0 and e % 2 == 0:
    print("Positive and even")
else:
    print("Not positive and even")

print("\n===========================\n")


# Write a program using not to flip boolean value.
user = input("Enter True/Flase: ").title()
value = user == "True"
print("Original:", value)
print("Flipped:", not value)