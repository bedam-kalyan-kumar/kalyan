# Reconnect and verify the updated structure and data
import sqlite3
conn = sqlite3.connect('kalyan.db')
cursor = conn.cursor()

# Check the table structure
cursor.execute('PRAGMA table_info(project1_login);')
columns = cursor.fetchall()
print("Table Structure:")
for column in columns:
    print(column)

# Check the data in the updated table
cursor.execute('SELECT id,username, password,gmail,image,video FROM project1_login;')
rows = cursor.fetchall()
print("\nData in the Table:")
for row in rows:
    print(row)

conn.close()
