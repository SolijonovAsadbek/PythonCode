# bool 1
# a = float(input("a: "))
# natija = a > 0
# print(natija)


# bool 5
# a = float(input("a: "))
# b = float(input("b: "))
#
# natija = a >= 0 or b < -2
# print(natija)


# bool 15
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

natija1 = a > 0 > b > c or a > 0 > c > b
natija2 = b > 0 > c > a or b > 0 > a > c
natija3 = c > 0 > a > b or c > 0 > b > a

total = natija1 or natija2 or natija3
print(total)
