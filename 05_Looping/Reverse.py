# Input a number and reverse it using a loop.

# a = int(input("Enter a number to reverse: "))
a = 102
rev = 0
while a > 0:
    digit = num % 10       # Get last digit
    rev = rev * 10 + digit # Add digit to reverse number
    num //= 10             # Remove last digit

print("Reversed number:", rev)
   
print("\n====================\n")

