# asyncio_example.py
# Examples and explanations for asyncio

# Example of using asyncio in Python

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('...World!')

asyncio.run(main())
