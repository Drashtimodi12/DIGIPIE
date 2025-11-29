# Run Two CPU-Heavy Functions in Parallel
# Write two functions:
# square_numbers() → calculate squares of numbers 1 to 50,000
# cube_numbers() → calculate cubes of numbers 1 to 50,000
# Run both using two different processes.

from multiprocessing import Process    # Import Process class to create new processes
import time

def square_numbers():
    for i in range(1, 50001):
        a = i ** 2
        print(f"Square function 1: Square of {i} is {a}.")
    print("Square function 1 Finished")

def cube_numbers():
    for i in range(1, 50001):
        b = i ** 3
        print(f"Cube function 2: Cube of {i} is {b}.")
    print("Cube function 2 Finished")

if __name__ == "__main__":      
    p1 = Process(target = square_numbers)
    p2 = Process(target = cube_numbers)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("\nBoth processes finished (Main Program ends).")