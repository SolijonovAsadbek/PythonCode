class Employee:
    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def full_name(self):
        return f"{self.fname} {self.lname}"

    @property
    def unpack(self):
        return self.fname, self.lname, self.pay

    def __str__(self):
        return f"{self.__class__.__name__}({self.fname}, {self.lname}, {self.pay})"


# x = Employee('A', 'B', 10000)
# print(x)
# print(x.fname)
# print(x.pay)
# print(x.unpack)
# print(x.full_name)
