# Write synchronous code that calls time.sleep(2) three times.
# → Total time = 6 seconds

import time
def task_sync(n):
    start = time.perf_counter()
    time.sleep(2)
    print(f"Working with task {n}")
    end = time.perf_counter()
    print(f"{n} It takes {end - start:.2f} second")

start_total = time.perf_counter()
task_sync(1)
task_sync(2)
task_sync(3)
end_total = time.perf_counter()
print(f"Total time (sync) = {end_total - start_total:.2f} seconds")


print("\n==================================\n")

# Write asynchronous code that uses await asyncio.sleep(2) three times using gather().
# → Total time = 2 seconds
import asyncio

async def task_async(n):
    start = time.perf_counter()
    print(f"Working with task {n} started")
    await asyncio.sleep(2)  
    print(f"Working with task {n} finished")
    end = time.perf_counter()
    print(f"It takes {end - start:.2f} second")


async def main():
    start_total = time.perf_counter()
    await asyncio.gather(task_async(1), task_async(2), task_async(3))
    end_total = time.perf_counter()
    print(f"Total time (async) = {end_total - start_total:.2f} seconds")


asyncio.run(main())



# OP:
# Working with task 1
# 1 It takes 2.00 second
# Working with task 2
# 2 It takes 2.00 second
# Working with task 3
# 3 It takes 2.00 second
# Total time (sync) = 6.00 seconds

# ==================================

# Working with task 1 started
# Working with task 2 started
# Working with task 3 started
# Working with task 1 finished
# It takes 2.01 second
# Working with task 2 finished
# It takes 2.01 second
# Working with task 3 finished
# It takes 2.01 second
# Total time (async) = 2.01 seconds