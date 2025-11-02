# examples.py
# Example code for virtualenv and testing

# This file demonstrates basic testing with unittest and pytest

def add(a, b):
    return a + b

# Unittest example
import unittest

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

if __name__ == '__main__':
    unittest.main()

# Pytest example (save as test_add.py for pytest to discover)
def test_add_pytest():
    assert add(2, 3) == 5
