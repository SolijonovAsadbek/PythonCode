# Shablon
class Dog:
    # consturtor
    def __init__(self, name, color, weight, height, age):
        self.name = name
        self.color = color
        self.weight = weight
        self.height = height
        self.age = age


object1 = Dog(name='Bethoven', color='Brown', weight=30, height=130, age=1.5)
object2 = Dog(name='Kris', color='White', weight=6, height=50, age=None)
object3 = Dog(name='Jack', color='Black', weight=8, height=70, age=3)
object4 = Dog(name='Alex', color='Grey', weight=16, height=90, age=3.5)
object5 = Dog(name='Devid', color='Black', weight=26, height=150, age=8)

# Bu usul yaxshi usul emas
# print(f'{object1.name} is {object1.age} years old.')
# print(f'{object2.name} is {object2.age} years old.')
# print(f'{object3.name} is {object3.age} years old.')
# print(f'{object4.name} is {object4.age} years old.')
# print(f'{object5.name} is {object5.age} years old.')

print('*' * 20)
# Bu usulni qollash tavsiya etiladi
objects = [object1, object2, object3, object4, object5]
for obj in objects:
    print(f'{obj.name} is {obj.age} years old.')



