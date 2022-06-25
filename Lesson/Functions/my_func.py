# print funksiyani aniqlayapman.
# def oddiy_funksiya():
#     a = "Men oddiy funktsiyaman."
#     print(a)
#
#
# oddiy_funksiya()


# return funksiyani aniqlayapman.
# def return_funksiya():
#     a = "Men oddiy funktsiyaman."
#     return a
#
#
# x = return_funksiya()
# print(x)


# Ixtiyoriy sonni darajaga oshiruvchi funksiya.
# def pow_num(number, degree):
#     return number ** degree
#
#
# x = pow_num(number=10, degree=0)
# print(x)

# operatorni kalit qiymat sifatida qabul qilib hissoblovchi funktsiya
# def yigindi(*args, op='+'):
#     summa = 0
#     if op == '+':
#         for arg in args:
#             summa += arg
#         return summa
#     elif op == '-':
#         summa = args[0] * 2
#         for arg in args:
#             summa -= arg
#         return summa
#     elif op == '*':
#         summa = 1
#         for arg in args:
#             summa *= arg
#         return summa
#     elif op == '/':
#         summa = args[0] ** 2
#         for arg in args:
#             summa /= arg
#         return summa
#     else:
#         raise TypeError("[ +, -, /, * ] - Operatorlardan birini kirting.")
#
#
# x = yigindi(1, 2, 4, op='0')
# print(x)
