# massiv = [1, -20, -290, 290, 30, 40, 20]
# k = int(input("k: "))
# l = int(input("l: "))
# sum_ = 0
# for i in range(k, l + 1):
#     sum_ += massiv[i]
#
# print(f"O'rta arif: {sum_ / (l - k + 1)}")

# array 21
# def avg_k_l(*args, start=None, end=None):
#     sum_ = 0
#     for i in range(start, end + 1):
#         sum_ += args[i]
#     return sum_ / (end - start + 1)
#
#
# a = avg_k_l(1, 2, 3, 4, 5, 6, 7, 8, 9, start=2, end=5)
# print(a)


# array 24

# def arif_prog(*args, ayirma=None):
#     if not ayirma:
#         ayirma = args[2] - args[1]
#
#     count = 0
#     for i in range(2, len(args) - 1):
#         if ayirma != args[i + 1] - args[i]:
#             count += 1
#     if count == 0:
#         return ayirma
#     else:
#         return 0
#
#
# ar = arif_prog(1, 3, 5, 7, 9, ayirma=3)
# print(ar)
