# examples.py
# Example code for file I/O

# Writing to a file
with open('output.txt', 'w') as f:
    f.write('Hello, file!')

# Reading from a file
with open('output.txt', 'r') as f:
    content = f.read()
    print('File content:', content)
