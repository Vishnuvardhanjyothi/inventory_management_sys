import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="VISHnu@2004",
    database="inventory_management"
)

cur = con.cursor(buffered=True)
print("Database connected successfully")

