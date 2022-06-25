# sqlite3 modulini chaqirib olamiz
import sqlite3

# example.db deb nomlangan file da hamma ma'lumotlar
# saqlanadi biz hozir unga ulanishni amalga oshirdik
con = sqlite3.connect('example.db')

cur = con.cursor()

# Jadval yaratish
cur.execute('CREATE TABLE IF NOT EXISTS stocks\n'
            '               (date text, trans text, symbol text, qty real, price real)')

# Ma'lumotlar qatorini kiriting
cur.execute('INSERT INTO stocks VALUES (\'2006-01-05\',\'BUY\',\'RHAT\',100,35.14)')

# O'zgarishlarni saqlang (majburiy qiling).
con.commit()

# Agar biz u bilan ishlagan bo'lsak, ulanishni ham yopishimiz mumkin.
# Har qanday o'zgarishlar kiritilganligiga ishonch hosil qiling, aks holda ular yo'qoladi.
con.close()


