import sqlite3 as sl

con = sl.connect('my-test.db')

with con:
  con.execute("""
    CREATE TABLE IF NOT EXISTS USER (
      id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      age INTEGER
    );
    """)

# sql = 'INSERT INTO USER (id, name, age) VALUES(?, ?, ?)'
# data = [
#   (1, 'Alice', 21),
#   (2, 'Bob', 22),
#   (3, 'Chris', 23)
# ]

sql = 'INSERT INTO USER (name, age) VALUES(?, ?)'
data = [
  ('Frank', 57),
  ('Tim', 36)
]

with con:
  con.executemany(sql, data)
