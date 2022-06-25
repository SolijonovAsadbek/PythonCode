# Butun sonlar 30-misol
# a = int(input("Yilni kiriting: "))
# butun = a // 100
# start = butun * 100 + 1
# end = start + 99
#
# if start <= a and end >= a:
#     print(f"{butun + 1} - asr.")
# else:
#     print(f"{butun} - asr.")


# Mantiqiy 20-misol
# a = int(input("Uch xonlai son kiriting: "))
# start = a // 100
# mid = (a // 10) % 10
# end = a % 10
# condition = start != mid and start != end and mid != end
# print(condition)

# if condition:
#     print(f"{a}-har hil raqamlardan tashkil topgan.")
# else:
#     print("Error!")

# Mantiqiy 29-misol

# x = float(input("x: "))
# y = float(input("y: "))
# x1 = float(input("x1: "))
# y1 = float(input("y1: "))
# x2 = float(input("x2: "))
# y2 = float(input("y2: "))
#
# a = (x > x1 and x < x2) and (y1 > y and y > y2)
#
# print(a)

a = input("Satr1: ")
# x = input("Satr2:")
start = a[0]
end = a[-1]
mid = a[1: -1]
print(start+mid[::-1]+end)