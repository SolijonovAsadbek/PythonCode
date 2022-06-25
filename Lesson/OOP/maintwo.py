# # Python program to illustrate destructor
# class Employee:
#
#     # Initializing
#     def __init__(self):
#         print('Employee created.')
#
#     # Deleting (Calling destructor)
#     def __del__(self):
#         print('Destructor called, Employee deleted.')
#
#     def ok(self):
#         print('ok')
#
#
# obj = Employee()


class Add:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x + self.y}'


class Multiple:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x * self.y}'


class Number(Add, Multiple):
    def __init__(self, x, y):
        super().__init__(x, y)

    def add(self):
        return Add(self.x, self.y)

    def mult(self):
        return Multiple(self.x, self.y)


# num = Number(12, 10)
# print(num.add())
# print(num.mult())


class Numbers:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def add(self):
        return self.x + self.y

    @property
    def mult(self):
        return self.x * self.y


num = Numbers(12, 10)
print(num.add)
print(num.mult)
