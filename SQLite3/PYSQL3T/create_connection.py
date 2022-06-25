import datetime
import sqlite3
# Baza bilan kelib chiqadigan xatoliklarni nomi bilish uchun Error klasini chaqirib olamiz.
from sqlite3 import Error

# Quyidagi kod orqali biz '/PythonCode/utils/database/' papkada 'mydatabase.db'
# deb nomlangan fayl yaratib olamiz
conn = sqlite3.connect('D:/DB/chinook/chinook.db')
# cursor obyektini yaratib olamiz.
# 'cur' obyekti  yordamida biz ma'lumotlar bazasiga tur xil SQL so'rovlar yuboramiz.
# Agar bu obyekt bo'lmasa biz hech qanday obyektni SQL so'rovini jo'nata olmaysiz.
cur = conn.cursor()


# Ma'lumotlar bazasida jadvallar nechtaligini bilish uchun quyidagi usulni bajaring.
def all_tables_name():
    try:
        with conn:
            rows = cur.execute("""SELECT name FROM sqlite_master WHERE type='table'""").fetchall()
            print(f"Muvoffaqqiyat: 'chinook.db' dagi barcha yaratilgan jadvallar nomi:\n{rows}")
    except Error as e:
        print(f"Xatolik: {e}")


# all_tables_name()


# Jadvalni yaratishda biz jadval mavjud emasligiga ishonch hosil qilishimiz kerak.
# Xuddi shunday, jadvalni olib tashlash/o'chirishda jadval mavjud bo'lishi kerak.
# 'IF NOT EXISTS' - (Agar yo'q bo'lsa) dan foydalanamiz.
def create_table():
    try:
        with conn:
            cur.execute("""CREATE TABLE testbase (id integer primary key autoincrement not null , 
                                                fname text not null ,
                                                lname text null ,
                                                joiningdate timestamp not null )""")
            print("Muvoffaqqiyat: 'chinook.db' ga 'testbase' jadvali muvoffaqqiyat yaratildi.")
    except Error as e:
        print(f"Xatolik: {e}")


# create_table()


# Bazaga (id, fname, lname, joiningdate) ma'lumotlarini yozuvchi funksiya.
def insert_table(id, fname, lname, joiningdate):
    try:
        with conn:
            cur.execute(
                f"""INSERT INTO testbase (id, fname, lname, joiningdate) VALUES (?, ?, ?, ?)""",
                (id, fname, lname, joiningdate))
    except Error as e:
        print(f"Xatolik: {e}")


# insert_table(1, 'Asadbek', 'Solijonov', datetime.datetime.now())
# insert_table(2, 'Javlon', 'Eshmatov', datetime.datetime.now())
# insert_table(3, 'Jasur', 'Shomuradov', datetime.datetime.now())
# insert_table(4, 'Jamshid', 'Nishonboyev', datetime.datetime.now())
# insert_table(5, 'Otabek', 'Bahriddinov', datetime.datetime.now())
# insert_table(6, 'Jobir', 'Dedaboyev', datetime.datetime.now())
# insert_table(7, 'Abbos', 'Eshmatov', datetime.datetime.now())
# insert_table(8, 'Elmurod', 'Haqnazarov', datetime.datetime.now())
# insert_table(9, 'Dilshobek', 'Kattabekov', datetime.datetime.now())
# insert_table(10, 'Botir', 'Ziyatov', datetime.datetime.now())


# rowcount - ni satrlar nechtaligini bilish uchun ishlatiladi. Lekin uni SELECT bilan ishlatilsa u doim -1
# qaytaradi. CHunki hech qanday satr tanlanmagan. Shuning uchun 'rowcount' o'rniga 'fetchall' dan foydalanishimiz kerak.
def table_rowcount():
    try:
        with conn:
            # rowc = cur.execute("""SELECT * FROM testbase""").rowcount
            rowc = cur.execute("""SELECT * FROM testbase""").fetchall()
            print(f"Muvoffaqqiyat: 'testbase' jadvalida {len(rowc)} ta qator ma'lumot bor.")
    except Error as e:
        print(f"Xatolik: {e}")


# table_rowcount()


# 'rowcount' agar 'DELETE' bilan birga ishlatilsa u o'chirilgan satrlarning sonini qaytaradi.
def delete_rows():
    try:
        with conn:
            rowc = cur.execute("""DELETE FROM testbase""").rowcount
            print(f"Muvoffaqqiyat: 'testbase' jadvalidan {rowc} ta qator o'chirildi. Jadval to'la tozalandi.")
    except Error as e:
        print(f"Xatolik: {e}")


# delete_rows()


# Ma'lumotlar bazasidan 'testbase' jadvalini to'liq nomi va ma'lumotlari bilan olib tashlash.
# Jadvalni o'chirishdan oldin 'testbase' jadvali bazada mavjud bo'lishi kerak.
# Yo'q bo'lib qolish ehtimolligi bo'lgani uchun 'IF EXISTS' so'rovi yoziladi.
# Bu agar 'testbase' jadvali bor bo'lsa o'chir degan ma'noni beradi.
def drop_table():
    try:
        with conn:
            cur.execute("""DROP TABLE testbase""")
            # cur.execute("""DROP TABLE IF EXISTS testbase""")
            print("Muvoffaqqiyat: 'testbase' jadvali to'liq olib tashlandi.")
    except Error as e:
        print(f"Xatolik: {e}")


# drop_table()


# Ommay kiritish usuli. Ajoyib va tezkor usullardan biri.
# Bir vaqtning o'zida bir nechta qatorlarni kiritish uchun 'executemany' iborasidan foydalanamiz.
# 'execute' funksiyasi ma'lumotlarni novbatdan yozadi,
# 'executemany' funksiyasi esa bir vaqtni o'zida bir nechta ma'lumotni yoza oladi.
def executemany_rows(data):
    try:
        with conn:
            cur.executemany("""INSERT INTO testbase VALUES (?, ?, ?, ?)""", data)
            print(f"Muvaffaqqiyat: 'testbase' ga bir qancha qator ma'lumotlar qo'shildi.")
    except Error as e:
        print(f"Xatolik: {e}")


data = [
    (11, 'Jalil', 'Bahodirov', datetime.datetime.now()),
    (12, 'Abdurahmon', 'Boydullayev', datetime.datetime.now()),
    (13, 'Akram', 'Nusratov', datetime.datetime.now()),
    (14, 'Gulmira', 'Nosirova', datetime.datetime.now()),
    (15, 'Abdullajon', 'Farmonov', datetime.datetime.now()),
]


# executemany_rows(data)

# Ma'lumotlar bazasiga datetime yozishning yana bir sodda usullaridan biri.
def create_table_for_time(obj):
    try:
        with conn:
            cur.execute("""CREATE TABLE IF NOT EXISTS essignment 
            (id integer primary key not null ,name text, day date)""")
            print("Muvaffaqiyat: 'essignment' bazasi yartildi.")
            cur.executemany("""INSERT INTO essignment (id, name, day) VALUES (?, ?, ?)""", obj)
            print("Muvaffaqqiyat: ''essignment' bazasiga bir nechta ma'lumotlar qo'shildi.")
    except Error as e:
        print(f"Xatolik: {e}")


datas = [
    (1, 'Alisher', datetime.date(2022, 1, 2)),
    (2, 'Bahodir', datetime.date(2022, 3, 4)),
    (3, 'Alijon', datetime.date(2022, 2, 1)),
    (4, 'Valijon', datetime.date(2022, 2, 4)),
    (5, 'Qodir', datetime.date(2022, 4, 4)),
    (6, 'Bahrom', datetime.date(2022, 5, 4))
]

create_table_for_time(datas)


# Ma'lumotlar bazasidan ma'lumotlarni saralab chiqarishning ORDER BY usuli.
def order_by_essigenmnt():
    try:
        result = cur.execute("""SELECT * FROM essignment ORDER BY name""").fetchall()
        print(result)
    except Error as e:
        print(f"Xatolik: {e}")


order_by_essigenmnt()
# Ma'lumotlar ba'zasi bilan ishlashni tugatganingizdan so'ng, uni close() bilan yopish bu yaxshi odatdir.
# Bu sizning ma'lumotlar bazangizga zarar yetkazmaslik uchun hizmat qilaadi.
conn.close()
