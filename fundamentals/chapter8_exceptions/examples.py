# examples.py
# Example code for exceptions

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")

try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

# Custom exception
class NegativeNumberError(Exception):
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Number must be positive")

try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)
