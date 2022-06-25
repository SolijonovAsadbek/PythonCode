import sqlite3
from employee_class import Employee

# Employee klasi yordamida ishchilarning ma'lumotlari obyektlarini yaratib olamiz.
emp1 = Employee('Ergashev', 'Baxtiyor', 2300000)
# emp2 = Employee('Boymirzayev', 'Hojimirza', 2400000)
# emp3 = Employee('Nishonboyev', 'Jamshid', 2500000)
# emp4 = Employee('Turg\'unov', 'Tursunpo\'lot', 2600000)
# emp5 = Employee('Ne\'matov', 'Abdujalil', 2700000)
# emp6 = Employee('Dedamirzayev', 'Javohir', 2900000)
# emp7 = Employee('Satimbayev', 'Javohir', 2800000)
# emp8 = Employee('Buvahanov', 'Akmal', 2900000)
# emp9 = Employee('Akramov', 'Dilshod', 3000000)
# emp10 = Employee('Alimjanov', 'Alimardon', 3100000)

# *** Connection Databse ***
# "/PythonCode/utils/database/" quyidagi manzilga 'employees.db' deb nomlangan ba'zani yataib olamiz.
# biz yaratgan hamma jadvallar shu bazaga saqlanib boradi.
conn = sqlite3.connect('/PythonCode/utils/database/employees.db')
cur = conn.cursor()

# 'employees.db' bazasida 'employee' deb nomlangan jadval yaratib olamiz.
cur.execute("""CREATE TABLE IF NOT EXISTS
employee (fname message_text ,lname message_text ,pay real)""")


# Bu funksiya ma'lumotlar bazasi shaxsga tegishli bo'lgan uchta ustuniga turli xil qiymatlar yozadi.
# CREATE
def insert_into(obj):
    with conn:
        cur.execute("""INSERT INTO employee VALUES (?, ?, ?)""", obj.unpack)


# Bu funksiya ma'lumotlar bazasidan shaxsning 'fname' yordamida barcha ma'lumotlarini qidirib topadi.
# READE
def search_fname(fname):
    with conn:
        result = cur.execute("""SELECT * FROM employee WHERE fname=?""", (fname,)).fetchall()
    return result


# Bu funktsiya shaxsning 'fname va lname' yordamida 'pay' maoshini o'zgartiradi
# UPDATE
def update_pay(obj, pay):
    with conn:
        cur.execute("""UPDATE employee SET pay=:pay WHERE fname=:fname  and lname=:lname""",
                    {'fname': obj.fname, 'lname': obj.lname, 'pay': pay})


# bu funksiya ma'lumotar bazasidan shxasning 'fname va lname' orqali qidirib uning ma'lumotlar satrini o'chiradi.
# DELETE
def del_fname_lname(obj):
    with conn:
        cur.execute("""DELETE FROM employee WHERE fname=:fname and lname=:lname""",
                    {'fname': obj.fname, 'lname': obj.lname})

# Biz yaratgan yuqorida funksiyalar to'g'ri yoki noto'g'rimi tekshirib ko'rish uchun
# turli qiymatlarni yozib tekshirib ko'ramiz.
# insert_into(emp1)
# insert_into(emp6)
# update_pay(emp1, 10000000)
# update_pay(emp2, 20000000)
# result = search_fname(emp1.fname)
# print(result)
# del_fname_lname(emp1)
