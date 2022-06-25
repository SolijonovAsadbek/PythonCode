class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        return f"{self.fname} {self.lname} {self.age} years old."


class Adress:
    def __init__(self, country, region, district, neighborhood, street, home):
        self.country = country
        self.region = region
        self.district = district
        self.neighborhood = neighborhood
        self.street = street
        self.home = home

    def __str__(self):
        return f"Adress:\n" \
               f"Country: {self.country}\n" \
               f"Region: {self.region}\n" \
               f"District: {self.district}\n" \
               f"Neighborhood: {self.neighborhood}\n" \
               f"Street: {self.street}\n" \
               f"Home: {self.home}"


class Student:
    def __init__(self, person, adress, course):
        self.person = person
        self.adress = adress
        self.course = course

    def __str__(self):
        return f"Person:\n" \
               f"{self.person}\n" \
               f"{self.adress}\n" \
               f"Course: {self.course}"


person1 = Person("Abduqodir", "Yusufjonov", 17)

adress1 = Adress("O'zbekistan", "Namangan", "Davlatobod", "Irvadon", "Abdulla Qoxhor", 13)

student1 = Student(person1, adress1, 2)

print(student1.adress.home)
