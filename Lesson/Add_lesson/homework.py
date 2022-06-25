# match-case 1
# n = int(input("n="))
# match n:
#     case 1:
#         print("dushanba")
#     case 2:
#         print("Seshanba")
#     case 3:
#         print("chorshanba")
#     case 4:
#         print("Payshanba")
#     case 5:
#         print("Juma")
#     case 6:
#         print("Shanba")
#     case 7:
#         print("Yakshanba")
#     case _: print("Kiritilgan son 7 dan oshib ketti")


# math-case 5
# a = int(input("a="))
# b = int(input("b="))
# amal = int(input("amal="))
# match amal:
#     case 1:
#         print(a + b)
#     case 2:
#         print(a - b)
#     case 3:
#         print(a * b)
#     case 4:
#         if b != 0:
#             print(a / b)
#         else:
#             print("b ni 0 ga teng emas qilib kiriting")
#     case _: print("bumday amal yoq 1-4gacha kirit ")


# match-case 10
# y = input("y=")
# k = int(input("k="))
# s = ""
# match y:
#     case "s":
#         s += "shimol "
#     case "j":
#         s += "janub "
#     case "q":
#         s += "sharq "
#     case "g":
#         s += "g'arb "
# match k:
#     case 0:
#         s = s + "Harakatni davom ettir"
#     case 1:
#         s = s + "Chapga buril"
#     case 2:
#         s = s + "O'nga buril"
#     case _:
#         s = s + "Bunday harakat yo'q"
# print(s)

# match-case 15
# n = int(input("Karta qiymatini kiriting: "))
# m = int(input("karta qiymati: "))
# s = ""
# match n:
#     case 1:
#         print("Bir", end=" ")
#     case 2:
#         print("ikki", end=" ")
#     case 3:
#         print("uch", end=" ")
#     case 4:
#         print("to'rt", end=" ")
#     case 5:
#         print("besh", end=" ")
#     case 6:
#         print("olti", end=" ")
#     case 7:
#         print("yetti", end=" ")
#     case 8:
#         print("sakkiz", end=" ")
#     case 9:
#         print("to'qqiz", end=" ")
#     case 10:
#         print("O'n", end=" ")
#     case 11:
#         print("valet", end=" ")
#     case 12:
#         print("Dama", end=" ")
#     case 13:
#         print("Qirol", end=" ")
#     case 14:
#         print("tuz", end=" ")
# match m:
#     case 1:
#         print("Qarg'a")
#     case 2:
#         print("g'isht")
#     case 3:
#         print("olma")
#     case 4:
#         print("chillak")

# mathc-case 19
# yil = int(input("Yil: "))
# CONST = 1984
# rang = abs(yil - CONST) % 5
# muchal = abs(CONST - yil) % 12
# muchal_yil = ""
# match rang:
#     case 0:
#         muchal_yil += "Yashil "
#     case 1:
#         muchal_yil += "Qizil "
#     case 2:
#         muchal_yil += "Sariq "
#     case 3:
#         muchal_yil += "Oq "
#     case 4:
#         muchal_yil += "Qora "
#
# match muchal:
#     case 0:
#         muchal_yil += "Sichqon"
#     case 1:
#         muchal_yil += "Sigir"
#     case 2:
#         muchal_yil += "Yo'lbars"
#     case 3:
#         muchal_yil += "Quyon"
#     case 4:
#         muchal_yil += "Ajdar"
#     case 5:
#         muchal_yil += "Ilon"
#     case 6:
#         muchal_yil += "Ot"
#     case 7:
#         muchal_yil += "Qo'y"
#     case 8:
#         muchal_yil += "Maymun"
#     case 9:
#         muchal_yil += "Tovuq"
#     case 10:
#         muchal_yil += "It"
#     case 11:
#         muchal_yil += "To'ng'iz"
# print(muchal_yil)

# while-5
# n = int(input("Ikkini qandaydir darajasi: "))
# k = 1
# m = 2
# s = ""
# while m <= n:
#     if m == n:
#         s += f"daraja: {k}"
#         break
#     m *= 2
#     k += 1
# if s != "":
#     print(s)
# else:
#     print(f"{n} ikkini darajasi emas.")

# while 10
# n = int(input("n="))
# k = 1
# m = 3
# s = ""
# while m <= n:
#     if m == n:
#         s += f"eng katta daraja: {k}"
#         break
#     m *= 3
#     k += 1
#     if m > n:
#         s += f"eng katta daraja: {k - 1}"
#         break
#     else:
#         continue
# print(s)

# wwhile-15
# s = float(input("Summani kiriting: "))
# p = float(input("Nechchi foiz: "))
# sum = s
# oy = 1
# str_oy = ""
# while sum <= 2 * s:
#     sum += sum * (p / 100)
#     if sum == 2 * s:
#         str_oy += f"roppa rosa {oy} oy"
#         break
#     oy += 1
#     if sum > 2 * s:
#         str_oy += f"taqriban {oy - 1} oydan oshiqroq vaqtda"
#         break
#     else:
#         continue
# print(str_oy)

# while-20
# n = int(input("Butun son: "))
# list = []
# m = n
# ikki_soni = 0
# while n > 0:
#     qoldiq = n % 10
#     n = n // 10
#     if qoldiq == 2:
#         ikki_soni += 1
#         list.append(qoldiq)
#         continue
# print(f"{m} soni ichida ikki raqami {ikki_soni} marta qatnashgan.")
# print(list)

# Kiritilgan son o'chamiga mos list hozil qilish
# n = int(input("n: "))
# list_ = list(range(n))
# print(list_)

# Eng kichik va eng katta sonni aniqlash funksiyasi
# list__ = [12, 32, 34, 34322, 324, 120, 234123, 15]
# print("eng kichik son", min(list__))
# print("eng katta son", max(list__))


# MinMax8
# n = int(input("n: "))
# asil = []
# for i in range(1, n + 1):
#     a = float(input(f"a{i}: "))
#     asil.append(a)
#
# notasil = asil[:]
# max_ = notasil[0]
# min_ = notasil[0]
# for i in range(n):
#     if max_ <= notasil[i]:
#         max_ = notasil[i]
#
#     if min_ >= notasil[i]:
#         min_ = notasil[i]
# print("max: ", max_)
# print("min: ", min_)
# print(asil)
# print("katta sonni index: ", asil.index(max_))
# print("kichik sonni index: ", asil.index(min_))


# MinMax6 1-variant
# numbers = [1, 23, 34, 56, -2, 0, -34]   # elementlar soni toq
# numbers = [0, 1, 23, 34, -2, 100, -34, 56]  # elementlar soni juft
# mid = len(numbers) // 2
# start_3 = numbers[:mid]
# end_3 = numbers[mid:]
# max_ = end_3[0]
# min_ = start_3[0]
# for i in range(mid):
#     if min_ >= start_3[i]:
#         min_ = start_3[i]
#     if max_ <= end_3[i]:
#         max_ = end_3[i]
#
# print(numbers)
# print(f"birinchi yarmi: {start_3}")
# print(f"ikkinchi yarmi: {end_3}")
# print(f"birinchi uchragan eng kichik son: {min_} indeksi: {numbers.index(min_)}")
# print(f"birinchi uchragan oxirgi eng katta son: {max_} indeksi: {numbers.index(max_, mid)}")


# MinMax6 2-variant
# numbers = [1, 23, 34, 56, -2, 0, -34]   # elementlar soni toq
# numbers = [0, 1, 23, 34, 56, -2, 0, -34]  # elementlar soni juft
# start_3 = numbers[:3]
# end_3 = numbers[-3:]
# max_ = end_3[0]
# min_ = start_3[0]
# for i in range(3):
#     if min_ >= start_3[i]:
#         min_ = start_3[i]
#     if max_ <= end_3[i]:
#         max_ = end_3[i]
#
# print(numbers)
# print(f"birinchi yarmi: {start_3}")
# print(f"ikkinchi yarmi: {end_3}")
# print(f"birinchi uchragan eng kichik son: {min_} indeksi: {numbers.index(min_)}")
# print(f"birinchi uchragan oxirgi eng katta son: {max_} indeksi: {numbers.index(max_, -3)}")
