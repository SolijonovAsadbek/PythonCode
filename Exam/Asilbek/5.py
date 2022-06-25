# 4
n = int(input("n="))
m = int(input("m="))
a = 1
b = 1
for i in range(1, n + 1):
    a *= i
for g in range(1, m + 1):
    b *= g
print(a / b)
