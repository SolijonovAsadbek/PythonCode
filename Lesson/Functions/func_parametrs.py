# parametrlarni funksiyaga uzatish
# fname, lname - forml parametrlar
# fname = 'Asilbek', lname = 'Masrurov'  - actual paratrlar.
import random   # randomayz qilish uchun ishlatamiz bu kutubxonani


def my_parm_func(fname, lname):
    return f"To'liq ismi: {fname} {lname}\nemail: {(fname + lname).lower() + str(random.randint(100, 1000))}@gmail.com"


# qiymatlarni pozitsion uztash
ma = my_parm_func('Asilbek', 'Masrurov')
# sa = my_parm_func('Asilbek', 'Solijonov')
print(ma)
# print(sa)

# kalit qiymat ko'rinishida uzatish
# ma = my_parm_func(lname='Masrurov', fname='Asilbek')

# kalit qiymat uzatilgandan keyin o'n tomonda pozitsion uzatib bo'lmaydi.
# ma = my_parm_func(lname='Masrurov', 'Asilbek')

# pozitsion qiymatdan keyin o'ng tomonda 'kalit=qiymat' ko'rinishida qiymat uzatishingiz mumkin.
# ma = my_parm_func('Asilbek', lname='Asilbek')
