# match case 14
# a = int(input("uch burchak tomoni:"))
# b = int(input("buyruq:"))
# match b:
#     case 1:
#         print("uch burchak tomoni:", a)
#     case 2:
#         print("ichki aylana radiusi:", a * 3 ** (1 / 2) / 6)
#     case 3:
#         print("tashqi aylana radiusi:", 2 * a * 3 ** (1 / 2) / 6)
#     case 4:
#         print("uch burchak yuzi", a ** 2 * 3 ** (1 / 2) / 6)
#     case _:
#         print("xato")


# match 18
# n = int(input("n: "))
# start = n // 100
# mid = (n // 10) % 10
# end = n % 10

# match start:
#     case 1:
#         print('bir yuz', end=" ")
#     case 2:
#         print('ikki yuz', end=" ")
#     case 3:
#         print('uch yuz', end=" ")
#     case 4:
#         print('to\'rt yuz', end=" ")
#     case 5:
#         print('besh yuz', end=" ")
#     case 6:
#         print('olti yuz', end=" ")
#     case 7:
#         print('yetti yuz', end=" ")
#     case 8:
#         print('sakkiz yuz', end=" ")
#     case 9:
#         print('to\'qqiz yuz', end=" ")

# match mid:
#     case 1:
#         print('o\'n', end=" ")
#     case 2:
#         print('yigirma', end=" ")
#     case 3:
#         print('o\'ttiz', end=" ")
#     case 4:
#         print('qiriq', end=" ")
#     case 5:
#         print('ellik', end=" ")
#     case 6:
#         print('oltmush', end=" ")
#     case 7:
#         print('yetmush', end=" ")
#     case 8:
#         print('sakson', end=" ")
#     case 9:
#         print('to\'qson', end=" ")
#     case _:
#         pass

# match end:
#     case 1:
#         print('bir')
#     case 2:
#         print('ikki ')
#     case 3:
#         print('uch ')
#     case 4:
#         print('to\'rt ')
#     case 5:
#         print('besh ')
#     case 6:
#         print('olti')
#     case 7:
#         print('yetti')
#     case 8:
#         print('sakkiz')
#     case 9:
#         print('to\'qqiz')
#     case _:
#         pass


def make_point(x, y):
    def points():
        print("____1____")
        print(f"Point({x}, {y})")

    def get_x():
        print("____2____")
        return x

    def get_y():
        print("____3____")
        return y

    def set_x(value):
        print("____4____")
        nonlocal x
        x = value

    def set_y(value):
        print("____5____")
        nonlocal y
        y = value

    # Attach getters and setters
    points.get_x = get_x
    points.set_x = set_x
    points.get_y = get_y
    points.set_y = set_y
    return points


p = make_point(1, 2)

print(p.get_x())
print(p.get_y())

p()

# p.set_x(42)
# p.set_y(7)

# p()      


x = 5


def f(x):
    def in_f():
        x = 10
        return x

    return in_f()


x = f(x)
print(x)










