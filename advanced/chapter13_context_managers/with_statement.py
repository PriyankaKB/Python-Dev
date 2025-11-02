# with_statement.py
# Examples and explanations for the with statement

with open('sample.txt', 'w') as file:
    file.write('Hello, world!')

with open('sample.txt', 'r') as file:
    content = file.read()
    print('File content:', content)
