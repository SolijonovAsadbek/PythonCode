import sqlite3
from employee_class import Employee

# Employee klasidan biz o'zimizga kerakli bo'lgan shaxslarning obyektlarini yaratib olamiz.
# emp1 = Employee('Ergashev', 'Baxtiyor', 2300000)
# emp2 = Employee('Boymirzayev', 'Hojimirza', 2400000)
# emp3 = Employee('Nishonboyev', 'Jamshid', 2500000)
# emp4 = Employee('Turgunov', 'Tursunpolot', 2600000)
# emp5 = Employee('Ne\'matov', 'Abdujalil', 2700000)
# emp6 = Employee('Dedamirzayev', 'Javohir', 2900000)
# emp7 = Employee('Satimbayev', 'Javohir', 2800000)
# emp8 = Employee('Buvahanov', 'Akmal', 2900000)
# emp9 = Employee('Akramov', 'Dilshod', 3000000)
# emp10 = Employee('Alimjanov', 'Alimardon', 3100000)

# *** Connection Databse ***
# Ma'lumotlarni saqlaydigan bazaning manzilini to'g'ri ko'rsatish
# Albatta sizda "/PythonCode/utils/database/" papkalari oldin yaratilgan bo'lishi kerak.
# Ba'zani nomi esa "employees.db" deb nomlanadi barcha yaratmoqchi bo'lgan jadvallariningiz
# shu ba'zada saqlanadi.
conn = sqlite3.connect('/PythonCode/utils/database/employees.db')
# cursor() obyektiga ulanishni amalga oshiramiz.
# cursor() obyekti orqali biz SQL so'rovlarni amalga oshiramiz.
cur = conn.cursor()

# *** CREATE TABLE employee *********************************************************
# 'employees.db' ma'lumotlar bazasiga 'employee' deb nomlangan jadval yaratib olamiz
# ishchilarning ma'lumotlarini saqlash uchun.
# cur.execute("""CREATE TABLE IF NOT EXISTS
# employee (fname message_text ,lname message_text ,pay real)""")

# *** CREATE ******************************************************
# 'employee' deb nomlangan jadval ustunlariga birma-bir qiymatlarni joylashtiramiz quyidagi kod orqali
# Bu 'CRUD' birikmasidagi 'CREATE' iborasiga mos tushadi.
# 1 - usul
# cur.execute("""INSERT INTO employee VALUES (?, ?, ?)""", emp1.unpack)
# conn.commit()

# 2 - usul
# cur.execute("""INSERT INTO employee VALUES (:fname, :lname, :pay)""", emp2.unpack)
# conn.commit()

# 3 - usul
# cur.execute("""INSERT INTO employee VALUES (:fname, :lname, :pay)""",
#             {'fname': emp3.fname, 'lname': emp3.lname, 'pay': emp3.pay})
# conn.commit()

# Quyidagi usullar yordamida o'zgaruvchilarni SQL so'roviga uzatish.
# 4 - 5 - usullar
# cur.execute(f"""INSERT INTO employee VALUES ('{emp4.fname}', '{emp4.lname}', '{emp4.pay}')""")
# cur.execute("""INSERT INTO employee VALUES ("{}", "{}", "{}")""".format(emp5.fname, emp5.lname, emp5.pay))
# conn.commit()

# **** READ *********************************************************
# Ma'lumotlar bazasidagi barcha ma'lumotlarni ko'rish so'rovlari va ma'lumotlarni ko'rsatishga 'limit' qo'yish
# 1 - usul
# rows = cur.execute("""SELECT * FROM employee""")
# print(rows)
# print(list(rows))
# print(len(list(rows)))
# print(set(rows))
# set() -funktsiyasi ba'zadagi ikkita bir xil ma'lumotni bitta qilib berish uchun ishlatildi.
# for row in set(rows):
#     print(row)

# 2 - usul
# objects = cur.execute("""SELECT * FROM employee""").fetchone()
# objects1 = cur.execute("""SELECT * FROM employee""").fetchmany(3)
# objects2 = cur.execute("""SELECT * FROM employee""").fetchall()
# agar size qiymati yozilmasa default holatda size=1 deb oladi (fetchone() is a fetchmany())
# objects3 = cur.execute("""SELECT * FROM employee""").fetchmany()
# print(objects)
# print(objects1)
# print(objects2)
# print(objects3)
# for obj in objects:
#     print(obj)

# 3 - usul
# Kesib olib usuli
# objects = cur.execute("""SELECT * FROM employee""")
# objects1 = objects.fetchone()
# objects2 = objects.fetchmany(3)
# objects3 = objects.fetchall()
# print(objects1)
# print(objects2)
# print(objects3)


# Ma'lumotlar bazasidan faqatgina keralilarini qidirib topish.

# 1 - usul
# objects = cur.execute("""SELECT * FROM employee WHERE fname='Ergashev'""").fetchall()
# print(objects)

# 2 - usul
# objects = cur.execute("""SELECT * FROM employee WHERE fname=?""", (emp1.fname,)).fetchall()
# print(objects)

# 3 - usul
# objects = cur.execute("""SELECT * FROM employee WHERE fname=:fname and lname=:lname""",
#                       (emp1.fname, emp1.lname)).fetchall()
# print(objects)

# 4 - usul dict
# objects = cur.execute("""SELECT * FROM employee WHERE fname=:fname and lname=:lname""",
#                       {'fname': emp1.fname, 'lname': emp1.lname}).fetchall()
# print(objects)


# *** UPDATE  *********************************************************
# cur.execute("""UPDATE employee SET pay=:pay WHERE fname=:fname  and lname=:lname""",
#             {'fname': emp2.fname, 'lname': emp2.lname, 'pay': 5500000})
# conn.commit()

# *** DELETE **********************************************************
# cur.execute("""DELETE FROM employee WHERE fname=:fname and lname=:lname""",
#             {'fname': emp1.fname, 'lname': emp1.lname})
# conn.commit()

conn.close()
