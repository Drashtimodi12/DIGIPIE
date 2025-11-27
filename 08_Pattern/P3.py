# 1
# 1 2
# 1 2 3
# 1 2 3 4

row = 4

for i in range(1, row+1):       # print rows
    for j in range(1, i + 1):   # prints numbers from 1 to i
        print(j, end=" ")
    print()
    

print("\n==============\n")

# 1
# 2 2
# 3 3 3
# 4 4 4 4

num = 4
for i in range(1, row+1):
    for j in range(1, i + 1):
        print(i, end =" ")
    print()

print("\n==============\n")


# 1 2 3 4
# 1 2 3
# 1 2
# 1

for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()

print("\n==============\n")

# 1
# 2 3
# 4 5 6
# 7 8 9 10
num = 1
for i in range(1, 5):
    for j in range(1, i + 1):
        print(num , end=" ")
        num += 1
    print()


print("\n==============\n")


# 10 9 8 7
# 6 5 4
# 3 2
# 1

num = 10
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print(num, end= " ")
        num -= 1
    print()


print("\n==============\n")


# 5
# 5 4
# 5 4 3
# 5 4 3 2
# 5 4 3 2 1

row = 5
for i in range(1, row+1):
    for j in range(5, 5 - i, -1):
        print(j, end = " ")
    print() 


print("\n==============\n")

# 1
# 0 1
# 1 0 1
# 0 1 0 1

row = 4
for i in range(1, row+1):
    for j in range(i):
        print((i + j) % 2, end = " ")
    print()