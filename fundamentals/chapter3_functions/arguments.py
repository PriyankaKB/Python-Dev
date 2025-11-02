# arguments.py
# Examples and explanations for function arguments

def add(a, b):
    return a + b

print('Sum:', add(3, 5))

def describe_person(name, age=30):
    print(f"Name: {name}, Age: {age}")

describe_person("Bob")
describe_person("Carol", 22)
