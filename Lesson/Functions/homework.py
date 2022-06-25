# Function 1
# def power_3(arg):
#     """ def power_3(arg):
#     Ixtiyoriy sonning 3-darajasini hissoblovchi funktsiya.
#     arg - ixtiyoriy son"""
#     multiple = 1
#     for i in range(3):
#         multiple *= arg
#
#     return multiple
#
#
# a = power_3(3)
# print(a)
# print(power_3.__doc__)


# Function 2
# def power(arg: float, deg: int):
#     """def power(arg: float, deg: int):
#     Ixtiyoriy sonning butun darajasini hissoblovchi funksiya"""
#     multiple = 1
#     if deg >= 0 and arg != 0:
#         for i in range(deg):
#             multiple *= arg
#         return multiple
#     elif arg == 0 and deg == 0:
#         return "Xissoblash mumkin emas."
#     else:
#         for i in range(abs(deg)):
#             multiple *= arg
#         return 1 / multiple
#
#
# a = power(2, -1)
# print(a)


"""Kostya yaqinda ilmiy-fantastik kitobni o'qidi. Unda eng dahshatli voqealar faqat
bir yilda uchta bir xil raqam bo'lganda sodir bo'lgan.Kostya ma'lum bir davrda qaysi
yillar "maxsus" bo'lganligi yoki bo'lishi bilan qiziqdi.

Foydalanuvchidan ikkita to'rt xonali A va B raqamlarini so'raydigan dastur yozing.
Keyin A dan B gacha bo'lgan oraliqdagi to'liq uchta bir xil raqamni o'z ichiga olgan
barcha to'rt xonali raqamlarni o'sish tartibida chiqaring.

Dasturning ishlashiga misol:
Birinchi yilni kiriting: 1900
Ikkinchi yilni kiriting: 2100
1900 yildan 2100 yilgacha bo'lgan yillar, uchta bir xil raqam bilan:

yil: 1911
yil: 1999

1911
1999
2000
2022

1900 yildan 2100 yilgacha bo'lgan yillar, uchta bir xil raqam bilan:"""


# 1-usul
# a = int(input("yil boshi: "))
# b = int(input("yil oxiri: "))
#
# for year in range(a, b):
#     years = str(year)
#     count = 0
#     for i in range(len(years)):
#         for j in range(4):
#             if (i != j) and (years[i] == years[j]):
#                 count += 1
#                 if count == 6:
#                     print(year)

# 2-usul
# a = int(input("yil boshi: "))
# b = int(input("yil oxiri: "))
# for year in range(a, b):
#     x_1 = year // 1000
#     x_2 = (year // 100) % 10
#     x_3 = (year // 10) % 10
#     x_4 = year % 10
#
#     m_1 = x_1 != x_2 and x_2 == x_3 == x_4
#     m_2 = x_1 != x_2 and x_1 == x_3 == x_4
#     m_3 = x_2 != x_3 and x_1 == x_2 == x_4
#     m_4 = x_3 != x_4 and x_1 == x_2 == x_3
#
#     bool_ = m_1 or m_2 or m_3 or m_4
#     if bool_:
#         print(year)


# # MinMax 27
# set_ = [5, 20, 3, 4]
# set_new = []
# min_ = set_[0] * set_[1]
# for i in range(len(set_)-1):
#     set_new.append(set_[i]*set_[i+1])
#     if min_ >= set_[i] * set_[i+1]:
#         min_ = set_[i] * set_[i+1]
#
# print("Jami ko'paytmalar: ", set_new)
# print("Minimal ko'paytmasi: ", min_)
#
#
# index = 0
# for j in range(len(set_new)):
#     if min_ == set_new[j]:
#         index = j
#
#
# print("Berilgan asil to'plam: ", set_)
# print(f"Elemetlar: {set_[index]} * {set_[index+1]} = {min_} -> {index}-{index+1} indeks.")


# def f(my_list=None):
#     if my_list is None:
#         my_list = list()
#     print(my_list)
#     my_list.append('*')
#     return my_list
#
#
# print(f())
# print('-' * 20)
# print(f())
# print('-' * 20)

