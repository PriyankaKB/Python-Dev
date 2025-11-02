# sqlite_example.py
# Examples and explanations for SQLite

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS products (id INTEGER, name TEXT)')
cursor.execute('INSERT INTO products (id, name) VALUES (?, ?)', (1, 'Book'))
cursor.execute('SELECT * FROM products')
print('Products:', cursor.fetchall())
conn.close()
