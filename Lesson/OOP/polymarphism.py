# Polymarphism

class Dog:
    species = 'Species is None'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self, sound='Woof .... Woof'):
        return f'{self.name} bark {sound}.'


class Bulldog(Dog):
    species = 'I don`t know species of the Bulldog'

    def speak(self, sound='Wuuf ... Wuuf'):
        return super().speak(sound)


class JackRussellTerrier(Dog):
    species = 'I don`t know species of the JackRussellTerrier'

    def speak(self, sound='Waaf ... Waaf'):
        return super().speak(sound)


class Dachshund(Dog):
    species = 'I don`t know species of the Dachshund'

    def speak(self, sound='Yaap ... Yaap'):
        return f'{self.name} says {sound}.'


bethoven = Bulldog('Bethoven', 10)
b_speak = bethoven.speak()
print(b_speak)

charli = JackRussellTerrier('Charli', 9)
ch_speak = charli.speak()
print(ch_speak)

jack = Dachshund('Jack', 4)
j_speak = jack.speak()
print(j_speak)
