# import datetime
#
# nw = datetime.datetime.now()
# print("Hozirgi vaqt: ", nw)
# print("Sana: ", nw.date())
# print('Vaqt: ', nw.time())
# print('Hozirgi vaqt: ', nw.today())
# print('soat:munit: ', nw.hour, nw.minute, sep=':')
# print('second: microsecond: ', nw.second, nw.microsecond, sep=':')
# print('Astimezone: ', nw.astimezone())
# print('IsoCalendar: ', nw.isocalendar())
# print('Cool time: ', nw.ctime())
# # print(nw.dst())
# print(nw.weekday())
# print('Dunyo stantart vaqti: ', nw.utcnow())
# print(nw.strftime('%c'))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{__class__.__name__}({self.name}, {self.age})"

    @property
    def desc(self):
        return f"{self.name} is {self.age} years old."


obj = Student('Asilbek', 23)
print(obj)
print(obj.name)
print(obj.desc)
