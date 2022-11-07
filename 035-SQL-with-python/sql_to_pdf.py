import sqlite3
from fpdf import FPDF

connection = sqlite3.connect("035-SQL-with-python/database.db")
cursor = connection.cursor()

cursor.execute("PRAGMA table_info(ips)")
# Returns list of tuples (representing columns) - gives column attributes 
columns = cursor.fetchall()
print(columns)

# portrait, points, 14
pdf = FPDF(orientation="P", unit="pt", format="A4")
pdf.add_page()

# First row with headers
for column in columns:
    pdf.set_font(family="Times", style="B", size=14)
    # column[1] == column names
    pdf.cell(w=100, h=25, txt=column[1], border=1)

# New line
pdf.ln()

cursor.execute("SELECT * FROM 'ips'")
rows = cursor.fetchall()

for row in rows:
    for element in row:
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=100, h=30, txt=str(element), border=1)
    pdf.ln()

pdf.output("035-SQL-with-python/output.pdf")