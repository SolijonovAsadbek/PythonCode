import sqlite3

# yaratilgan 'example.db' deb nommlangan ma'lumotlar
# bazasiga ulanishni amalga oshirib olamiz.
con = sqlite3.connect('example.db')
cur = con.cursor()

# for sikl yordamida biz ma'lumotlar bazasidagi barcha ma'lumotlarni o'qib olamiz
# for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
#     print(row)

# faqat kerak ma'lumotlarni ko'rish uchun quyidagicha sql so'rovini yuboramiz
# for row in cur.execute('SELECT symbol, qty, price  FROM stocks ORDER BY price'):
#     print(row)

# yuqorida for sikl ishlatildi endi uni for siklsiz to'la ko'rish uchun nima qilinadi.
# qtyobj = cur.execute("SELECt * FROM stocks WHERE qty=100")
# print(tuple(qtyobj), type(qtyobj))  # qty=100 ga teng bo'lgan barcha elementlarni 'tuple'da
# chiqarish uchun ishlatiladi
# print(list(qtyobj))  # qty=100 ga teng bo'lganlarni barchasini 'list'da o'rab chiqaradi.
# print(set(qtyobj))  # qty=100 ga teng bo'lganlarni barchasini 'set'da o'rab chiqaradi.
# Agar obyektlarni ichida bir xil elementlar bo'lsa uni bitta qilib olib ketadi.

# Yodda tuting: qtyobj obyektlarini to'la olib bo'lgandan keyin, yana uni ishlatish yaroqsiz bo'lib qoladi.
# Yana qayta chiqarish uchun SQL so'rovini jo'natish talab qilinadi.

# print(qtyobj.fetchmany(2))  # Limitni ko'rsatishda ishlatiladi.
# print(qtyobj.fetchone())  # Faqat bittasini qidirib topishda ishlatiladi
# print(qtyobj.fetchall())  # Hammasini qidirishda topishda ishlatiladi.
