# Stop taking input if the user enters -1 using break.

while True:
    num = int(input("Enter 1 or -1: "))
    if num == -1:
        print("Stope the program...")
        break
    else:
        print("Welcome")




# Print the list of entered numbers.
a = []
while True:
    num = int(input("Enter a number (or -1 to stop): "))
    if num == -1:
        print("Stope the program...")
        break
    else:
        a.append(num)
print("Numbers entered:", a)