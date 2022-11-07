import sqlite3
import pandas

connection = sqlite3.connect("035-SQL-with-python/database.db")
cursor = connection.cursor()

new_rows = [
    ("1385298725", "hello", 134),
    ("3857827358", "example", 173),
]

cursor.executemany("INSERT INTO 'ips' VALUES(?,?,?)", new_rows)
connection.commit()

cursor.execute("SELECT * FROM 'ips'")
print(cursor.fetchall())