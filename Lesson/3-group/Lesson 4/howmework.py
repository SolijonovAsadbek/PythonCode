# Boolean 19
# a = int(input("son:"))
# b = int(input("son:"))
# c = int(input("son:"))
# n1 = a == b * -1 or a == c * -1
# n2 = a == c * -1 or a == b * -1
# n3 = c == b * -1 or c == a * -1
#
# r = n1 or n2 or n3
# print(r)

# Boolean 22
# n = int(input("n: "))
# start = n // 100
# mid = (n // 10) % 10
# end = n % 10
# c1 = start <= mid <= end
# c2 = start >= mid >= end
# r = c1 or c2
# print(r)


# Boolean 23
# n = int(input("Palindrom:"))
# str_ = str(n)
# rts_ = str_[::-1]
# r = int(str_) == int(rts_)
# print(r)


# Boolean 29
# x = float(input("x: "))
# y = float(input("y: "))
#
# x1 = float(input("x1: "))
# y1 = float(input("y1: "))
#
# x2 = float(input("x2: "))
# y2 = float(input("y2: "))
#
# c1 = x1 < x < x2
# c2 = y2 < y < y1
#
# r = c1 and c2
# print(r)

# Boolean 32
# import math
#
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
#
# c1 = math.sqrt(a ** 2 + b ** 2) == c
# c2 = math.sqrt(c ** 2 + b ** 2) == a
# c3 = math.sqrt(a ** 2 + c ** 2) == b
#
# r = c1 or c2 or c3
# print(r)


# Boolean 33
# a = float(input("a: "))
# b = float(input("b: "))
# c = float(input("c: "))
#
# c1 = a + b > c > 0
# c2 = c + b > a > 0
# c3 = c + a > b > 0
#
# r = c1 and c2 and c3
# print(r)


# Boolean 34
# x = int(input("x: "))
# y = int(input("y: "))
# print(f"(1,1) = Oq -True\n(1,2) = Qora-False")
# c1 = x % 2 != 0 and y % 2 != 0
# c2 = x == y
# r = c1 or c2
# print(r)
