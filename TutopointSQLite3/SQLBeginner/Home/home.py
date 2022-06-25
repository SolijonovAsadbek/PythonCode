import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('chinok.db')
cur = conn.cursor()


def attach_database():
    try:
        with conn:
            cur.execute("""ATTACH DATABASE 'chinok.db' as 'testATTACH'""")
            print('Muvaffaqqiyat: Ok')
    except Error as e:
        print(f"Xatolik: {e}")


attach_database()
