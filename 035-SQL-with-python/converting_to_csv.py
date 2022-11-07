import sqlite3
import pandas

connection = sqlite3.connect("035-SQL-with-python/database.db")
cursor = connection.cursor()

dataframe = pandas.read_sql_query("SELECT * FROM 'ips' ORDER BY asn", connection)
print(dataframe)

# The index is the first column of the printed out dataframe above
dataframe.to_csv("035-SQL-with-python/database.csv", index=None)
dataframe.to_excel("035-SQL-with-python/database.xlsx", index=None)