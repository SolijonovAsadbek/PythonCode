import pickle
import dill


class Dog:
    species = 'Canis Familiars'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


obj = Dog('Bethoven', 3)
with open('my_dog.pkl', 'wb') as file:
    dill.dump_session(file)
