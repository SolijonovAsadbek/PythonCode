# 1-savol
# print_ funksiyasi
# kiritilgan parmetrlarni ekranga chiqrib beradi

# 2-savol
# primitiv tiplar bu  intejr,float, string,complex,boleen

# 3-savol
# list dinamik boladi [] bilan yoziladi
# tuple o'zgarmas boladi () ichida yoziladi va listan tezroq ishlaydi
# string dinamik boladi () ichida yoziladi

# 4-savol
# a=True
# while a:
#     print("1")
#     print("2")
#     if True:
#         print("3")
#         print("4")
#         break
#     print("5")
# bunda 1,2,3,4 chiqadi holos


# while a:
# print("1")
# print("2")
# print("3")
# if True:
#     print("4")
#     continue
# print("5")
# print("6")
# bunda faqat 1,2,3 sonlari chiqadi va sikilanib qoladi

# while a:
#     print("1")
#     print("2")
#     print("3")
#     if True:
#         a=False
#         print("4")
#         print("5")
#     print(6)
# bunda 1,2,3,4,5,6 sonlar chiqadi va toxtaydi

# 5-savol
# funksiyani  avzaligi birmarta yaratilgan dasturdan qayta qayta ishlatiladi agar kodni ozgartirmoxchi bolsabgiz bitasino
# o'zgartirish kifoya qiladii

# 6-savol
# dictionary kalit va qiymatlar bilan ishlashda kerak boladi { } qavs ichida yoziladi
# va dinamik hisoblanadi

# 7-savol
# dastur bajarilayotganda listda manapulatsiya sekinroq boladi chunki unda imkoniyatlar koproq

# 8-savol
#
#
# def f(*args):
#     for i in args:
#         print(i)
# f(1,2,3,6,4,6)

# def f(**kvargs):
#     for i,n in kvargs:
#         print(i ,n)
# f(olma=1,nok=2)


# 9-savol
# string=(1,2,3,4)
# string[:]
# print(string)
#
# list=[1,2,3,6]
# list[:]
# print(list)
# farqi yoq

# 10-misol
# a=[1,2,3,6]
# a+=[5,7,5]
# print(a)


# AMALIY
# 1-savol
# s=int(input("s="))
# m=int(input("m="))
# if (6<=s<=12) and (0<=m<=60):
#     print("morning")
# elif (12<=s<=18) and (0<=m<=60):
#     print("afternon")
# elif (18<=s<=24) and (0<=m<=60):
#     print("evening")
# elif (0<=s<=6) and (0<=m<=60):
#     print("midningh")
# else:
#     print("xato")

# 2-savol
# n = int(input("2 dan 100 gacha son kiriting="))
# s = []
# for i in range(1, n + 1):
#     for a in range(1, i):
#         if i / a == i or i / a == 1:
#             s += i
# print(s)

# 4-savol
# n=int(input("n="))
# m=int(input("m="))
# a=1
# b=1
# for i in range(1,n+1):
#     a*=i
# for g in range(1,m+1):
#     b*=g
# print(a/b)
#
#
# 3-misol
# def f(*args):
#     a=1
#     s=0
#     for i in args:
#         a*=i
#         s+=1
#     return a**(1/s)
# x=f(3,3)
# print(x)


# Jami 75 ball
