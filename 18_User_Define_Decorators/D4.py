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