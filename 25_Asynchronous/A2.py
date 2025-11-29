# Make 3 tasks run at the same time instead of one-by-one.

import asyncio

async def task(n):
    print(f"Download file {n}")
    await asyncio.sleep(3)
    print(f"File {n} downloaded!")

async def main():
    await asyncio.gather(task(1), task(2), task(3))

asyncio.run(main())

# OP:
# Download file 3
# Download file 2
# Download file 1
# File 3 downloaded!
# File 2 downloaded!
# File 1 downloaded!