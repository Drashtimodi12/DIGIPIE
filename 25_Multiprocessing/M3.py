# Create 3 Processes to Perform Heavy Tasks
#     Count numbers from 1 to 2 million
#     Add numbers from 1 to 1 million
#     Multiply numbers in a loop 1 to 200,000
# Each process should print:
#     Process X started
#     Process X finished
# Goal: Understand how multiprocessing speeds up CPU-heavy tasks.


from multiprocessing import Process
import time

def count_numbers():
    print("Process 1 started: Counting numbers from 1 to 2 million")
    total = 0
    for i in range(1, 2000001):
        total += 1
    time.sleep(1)  # Simulate some delay
    print("Process 1 finished")

def add_numbers():
    print("Process 2 started: Adding numbers from 1 to 1 million")
    total = 0
    for i in range(1, 1000001):
        total += i
    time.sleep(10)  # Simulate some delay        
    print("Process 2 finished")

def multiply_numbers():
    print("Process 3 started: Multiplying numbers in a loop from 1 to 200,000")
    product = 1
    for i in range(1, 200001):
        product *= i
    time.sleep(1)  # Simulate some delay
    print("Process 3 finished")

if __name__ == "__main__":
    p1 = Process(target=count_numbers)
    p2 = Process(target=add_numbers)
    p3 = Process(target=multiply_numbers)

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print("All processes finished (Main Program ends).")


# OP:
# Process 1 started: Counting numbers from 1 to 2 million
# Process 2 started: Adding numbers from 1 to 1 million
# Process 3 started: Multiplying numbers in a loop from 1 to 200,000
# Process 1 finished
# Process 2 finished
# Process 3 finished
# All processes finished (Main Program ends).