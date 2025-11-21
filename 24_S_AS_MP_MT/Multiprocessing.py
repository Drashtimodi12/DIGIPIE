"""
Definition:- Multiprocessing means running multiple processes at the same time, where 
each process has its own memory space and runs independently on different CPU cores.

What is a Process?:-  
    A process is an independent program with its own memory, resources, and execution space.
    Unlike threads, processes do NOT share memory and can run truly in parallel.

What is Multiprocessing?:-
    Multiprocessing is a technique where multiple processes run simultaneously, 
    allowing Python to use multiple CPU cores for actual parallel execution.

When is Multiprocessing Useful?:-
    Multiprocessing is best for CPU-bound tasks, such as:
        • Large mathematical calculations
        • Image processing
        • Data analysis
        • Machine Learning tasks
    These tasks require heavy CPU work, so multiprocessing improves speed.

When is Multiprocessing NOT Useful?:-
    It is not efficient for I/O tasks like file reading, downloading, database access,
    because creating processes is heavier and slower than threads.

Why Multiprocessing Works Better Than Multithreading for CPU Tasks?:-
    Because multiprocessing does NOT have the GIL.
    Each process runs independently on separate CPU cores → TRUE PARALLELISM.

Multiprocessing Functionalities:-
    multiprocessing.Process(target=Function_name):- Creates a new process and assigns a function to run.
    start():- Starts execution of the process.
    join():- Makes the main program wait until the process completes.
    is_alive():- Checks if the process is still running.
    name:- Returns the name of the process.

    
      CPU Core 1          CPU Core 2          CPU Core 3
   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
   │  Process 1   │    │  Process 2   │    │  Process 3   │
   │ Own Memory   │    │ Own Memory   │    │ Own Memory   │
   └──────────────┘    └──────────────┘    └──────────────┘
            |                   |                   |
        Task 1             Task 2              Task 3


Every process has separate memory. No GIL problem. Best for CPU-heavy tasks (calculations, ML, processing)
"""

from multiprocessing import Process
import time

# Function for Process 1
def fun1():
    print("Process 1 start")
    time.sleep(3)   # Pause for 3 seconds (simulating a long task)
    print("Process 1 Finished")

# Function for Process 2
def fun2():
    print("Process 2 start")
    time.sleep(2)   # Pause for 2 seconds (simulating a long task)
    print("Process 2 Finished")

# This part runs only when the file is executed directly, and prevents multiprocessing from restarting the program again.
if __name__ == "__main__":
    # Create two separate processes
    p1 = Process(target=fun1)   # Process 1 will run fun1()
    p2 = Process(target=fun2)   # Process 2 will run fun2()

    # Start both processes (run at the same time)
    p1.start()
    p2.start()

    # Wait until both processes finish their tasks
    p1.join()
    p2.join()

    # After both processes are done
    print("Both processes completed (Main process ends)")
