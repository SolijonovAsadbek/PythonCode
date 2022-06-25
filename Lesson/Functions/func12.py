# func16
# def sort3(arg1, arg2, arg3):
#     if isinstance(arg1, str) or isinstance(arg2, str) or isinstance(arg3, str):
#         raise TypeError("Son kiriting iltmos!")
#
#     def inner_sort3():
#         nonlocal arg3, arg2, arg1
#         if arg1 < arg2 < arg3 or arg2 < arg1 < arg3:
#             if arg2 < arg1:
#                 arg1, arg2, arg3 = arg2, arg1, arg3
#
#         elif arg1 < arg3 < arg2 or arg3 < arg1 < arg2:
#             if arg1 < arg3:
#                 arg1, arg2, arg3 = arg1, arg3, arg2
#             else:
#                 arg1, arg2, arg3 = arg3, arg1, arg2
#
#         elif arg2 < arg3 < arg1 or arg3 < arg2 < arg1:
#             if arg2 < arg3:
#                 arg1, arg2, arg3 = arg2, arg3, arg1
#             else:
#                 arg1, arg2, arg3 = arg3, arg2, arg1
#
#         return arg1, arg2, arg3
#
#     return inner_sort3()
#
#
# natija = sort3(3, 2, False)
# print(natija)


# func16
# def ishora(arg):
#     if isinstance(arg, str):
#         raise TypeError("Ilimos son kiriting.")
#
#     def inner_shora():
#         if arg > 0:
#             return 1
#         elif arg == 0:
#             return 0
#         else:
#             return -1
#
#     return inner_shora()
#
#
# natija = ishora(0) + ishora(-10)
# print(natija)


# # func46
# def ekub(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise TypeError("Iltimos butun son kiriting.")
#
#     def inner_ekub(a, b):
#         while a != b:
#             if a < b:
#                 b -= a
#             else:
#                 a -= b
#         return a
#
#     return inner_ekub(a, b)
#
#
# # natija = ekub(8, 10)
# # print(natija)
#
# # func46
# def ekuk(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         raise TypeError("Iltimos butun son kiriting.")
#
#     def inner_ekuk():
#         global ekub
#         natija = ekub(a, b)
#         ab = a * b
#         return ab / natija
#
#     def great():
#         return 'Salom'
#
#     inner_ekuk.great = great
#
#     return inner_ekuk
#
#
# natija2 = ekuk(5, 10)
# print(natija2.great())
# # print(natija2())
# # print(natija2.k())


# def make_point(x, y):
#     def points():
#         print(f"Point({x}, {y})")
#
#     def get_x():
#         return x
#
#     def get_y():
#         return y
#
#     def set_x(value):
#         nonlocal x
#         x = value
#
#     def set_y(value):
#         nonlocal y
#         y = value
#
#     # Attach getters and setters
#     points.get_x = get_x
#     points.set_x = set_x
#     points.get_y = get_y
#     points.set_y = set_y
#     return points
#
#
# p = make_point(1, 2)
# print(p.get_x())  # 1
# print(p.get_y())  # 2
# p()  # Point(1, 2)
# p.set_x(42)
# p.set_y(7)
# p()  # Point(42, 7)

# a = int(input("a: "))
# b = int(input("b: "))
#
#
# def ekuk(func):
#     def inner_ekuk(*args):
#         ekub = func(*args)
#         ab = a * b
#         e = ab / ekub
#         return e
#
#     return inner_ekuk
#
#
# import logging
#
#
# @ekuk
# def ekub(a, b):
#     while a != b:
#         logging.info(a)
#         if a < b:
#             b -= a
#         else:
#             a -= b
#     return a
#
#
# print(ekub(a, b))
