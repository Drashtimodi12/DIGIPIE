# A
# A B
# A B C
# A B C D

row = 4
alp = r"[A-Z]"
for i in range(1, row+1):
    for j in range(0, i):
        print(chr(65 + j), end = " ")
    print()