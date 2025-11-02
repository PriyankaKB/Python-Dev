# examples.py
# Example code for databases

import sqlite3

# SQLite example
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INTEGER, name TEXT)')
cursor.execute('INSERT INTO users VALUES (?, ?)', (1, 'Alice'))
cursor.execute('SELECT * FROM users')
print('Users:', cursor.fetchall())
conn.close()
