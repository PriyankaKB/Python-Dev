# examples.py
# Example code for type hints

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))

from typing import List

def total(values: List[int]) -> int:
    return sum(values)

print(total([1, 2, 3]))
