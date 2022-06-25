# if 13
# 1-usul
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
# if a != b != c:
#     if a <= b <= c or c <= b <= a:
#         print(b)
#     elif b <= c <= a or a <= c <= b:
#         print(c)
#     else:
#         print(a)
# else:
#     print("Hech biri teng emas bo'lsin.")

# 2-usul
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
# if a == b or a == c or b == c:
#     print("Hech biri teng emas bo'lsin.")
# else:
#     if a > b:
#         if a > c:
#             if b > c:
#                 print(b)
#             else:
#                 print(c)
#         else:
#             print(a)
#     else:
#         if b > c:
#             if a > c:
#                 print(a)
#             else:
#                 print(c)
#         else:
#             print(b)

# if 28
# a = int(input("Yil: "))
# if a % 4 == 0 and a < 399:
#     print("366 kun bor.")
# elif a % 100 == 0 and a % 400 == 0:
#     print(366, "Kun bor.")
# else:
#     print(f"{365} kun bor.")


# match case  "Qo'shimcha misol"
# a = int(input("son: "))
#
# n = a % 6
# s = ""
# match n:
#     case 1:
#         s += "Qoldiq bir"
#     case 2:
#         s += "Qoldiq ikki"
#     case 3:
#         s += "Qoldiq uch"
#     case 4:
#         s += "Qoldiq to'rt"
#     case 5:
#         s += "Qoldiq besh"
#     case _:
#         print("Qoldiq yo'q")
# print(s)

# Kabisa yili If..else
# n = int(input("n: "))
#
# if n % 4 == 0:
#     if n % 100 == 0:
#         if n % 400 == 0:
#             print("Kabisa yili.")
#         else:
#             print("Oddiy yil.")
#     else:
#         print("kabisa yili")
#
# else:
#     print("Oddiy yil.")



def make_point(x, y):

	def points():
		print(f"Points({x}, {y}")

	def get_x():
		return x

	def geet_y():
		return y

	def set_x(value):
		x = value
		return value

	def set_y(value):
		y = value
		return y

	return points

make_point(12,13)
