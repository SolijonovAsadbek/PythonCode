# Birinchi time modulidan 'sleep()' funksiyasini chaqirib olamiz.
from time import sleep


# 'progress()' nomli funktsiya 'perecent' va 'width' deb nomlangan  2 ta parametr qabul qiladi.
# 'precent' - foiz uchun
# 'width' - bu foiz to'ladigan qismning eni(belgilar soni)
def progress(precent=0, width=30):
    left = precent * width // 100
    right = width - left
    # '\r' - vazifasi chop etishni boshlang'ich pozitsiyasini ushlab turish uchun xizmat qiladi.
    print('\r[' + f'▌' * left + ' ' * right + f'] {precent:.0f}%', end='')


print("Inlab Academy bilan birga o'rganing.")
# for siklda endi yuqorida yaratgan 'progress()' nomli funktsiyamizni ishga tushiramiz.
for i in range(101):
    # yuqoridagi yaratgan funktsiyamizni chaqiryapmiz
    progress(i)

    # sleep(0.1) bu dastur ishlashini 0.1 sekundga kechiktirish uchun
    # agar yozilmasa biz bo'layotgan jarayonni ilg'ayolmay qolamiz.
    sleep(0.1)

    if i == 100:
        print(f"\nBiz aynan sizni kutyapmiz! {chr(9787)}\n"
              f"{chr(9742)}: (69) 239-50-39")
