"""
Definition:- Synchronous programming means executing tasks one after another, in a fixed sequence.
            A task must finish completely before the next task starts. Sequential execution.

Ex: standing in a line at a ticket counter — the next person is served only after the previous person finishes.

How it works internally:
    If Task 1 takes 5 seconds → Python waits for 5 seconds.
    Only then does Task 2 start.
    Other tasks cannot run in parallel.
    If one task is slow, the entire program slows down.

Good for:- Simple tasks, Predictable flow, Code readability
Not good for:- Slow operations (network, downloading), Apps needing high performance, Handling many users (web servers)


Synchronous Execution
-----------------------------------------
Task 1 -----> Task 2 -----> Task 3 -----> Task 4
(Waits)       (Waits)       (Waits)       (Waits)

Tasks run sequentially. Next task starts only after previous finishes. Slow if tasks involve waiting (e.g., sleep, I/O)
"""

import time   # time.sleep() is used to simulate a time-consuming task

def fun1():
    print("Task 1 Start")
    time.sleep(2)          # Simulating a delay of 2 seconds
    print("Task 1 Finished")

def fun2():
    print("Task 2 Start")
    time.sleep(2)          # Simulating a delay of 2 seconds
    print("Task 2 Finished")

def main():
    # In synchronous programming, tasks execute one after another
    fun1()  # First complete Task 1
    fun2()  # After Task 1 finishes, start Task 2

# Running the synchronous program
main()  # Total time = 2 sec + 2 sec = 4 seconds
