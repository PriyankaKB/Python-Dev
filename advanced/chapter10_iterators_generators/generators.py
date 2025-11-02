# generators.py
# Examples and explanations for generators

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
for num in gen:
    print('Countdown:', num)
