from math import sqrt

# Kvadrat tenglama
class KVT:
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        D = self.b ** 2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b + sqrt(D)) / (2 * self.a)
            x2 = (-self.b - sqrt(D)) / (2 * self.a)
            return f'x1: {x1}\nx2: {x2}'
        elif D == 0:
            x1 = (-self.b + sqrt(D)) / (2 * self.a)
            return f'x: {x1}'
        else:
            return 'Bo`sh to`plam.'


one = KVT(a=1, b=3, c=2)
print(one)
