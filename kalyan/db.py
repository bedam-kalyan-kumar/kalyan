import sqlite3
connection=sqlite3.connect("kalyan.db")
cursor=connection.cursor()

# cursor.execute("INSERT INTO Login(USERNAME,PASSWORD) VALUES (?,?)",('KALYAN',"K@1alyan"))   

cursor.execute("SELECT * FROM Login")
rows=cursor.fetchall()
for row in rows:
    print(row)
connection.commit()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

tables = cursor.fetchall()

for table in tables:
    print(table[0])
connection.close()