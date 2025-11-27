# Loop task — Print table of any number

def greet(fun):
    def start():
        print("Wellcome To printing Table according your input.")

        a = int(input("Enter number: "))

        for i in range(1, 11):
            result = a * i
            fun(a, i, result)
        
        print("Thank You\n")
        
    return start

@greet
def table(a, i, result):
    print(f"{a} * {i} = ", result)

table()

# OP:
# Wellcome To printing Table according your input.
# Enter number: 2
# 2 * 1 =  2
# 2 * 2 =  4
# 2 * 3 =  6
# 2 * 4 =  8
# 2 * 5 =  10
# 2 * 6 =  12
# 2 * 7 =  14
# 2 * 8 =  16
# 2 * 9 =  18
# 2 * 10 =  20
# Thank You
