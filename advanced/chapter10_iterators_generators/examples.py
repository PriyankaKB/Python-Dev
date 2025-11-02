# examples.py
# Example code for iterators and generators

# Iterator example
numbers = [1, 2, 3]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator example
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print('Countdown:', num)
