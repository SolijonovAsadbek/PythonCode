# Person shablon
class Person:
    # name() funksiyasi
    def name(self):
        return 'Valijon'

    def surname(self):
        return 'Obidov'

    def age(self):
        return f'Yoshi 12 da'

    def manzil(self):
        return "Manzil: Namangan viloyati, Chortoq tumani, Bodomzor ko'chasi, 17-uy"

    # telefon() funksiyasi
    def telefon(self):
        return '+998 99 017 28 73'


# Person shablonidan obyekt yaratamiz.
obj = Person()
print('Person ismi: ', obj.name())
print('Person yoshi: ', obj.age())
print('Person manzili: ', obj.manzil())
print('Person familyasi: ', obj.surname())
print('Person telefoni: ', obj.telefon())

