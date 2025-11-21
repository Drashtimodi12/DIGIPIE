# Recursive Function:
# Write a recursive function factorial(n) that returns the factorial of a given number n.

def fact(a):
    if a == 1:
        return 1
    else:
        return a * (fact(a-1))

b = int(input("Enter the number for factorial: "))
print(f"The number of factorial is {fact(b)}")

