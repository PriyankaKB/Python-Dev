# pep8_style.py
# Examples and explanations for PEP8 style

# PEP8: Use 4 spaces per indentation level
def add(a, b):
    return a + b

# PEP8: Limit lines to 79 characters
long_variable_name = (
    'This is a long string that is split over multiple lines '
    'to follow the 79 character limit.'
)

# PEP8: Use blank lines to separate functions and classes
class MyClass:
    def __init__(self, value):
        self.value = value

    def show(self):
        print(self.value)

# PEP8: Use spaces around operators and after commas
x = 1 + 2
my_list = [1, 2, 3]

# PEP8: Use lowercase_with_underscores for function and variable names
def my_function():
    pass

# PEP8: Add docstrings to modules, functions, and classes
def greet(name):
    """Greet a person by name."""
    print(f"Hello, {name}!")

greet("Alice")

# PEP8: Example of a function with a docstring
def calculate_area(width, height):
    """Calculate the area of a rectangle."""
    return width * height

area = calculate_area(5, 3)
print(f"Area: {area}")

# PEP8: Constants should be all uppercase with underscores
PI = 3.14159
radius = 2
circle_area = PI * (radius ** 2)
print(f"Circle area: {circle_area}")

# PEP8: Import standard libraries at the top of the file
import math

# PEP8: Avoid extraneous whitespace
value = (1 + 2) * (3 / 4)
print(value)

# PEP8: Use 'is' for None comparisons
def check_none(val):
    if val is None:
        print('Value is None')
    else:
        print('Value is not None')

check_none(None)
check_none(5)

# PEP8: Example of a list comprehension
def get_even_numbers(numbers):
    """Return a list of even numbers from the input list."""
    return [n for n in numbers if n % 2 == 0]

evens = get_even_numbers([1, 2, 3, 4, 5, 6])
print(f"Even numbers: {evens}")

# PEP8: Use single blank line between methods inside a class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hi, I'm {self.name}")

person = Person("Bob")
person.greet()

# PEP8: Use spaces after commas and around operators
result = (1 + 2) * (3 + 4)
print(f"Result: {result}")

# PEP8: Use __name__ == "__main__" guard for script entry points
def main():
    print("This is the main function.")

if __name__ == "__main__":
    main()

# PEP8: Example of proper exception handling
try:
    value = int("abc")
except ValueError as error:
    print(f"Caught an exception: {error}")

# PEP8: Example of using type hints
def multiply(a: int, b: int) -> int:
    """Multiply two integers and return the result."""
    return a * b

print(multiply(3, 4))

# PEP8: Example of using f-strings for formatting
name = "Charlie"
age = 28
print(f"{name} is {age} years old.")

# PEP8: Example of using enumerate for index-value pairs
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Color {index}: {color}")

# PEP8: Example of using zip for parallel iteration
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]
for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# PEP8: Example of using list unpacking
first, *rest = [1, 2, 3, 4]
print(f"First: {first}, Rest: {rest}")

# PEP8: Avoid trailing whitespace and extra blank lines at the end of the file
