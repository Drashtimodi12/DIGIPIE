# * * * *
# * * * *
# * * * *
# * * * *
r=4
c=4
for i in range(1, r+1):
    for j in range(1, c+1):
        print("*" , end = " ")
    print()



print("\n==============\n")

# *****
# *   *
# *   *
# *****
row = 4
col = 5
for i in range(1, row+1):
    if i == 1 or i == row:
        print("*" * col) 
    else:
        print("*"+" "*(col-2)+"*")
    