# *args ni moslashuvchan funksiyada tutgan o'rni.
# Moslashuvchan funkstsiya. ----- *args
# def my_arguments(*args):
#     print(args, type(args), len(args))
#
#
# my_arguments()
# my_arguments(12, 3, 2.5, True, False, 2+3j, 'foo')


# **kwargs lug'at hosil qilishda ishlatiladi, lug'atda doim kalit va qiymat bo'lgani uchun, funksiyaga
# kalit=qiymat ko'rinishida yozishimiz shart.
# def my_keyargs(**kwargs):
#     print(f"kwargs: {kwargs}", f"type: {type(kwargs)}", f"length: {len(kwargs)}", sep='\n')
#
#
# my_keyargs(name='Foo', age=12, family=True, phone='911752563')


# *args, **kwargs  -  bularni bitta funskiyada qanday ishlatish kerakligi.
# def arg_kwarg(*args, **kwargs):
#     print(f"args: {args}\nkwargs: {kwargs}")
#
#
# arg_kwarg(1, 2, 3, 4, True, False, 2+3j, 2.32, (1, 0.3, 'Asilbek'), name='foo', age=12, family=False, phone=911552523)

# pozitsion, *args, **kwargs larni qanday tartibda uzatilishi ko'rsatilgan.
# def arg_kwarg(a, b, *args, **kwargs):
#     print(f"a: {a}\nb: {b}\nargs: {args}\nkwargs: {kwargs}")
#
#
# arg_kwarg(1, 2, 3, 4, True, False, 2+3j, 2.32, (1, 0.3, 'Asilbek'), name='foo', age=12, family=False, phone=911552523)
import math

# def avg(a, b, /, c, *, key='+'):
#     if key == '+':
#         return a + b + c
#     elif key == '-':
#         return a - b - c
#     elif key == '*':
#         return a * b * c
#     elif key == '/':
#         return a / b / c
#     else:
#         return f'{key} - bunday belgi mavjud emas.'
#
#
# # print(avg(1, 2, 3, key='/'))
# print(avg(1, 2, c=3, key='/'))

a = int(input('a son: '))


def tub_sonlar(a):
    b = 0
    c = 0
    tub = []
    for i in range(2, a):
        for j in range(1, i + 1):
            if i % j == 0:
                b += 1
        # print(f'a:{i}, b: {b}')
        if b == 2:
            tub.append(i)
            c += 1
        b = 0
    return c, tuple(tub)


x = tub_sonlar(a)
print(f'Barcha tub sonlar: {x[0]}\nTub sonlar ro`yxati: {x[1]}')
