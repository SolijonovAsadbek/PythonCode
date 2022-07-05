# # a = float(input("a: "))
#
#
# def increment(number):
#     try:
#         if not (isinstance(number, float) or isinstance(number, int)):
#             raise TypeError("Faqat sonlarni kiriting.")
#
#         # closure function
#         def inner_increment():
#             return number + 1
#
#         return inner_increment()
#     except Exception as e:
#         print(f"Xatolik: {e}")
#
#
# b = increment(1.0)
# print(f"increment: {b}")

# Simple Function
# Decorator - bu Funksiya ichida funksiya qabul qilivchi funksiyaga aytiladi.
# Decorator
# def decor(func):
#     def beauty(*args):
#         print(f'{args} yig`indisi: {func(*args)}')
#
#     return beauty
#
#
# @decor
# def summa(*args):
#     add = 0
#     for item in args:
#         add += item
#     return add
#
#
# summa(1, 2, 3)
# lambda funksiya
# square = lambda x: (x ** 2, 'hello');  # Nomsiz funksiya.
#
# print(square(4))


# standard funksiya
# def another_square(x):  # Nomlangan funksiya.
#     return x ** 2


# natija = (lambda x: x ** 3)(4)
# print(natija)

# def second(x):
#     return x[1]
#
#
# a = [(2, 123), (34, 90), (112, 1223), (1, 2)]
# # a.sort(key=second)
# a.sort(key=lambda x: x[1])
# print(a)

natija = (lambda x: (x % 2 and 'Toq' or 'Juft'))(1)
print(natija)
