# examples.py
# Example code for concurrency

import threading
import multiprocessing
import asyncio

# Threading example
def print_numbers():
    for i in range(3):
        print(f"Thread: {i}")

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# Multiprocessing example
def square(n):
    print(f"Square: {n * n}")

process = multiprocessing.Process(target=square, args=(4,))
process.start()
process.join()

# Asyncio example
async def say_hello():
    print("Hello asynchronously!")

asyncio.run(say_hello())
