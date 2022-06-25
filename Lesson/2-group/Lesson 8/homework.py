# while 22
# son = int(input("Son: "))
# count = 0
# k = 2
# if son > 1:
#     while k < son:
#         if son % k == 0:
#             count += 1
#         k += 1
#
#     if count > 0:
#         print(f"{son} Tub son emas!")
#     else:
#         print(f"{son} tub son")


# while 23
# a = int(input("a= "))
# b = int(input("b= "))
# while a > 0:
#     if a > b:
#         a %= b
#         print(a)
#     else:
#         b %= a
#         print(b)
# print("EKUB=", a + b)


# while 24
# n = int(input("Son: "))
# start = 0
# end = 1
# num = 0
# s = ""
# while num <= n:
#     num = start + end
#     start = end
#     end = num
#     if num == n:
#         s += f"{n} fibonachi son"
#         break
# if s == "":
#     print(f"{n} fibonachi emas.")
# else:
#     print(s)

# while 28 Flag method
# e = float(input("e: "))
# a1 = 2
# a2 = 2 + 1 / a1
# k = 2
# boo_ = True
# while boo_:
#     if abs(a2 - a1) < e:
#         print(f"a{k - 1}: {a1}")
#         print(f"a{k}: {a2}")
#         boo_ = False
#     a1 = a2
#     a2 = 2 + 1 / a1
#     k += 1


# MinMax1
N = int(input("N: "))
numbers = list()
for i in range(N):
    a = float(input(f"son{i + 1}: "))
    numbers.append(a)
print(numbers)

max_ = numbers[0]
for i in range(N):
    if max_ <= numbers[i]:
        max_ = numbers[i]

print("maxsimal son: ", max_)
