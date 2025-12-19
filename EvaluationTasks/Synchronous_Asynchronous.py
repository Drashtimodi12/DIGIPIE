"""
Question 4: Synchronous vs Asynchronous Programming (25 Marks | 45 Minutes)
Objective: Understand blocking vs non-blocking execution.
Problem Statement: Simulate 3 API calls, each taking 2 seconds.

Part A: Synchronous Execution=
Use time.sleep(2)
Execute API calls one by one
Print start and end time
Measure total execution time

Part B: Asynchronous Execution=
Use asyncio
Use async def and await asyncio.sleep(2)
Run API calls concurrently
Measure total execution time
"""

import time
import asyncio
import requests

print("***Synchronous***")
def syn_fun(api_number):
    print(f"API {api_number} start.")
    time.sleep(2)
    print(f"API {api_number} end.")


start = time. time()
syn_fun(1)
print("---------------")
syn_fun(2)
print("---------------")
syn_fun(3)
end = time.time()

print("-----")
print(f"Total Synchronous Execution time: {end - start} seconds.")


print("\n\n***Asynchronous***")
async def asyn_fun(number):
    print(f"API {number} start.")
    await asyncio.sleep(2)
    print(f"API {number} end.")

async def main():
    start = time.time()
    await asyncio.gather(asyn_fun(1), asyn_fun(2), asyn_fun(3))
    end = time.time()
    print("-----")
    print(f"Total Asynchronous Execution time: {end - start} seconds.")


asyncio.run(main())

