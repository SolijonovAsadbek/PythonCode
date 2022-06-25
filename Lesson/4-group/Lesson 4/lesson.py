# a = int(input("a: "))
# if a >= 2:
#     print("Ikkidan katta son.")
# elif a == 2 or a > 2:
#     print("Ikkiga teng son.")
# else:
#     print("Ikkidan kichik.")


# name = input("Ismingini kiriting: ")
# lname = input("Familyangizni kiriting: ")
# age = int(input("Yoshingizni nechida? :"))
#
# if age >= 12:
#     print(f"Hush kelibsiz {lname + ' ' + name} Python dasturlash kursiga.")
# elif age >= 12:
#     print(f"Hush kelibsiz {lname + ' ' + name} Matem va Ingliz tili kursiga.")
# elif 10 <= age < 12:
#     print("Ok")
# else:
#     print("Siz yoshingiz  IT kursiga mos kelmaysiz.")
#
# if age >= 12:
#     print(f"Hush kelibsiz {lname + ' ' + name} Matem va Ingliz tili kursiga.")


class Base:
    def __init__(self):
        self.a = "Python Language"
        self.__c = "Django Framework"

    def get_c(self):
        return self.__c

    def set_c(self, value):
        self.__c = value


# # Hosila sinf yaratish
class Derived(Base):
    def __init__(self):
        # Asosiy sinfning konstruktorini chaqirish
        Base.__init__(self)
        print("Asosiy sinfning shaxsiy a'zosiga chaqirish: ")
        print(self.__c)


# Driver code
obj1 = Base()
print(obj1.a)
print(obj1.get_c())
obj1.set_c("Flask Framework")
print(obj1.get_c())

# obj2 = Derived()
# print(obj2.__c)
