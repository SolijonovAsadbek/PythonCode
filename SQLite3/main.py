import sqlite3

con = sqlite3.connect('D:/DB/chinook/chinook.db')
cur = con.cursor()


def records(name):
    return cur.execute("""SELECT * FROM customers WHERE FirstName=?""", (name,)).fetchall()


