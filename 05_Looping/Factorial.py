# Input a number and calculate its factorial using a loop.


a = int(input("Enter number: "))
m = 1
for i in range(1, a+1):
    m *= i
print(m)