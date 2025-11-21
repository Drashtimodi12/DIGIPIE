# List task — Find largest number
import math
def greet(fun):
    def start():
        print("-----START-----")
        a = [3, 9, 1, 7, 4]
        b = max(a)
        fun(b)
        print("-----END-----\n")
    return start

@greet
def num(b):
    print("Largest number: ", b)

num()