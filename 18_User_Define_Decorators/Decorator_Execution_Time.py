# Decorator + loop task
import time

def greet(fun):
    def wrepper():
        print("-----START-----")
        start = time.time()
        fun()
        end= time.time()
        print(F"\nProgram runing time is: {end - start} second.")
        print("-----END-----\n")
    return wrepper

@greet
def n():
    for i in range(1, 101):
        print(i, end = " ")

n()