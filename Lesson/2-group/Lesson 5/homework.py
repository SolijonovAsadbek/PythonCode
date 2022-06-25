# 1-misol
# k = int(input("K: "))
# n = int(input("N: "))
#
# for i in range(n):
#     print(k, i)


# 6-misol
# a = float(input("1 kg konfet narxi: "))
# for i in range(1, 2):
#     for j in range(1, 10):
#         kg = i + j/10
#         print(f"{kg}-kg konfetning narxi: {round(kg*a, 1)}")
#     print(f"{1+i}-kg konfetning narxi: {round((i+1)*a, 1)}")
# *****************************
# for i in range(2, 11, 2):
#     kg = 1+i/10
#     print(f"{kg} - kg konfetning narxi: {kg*a} so'm")

# 11-misol
# n = int(input("N: "))
# sum = 0
# for i in range(n, 2*n+1):
#     sum += i**2
#     print(i**2, end=" ")
# print(f"->{sum}")

# 12-misol
# n = int(input("n: "))
# multiple = 1
# for i in range(1, n):
#     multiple *= i
#     for j in range(1, 10):
#         c = (i + j / 10)
#         multiple *= c
#     multiple *= (i + 1)
# print(multiple)


# 20-misol
# n = int(input("n: "))
# k = 1
# s = 0
# for i in range(1, n + 1):
#     k = k * i
#     s = s + k
# print(s)
