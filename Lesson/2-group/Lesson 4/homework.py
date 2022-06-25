# xa = float(input("xa: "))
# ya = float(input("ya: "))
# xb = float(input("xb: "))
# yb = float(input("yb: "))
# xc = float(input("xc: "))
# yc = float(input("yc: "))
#
# xd = xb - xa + xc
# yd = yb - ya + yc
# print(f"A koordinata: ({xa}, {ya})")
# print(f"B koordinata: ({xb}, {yb})")
# print(f"C koordinata: ({xc}, {yc})")
# print("Natija".center(26,'='))
# print(f"D koordinata: ({xd}, {yd})")


# 27-masala
# a = float(input("Son: "))
# a = round(a)
# print("Yaxlit: ", a)
# if a % 2 == 0:
#     print(1)
# else:
#     print(-1)

# 28- masala
# a = int(input("Yil: "))
#
# kabisa = a % 4 == 0 and a % 100 == 0 and a % 400 == 0
# if kabisa:
#     print(f"{a} yilda 366 kun bor")
# else:
#     print(f"{a} yilda 365 kun bor")

# 29-30-masala
# a = int(input("Son: "))
#
# if a > 0:
#     print("Musbat,", end=" ")
#     if a % 2 == 0:
#         print("Juft, ", end=" ")
#     else:
#         print("Toq, ", end=" ")
#     print(f"{len(str(a))} xonali son.")
# elif a < 0:
#     print("Manfiy, ", end=" ")
#     if a % 2 == 0:
#         print("Juft, ", end=" ")
#     else:
#         print("Toq, ", end=" ")
#     print(f"{len(str(a))-1} xonali son.")
# else:
#     print("Nol ga teng!")

# Mavzu: While operator
# n = 10
# while n > 0:
#     n -= 1
#     if n % 2 == 1:
#         print(n, end=', ')
#         # break
# else:
#     print("Break !")
# print("not else Break!")

# while True:
#     x = input("Son1: ")
#     if x == "":
#         break
#     y = input("Son2: ")
#     print(f"{x}*{y} = {float(x) * float(y)}")
# print("Turn off!")
#
# import random
# week_days = ['Dushanba', 'Seshanba', 'Chorshanba', 'Payshanba', 'Juma', 'Shanba', 'Yakshanba']
# x = random.randint(0, 7)
# week_day = week_days[x]
# n = 0
# w_n = len(week_days)
# while n < w_n:
#     if week_day.capitalize() in week_days:
#         week_days.remove(f"{week_day.capitalize()}")
#         w_n = len(week_days)
#         continue
#     print(week_days[n])
#     n += 1
# else:
#     print(f"{week_day} dam olish kuni")

a = 'ali', 1, 2, 3, 45
print(a)