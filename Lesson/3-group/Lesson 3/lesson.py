# a = True
# b = False
#
# c = a & b
# c1 = a | b
# print(f"{a} and {b} = {c}")
# print(f"{a} or {b} = {c1}")
# print(f"not {a} = {not a}, not {b} = {not b}")

# a = 1
# print(1 <= a <= 13)


# Boolean 36
x1 = int(input("x1: "))
y1 = int(input("y1: "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))

b = x1 == x2 and y1 != y2
d = y1 == y2 and x1 != x2
c = b or d
print(c)

