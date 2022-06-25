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
def decor(func):
    def beauty(*args):
        print(f'{args} yig`indisi: {func(*args)}')

    return beauty


@decor
def summa(*args):
    add = 0
    for item in args:
        add += item
    return add


summa(1, 2, 3)
