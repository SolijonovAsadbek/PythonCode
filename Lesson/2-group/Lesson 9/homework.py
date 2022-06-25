# MinMax15
# b = float(input("b: "))
# c = float(input("c: "))
# if b > c:
#     b, c = c, b
# n = int(input("List uzunligi: "))
# numbers = []
# for i in range(n):
#     a = float(input(f"a{i}: "))
#     numbers.append(a)
# max_ = numbers[0]
#
# for number in numbers:
#     if b <= number <= c:
#         if max_ <= number:
#             max_ = number
#
# if b <= max_ <= c:
#     print("Max: ", max_)
# else:
#     print(0, 0)


# MinMax 20
# numbers = [-12, 210, 1, 0]
# if len(numbers) > 1:
#     extre_max = numbers[0]
#     extre_min = numbers[0]
#     for number in numbers:
#         if extre_max <= number:
#             extre_max = number
#         if extre_min >= number:
#             extre_min = number
#     print(f"Ekstrimal qiymatlar {extre_min}, {extre_max} .")
# elif len(numbers) == 1:
#     print(f"Ekstrimal qiymat {numbers[0]} .")
# else:
#     print("Ekstrimal qiymatlar mavjud emas.")
