import sqlite3

conn = sqlite3.connect('example.db')

conn.execute('''PRAGMA foreign_key = ON''')
cur = conn.cursor().execute('''SELECT * FROM PATIENT WHERE DOCTOR_ID=2''')
for row in cur:
    print(row)

conn.close()
