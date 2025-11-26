# Input a number N and print its multiplication table up to 10 using a loop.

a = int(input("Enter a Number: "))

for j in range(1, 11):
        print(f"{a} * {j} = {a * j}")
