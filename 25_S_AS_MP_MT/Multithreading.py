"""
Definition:- Multithreading means running multiple threads at the same time within the same program. 

What is a Thread:- A thread is a small units of a process, lightweight part of a program that can run tasks independently.
    A single program (process) can have multiple threads working at the same time.

What is Threading:- Threading is a technique where multiple threads run simultaneously inside one program.
    Python provides a threading module to create and manage these threads.
    
When is Threading Useful:- Threading is useful for I/O-bound tasks, such as:
    Reading/writing files, Downloading data, Waiting for network responses, Database operations
    Because these tasks involve waiting, multiple threads can run while others wait.

When is Threading NOT useful?:- Threading is not good for CPU-heavy tasks (like large calculations) because 
    of the GIL (Global Interpreter Lock) that allows only one thread to execute Python code at a time.

What is Global Interpreter Lock?:- The GIL is a lock in Python that allows only one thread to execute Python code at a time. 
    Even with multiple threads and multiple CPU cores, only one thread can run at once. 
    Because of this, multithreading is not useful for CPU-heavy tasks in Python.

Threading Functionalities:-
    threading.Thread(target=Function_name):- Creates a new thread and assigns a function for it to execute.
    start():- Begins the execution of the thread’s assigned function.
    join():- Stops the main program until the thread has finished running.
    is_alive():- Checks whether the thread is still running or has completed.
    current_thread():- Returns the thread that is currently executing the code.
    daemon = True:- Marks the thread as a background thread that ends when the main program ends.

                ┌──────────────────────────┐
                │        ONE PROCESS       │
                │   (Same Memory Space)    │
                └───────────┬──────────────┘
                            |
           ┌────────────────┴────────────────┐
           |                |                |
     ┌──────────┐     ┌──────────┐     ┌──────────┐
     │ Thread 1 │     │ Thread 2 │     │ Thread 3 │
     └──────────┘     └──────────┘     └──────────┘
           |                 |                |
       (Runs code)      (Runs code)      (Runs code)

All threads run inside one single process. Threads share memory.    
Because of GIL → only one thread runs Python code at a time
"""

import threading
import time

# Function that represents Task 1
def fun1():
    print("Function 1 start")
    time.sleep(3)   # Simulating a 3-second time-taking task
    print("Function 1 Finished")

# Function that represents Task 2
def fun2():
    print("Function 2 start")
    time.sleep(2)   # Simulating a 2-second time-taking task
    print("Function 2 Finished")

# Creating two threads and assigning tasks to them
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)

# Starting both threads (they run at the same time)
t1.start()
t2.start()

# Wait for both threads to finish before ending the main program
t1.join()
t2.join()

print("Both tasks completed (Main thread ends)")
