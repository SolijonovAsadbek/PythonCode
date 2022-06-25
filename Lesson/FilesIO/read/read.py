# 'r' - 'data.txt' faylga o'qish rejimini yoqib beradi.
# with open('data.txt', 'r') as mening_faylim:
#     obj = mening_faylim.read()
# print(obj)


# 'w' - 'data.txt' faylga ma'lumot yozishda ishlatiladi.
# Agar ma'lumotlar 'data.txt' faylida mavjud bo'lsa, ular yangi ma'lumotga o'zgaritiriladi.
# Eski ma'lumotlar o'chirilib yuboriladi.
# with open('data.txt', 'w') as file:
#     data = 'Bugun Abduqodir darsga 10:30 keldi.\nDarsga kech qolmang deb ustozi ogohlantirdi.'
#     file.write(data)

# 'a' - data.txt fayliga ma'lumotlarni o'chirmasdan, yangi ma'lumotlarni qo'shishda ishlatiladi.
# with open('data.txt', 'a') as file:
#     data = "\nAbduqodir boshqa takrotlanmaydi dedi."
#     file.write(data)

# Biror bir papkaga fayl yaratish.
# with open('/PythonCode/Lesson/FilesIO/datas2.txt', 'a') as file:
#     pass



# with open('D:/install/Beginning Django E-Commerce - Free Pdf Book.pdf', encoding="utf8", mode="rb") as file:
#     obj = file.read()
#
# print(obj)

