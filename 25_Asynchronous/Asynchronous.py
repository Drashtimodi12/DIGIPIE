"""
Asynchronous:- this execution lets multiple tasks run without blocking each other by using non-blocking I/O and
     an event loop, making programs faster and more efficient for operations that involve waiting.

Ex: “Start a task → donot wait for it → move to next task → come back when the first task is done.”

This approach is excellent for tasks that spend a lot of time waiting, such as:
    Downloading files; Calling APIs; Database queries; Sending emails; Timer tasks; Background processingrs

How Asynchronous Works in Python:- 
    async def keyword --> Defines a coroutine (an asynchronous function).
    await keyword --> Pauses the async function until the awaited task is finished.
    asyncio module --> Built-in module that manages asynchronous tasks.
        asyncio.sleep() --> Asynchronous, non-blocking timer
        asyncio.gather() --> Run multiple async tasks at the same time
        asyncio.run() --> Starts the main event loop
        asyncio module --> Built-in module that manages asynchronous tasks.    

Event Loop
Async code runs on an event loop, which decides:
    Which task should run, Which task is waiting, When to resume tasks
    The event loop allows pseudo-parallel execution in a single thread.

Why Use Asynchronous Programming?
    Best for I/O-bound operations
    If your code is waiting for:    API responses, File read/write, Database fetch, Network requests
        Async allows other tasks to run while waiting. This improves speed and performance.
    
Not ideal for CPU-heavy tasks:- For heavy processing use:
    multiprocessing, multithreading


    Asynchronous Execution
---------------------------------------------------
Task 1: Start --- Wait ⏳ --- Continue -------- Finish
                    |
Task 2: Start ------+------ Continue --------- Finish
                    |
Task 3: Start ------+------ Continue --------- Finish
"""


import asyncio   # Import Python's built-in asynchronous module

# -----------------------------------------
# Asynchronous Function 1
# -----------------------------------------
async def fun1():
    print("Function 1 Start.")
    
    # Non-blocking wait for 5 seconds.
    # During this wait, other async tasks can run.
    await asyncio.sleep(5)
    
    print("Function 1 Stop.")


# -----------------------------------------
# Asynchronous Function 2
# -----------------------------------------
async def fun2():
    print("Function 2 Start.")
    
    # Non-blocking wait for 2 seconds.
    # This runs independently from fun1().
    await asyncio.sleep(2)
    
    print("Function 2 Stop.")

# -----------------------------------------
# Main asynchronous function
# This function executes both fun1() and fun2() concurrently.
# -----------------------------------------
async def main():
    # asyncio.gather() runs both functions at the same time.
    await asyncio.gather(fun1(), fun2())

# -----------------------------------------
# Start the event loop and run the program
# -----------------------------------------
asyncio.run(main())


# OP:
# Function 1 Start.
# Function 2 Start.
# Function 2 Stop.
# Function 1 Stop.