# examples.py
# Example code for decorators

def simple_decorator(func):
    def wrapper():
        print('Before function call')
        func()
        print('After function call')
    return wrapper

@simple_decorator
def greet():
    print('Hello!')

greet()

# Decorator with arguments
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print('Hi!')

say_hi()
