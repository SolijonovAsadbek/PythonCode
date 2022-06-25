# 3 - misol
def uge(*args):
    mult = 1
    for arg in args:
        mult *= arg
    return mult ** (1 / len(args))


a = uge(3, 3, 3)
print(a)
