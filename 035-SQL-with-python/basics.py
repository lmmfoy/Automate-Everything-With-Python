import sqlite3

# Create connection + cursor
connection = sqlite3.connect("035-SQL-with-python/database.db")
cursor = connection.cursor()

# Get all rows and columns, ordered
cursor.execute("SELECT * FROM 'ips' ORDER BY asn")
# Output is a list of tuples(which represent rows)
# fetchall can only be used once per query
print(cursor.fetchall())

# All rows, and 2 columns
cursor.execute("SELECT address, asn FROM 'ips' ORDER BY asn")
print(cursor.fetchall())

# Rows where asn < 300
cursor.execute("SELECT * FROM 'ips' WHERE asn < 300")
print(cursor.fetchall())

# Rows where asn == 144
cursor.execute("SELECT * FROM 'ips' WHERE asn == 144")
print(cursor.fetchall())

# Rows where asn < 300 and "sa" at end of domain name (% = any number of characters followed by "sa")
cursor.execute("SELECT * FROM 'ips' WHERE asn < 300 AND domain LIKE '%sa'")
results = cursor.fetchall()

for row in results:
    print(row)