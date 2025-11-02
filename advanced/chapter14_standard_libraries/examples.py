# examples.py
# Example code for standard libraries

import os
import sys
import datetime
import json

# OS example
print('Current directory:', os.getcwd())

# SYS example
print('Python version:', sys.version)

# Datetime example
now = datetime.datetime.now()
print('Current time:', now)

# JSON example
data = {'name': 'Alice', 'age': 30}
json_str = json.dumps(data)
print('JSON string:', json_str)
