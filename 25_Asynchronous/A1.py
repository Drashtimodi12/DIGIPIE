# Create an async function that waits for 2 seconds and prints a message.

import asyncio

async def task(n):
    print("HI!")
    await asyncio.sleep(2)
    print(f"Hello from async! {n} num...")


async def main():
    await asyncio.gather(task(1), task(2))

asyncio.run(main())

# OP:
# HI!
# HI!
# Hello from async! 1 num...
# Hello from async! 2 num...