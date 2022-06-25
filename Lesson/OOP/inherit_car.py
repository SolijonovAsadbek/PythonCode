class Avtomobil:

    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def __str__(self):
        return f'{self.name} {self.color} {self.color} rangda.'


class Tesla(Avtomobil):
    count = 0
    oq = 0
    qora = 0
    model_s = 0
    model_3 = 0
    model_x = 0
    model_y = 0

    def __init__(self, name, model, color):
        super().__init__(name, model, color)
        Tesla.count = 0

        # Necha qana rangga zakas berilganini hissoblovchi dastur
        if self.color.lower() in ['oq', 'white']:
            Tesla.oq += 1
        elif self.color.lower() in ['qora', 'black']:
            Tesla.qora += 1

        # Nechta modelga buyurta berilganini hissoblovchi dastur
        if self.model.lower() in ['model s']:
            Tesla.model_s += 1
        elif self.model.lower() in ['model 3']:
            Tesla.model_3 += 1
        elif self.model.lower() in ['model x']:
            Tesla.model_x += 1
        elif self.model.lower() in ['model y']:
            Tesla.model_y += 1


class BMW(Avtomobil):
    count = 0
    colors = []
    models = []

    def __init__(self, name, model, color):
        super().__init__(name, model, color)
        BMW.count += 1
        BMW.colors.append(color.lower())
        BMW.models.append(model.lower())

    def cocolor(self, color):
        amount = BMW.colors.count(color)
        if amount:
            return f'{color} bmw: {amount} ta'
        else:
            return f'{color} rangli BMW yo`q'

    def momodel(self, model):
        amount = BMW.models.count(model.lower())
        if amount:
            return f"{model}: {amount} ta"
        else:
            return f"{model} modeli yo'q"


tesl = Tesla('Tesla 1', 'model x', 'oq')
tesl3 = Tesla('Tesla 1', 'model x', 'oq')
tesl2 = Tesla('Tesla 2', 'model y', 'qora')
bmw = BMW('BMW 1', 'model bmw_x', 'oq')
bmw2 = BMW('BMW 2', 'model bmw_y', 'qora')
print(bmw2.cocolor('qora'))
print(bmw2.momodel('model bmw_x'))
print(BMW.colors)
# print(tesl.qora, tesl.model_x)


