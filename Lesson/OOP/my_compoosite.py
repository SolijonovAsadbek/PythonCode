# Kompozit klass
class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.address = Address    # Address klasi ulandi
        self.passport = Passport  # Passport klasi ulandi

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Birthday: {self.birthday}\n' \
               f'Passport: {self.passport}\n' \
               f'Address: {self.address}'


# Komponent klass
class Passport:
    def __init__(self, seria, number, JSHSHIR):
        self.seria = seria
        self.number = number
        self.jshshir = JSHSHIR

    def all(self):
        return f'Seria number: {self.seria} {self.number}\nJSHSHIR: {self.jshshir}'


# Koponent klass
class Address:
    def __init__(self, citiy, street, home, district=None, village=None):
        self.citiy = citiy
        self.district = district
        self.village = village
        self.street = street
        self.home = home

    def all(self):
        return f'Citiy: {self.citiy}, ' \
               f'{f"District: {self.district}, " if self.district else ""}{f"Village: {self.village}, " if self.village else ""}' \
               f'Street: {self.street} , ' \
               f'Home: {self.home}'


asilbek = Person('Asilbek', '12.12.12')
asilbek_adress = asilbek.address('Namangan', 'Boburshox', 61, district='Chortoq', village='O`rikzor')
asilbek_passport = asilbek.passport('AA', 12345678, 12121212345678)
asilbek.address = asilbek_adress.all()
asilbek.passport = asilbek_passport.all()

print(asilbek)
