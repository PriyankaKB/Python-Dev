# examples.py
# Example code for comprehensions

# List comprehension
squares = [x * x for x in range(5)]
print('Squares:', squares)

# Dict comprehension
square_dict = {x: x * x for x in range(5)}
print('Square dict:', square_dict)

# Set comprehension
unique = {x % 2 for x in range(5)}
print('Unique set:', unique)
