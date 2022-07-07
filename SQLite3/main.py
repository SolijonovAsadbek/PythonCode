import sqlite3

con = sqlite3.connect('D:/DB/chinook/chinook.db')
cur = con.cursor()


def search(name):
    return cur.execute("""SELECT * FROM customers WHERE FirstName=?""", (name,)).fetchall()

