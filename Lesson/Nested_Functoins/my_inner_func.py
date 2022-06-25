# Ichma - ich funksiyaga misol

# from time import sleep
#
#
# def outer_func():
#     def inner_func():
#         def say():
#             print("Hello world")
#
#         print('Inner function ichi.')
#         sleep(5)
#         say()
#
#     print('Outer function ichi.')
#     sleep(10)
#     inner_func()
#
#
# outer_func()


# clousure function

# def out(arg):
#     def inner():
#         return f'this is {arg}'
#     return inner()
# value = int(input('value: '))
# x = out(value)
# print(x)


# Inner function orqali focus ni bir yerga qaratish
# def more_str(text:str, num:int, /):
#     if not isinstance(text, str):
#         raise TypeError(f'text:str is not {type(text)}')
#
#     if not isinstance(num, int):
#         raise TypeError(f'num:int is not {type(num)}')
#
#     def base():
#         return text * num
#
#     return base()
#
# x = more_str('H ', 12)
# print(x)

# Inner function dan ma'lumotlar bazasi sifatida foydalanish
# def out(arg1):
#     def inner(arg2):
#         def calc():
#             return arg1 * arg2
#         return calc()
#
#     return inner
#
# inn = out(12)(10)

# cal = inn(21)
# print(cal)


# Cheksiz rekursiya hosil qilish
# def loop():
#     print("loop")
#     return print('looop2'), loop()
#
#
# loop()


# # Rekursion funksiya
# def factorial(x):
#     if x < 2:
#         return 1
#     return x * factorial(x - 1)
#
#
# result = factorial(5)
# print(result)


# Ichma - ich funksiyaning ishlash ketma-ketligi
# def outer_func():
#     print("outer_func() - 1")
#
#     def inner_func():
#         print('inner_func() - 2')
#         print('inner_func() - 3')
#
#     print('outer_func() - 4')
#     inner_func()
#     print('outer_func() - 5')
#
#
# outer_func()


# def outer_func(arg):
#     # Closure Function
#     def inner_func():
#         return arg * 10
#
#     return inner_func()
#
#
# x = outer_func(12)
# print(x)


# Mukammal faktorial funktsiyasi hosil qilish.
# def factorial(arg):
#     if not isinstance(arg, int):
#         raise TypeError(f"Factorial funksiya faqat <class 'int'> qabul qiladi. {type(arg)} emas.")
#
#     def inner_fac(x):
#         if x < 2:
#             return 1
#         return x * factorial(x - 1)
#
#     return inner_fac(arg)
#
#
# res = factorial(3)
# print(res)
