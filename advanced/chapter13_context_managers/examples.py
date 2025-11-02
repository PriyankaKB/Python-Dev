# examples.py
# Example code for context managers

# Using a built-in context manager
with open('test.txt', 'w') as f:
    f.write('Hello, context manager!')

# Custom context manager
class MyContext:
    def __enter__(self):
        print('Entering context')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exiting context')

with MyContext():
    print('Inside context')
