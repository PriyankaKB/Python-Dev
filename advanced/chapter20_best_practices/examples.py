# examples.py
# Example code for best practices

# 1. Use descriptive variable names
total_price = 100
number_of_items = 5
average_price = total_price / number_of_items
print(f"Average price: {average_price}")

# 2. Use functions to avoid code repetition
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")

# 3. Use docstrings for documentation
def add(a, b):
    """Return the sum of a and b."""
    return a + b

print(add(2, 3))

# 4. Use context managers for file operations
with open('sample.txt', 'w') as f:
    f.write('Hello, file!')

# 5. Handle exceptions properly
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

# 6. Follow PEP8 style guidelines (indentation, spaces, etc.)
# This is a comment explaining the next line
x = [1, 2, 3]
for item in x:
    print(item)
