# a = input("Nom kiriting: ")
# b = input("Nom_2 ni kiriting: ")

# if a > b:
# 	print("Birinchi nom katta.")
# else:
# 	print("Ikkinchi nom katta")


# a = True

# match a:
# 	case True:
# 		print(True)
# 	case False:
# 		print(False)

# Result: True 



# a = False

# match a:
# 	case True:
# 		print(True)
# 	case False:
# 		print(False)

# Result: False



# print("2 ga Qoldiqli bo'lishga doir algoritim.")
# a = float(input("Katta son kiriting:"))
# c = a%2

# match c:
# 	case 1:
# 		print(f"Siz kiritgan {a} soni 2ga qoldiqli bo'linar ekan.")
# 	case 0:
# 		print(f"Siz kiritgan {a} soni 2ga qoldiqsiz bo'linar ekan.")


# print("Sonni o'qib beruvchi dastur.")
# print('='*12)

# a = int(input("Son kiriting: ")) 
# c = a%10
# b = ""
# if a >= 10:
# 	dec = a // 10
# 	match dec:
# 		case 1:
# 			b ="o'n "
# 		case 2:
# 			b ="yigirma "
# 		case 3:
# 			b ="o'ttiz "
# 		case 4:
# 			b ="qiriq "
# 		case 5:
# 			b ="ellik "
# 		case 6:
# 			b ="oltmush "
# 		case 7:
# 			b ="yetmush "
# 		case 8:
# 			b ="sakson "
# 		case 9:
# 			b ="to'qson "
# match c:
# 	case 0:
# 		b +=""
# 	case 1:
# 		b +="bir"
# 	case 2:
# 		b +="ikki"
# 	case 3:
# 		b +="uch"
# 	case 4:
# 		b +="to'rt"
# 	case 5:
# 		b +="besh"
# 	case 6:
# 		b +="olti"
# 	case 7:
# 		b +="yetti"
# 	case 8:
# 		b +="sakkiz"
# 	case 9:
# 		b +="to'qqiz"
# print(b)

	
# a = input("Hafta kunini kiriting: ")

# match a:
# 	case "Yakshanba":
# 		print("Haftaning birinchi kuni")
# 	case "Dushanba":
# 		print("Haftaning ikkinchi kuni")
# 	case "Seshanba":
# 		print("Haftaning uchunchi kuni")
# 	case "Chorshanba":
# 		print("Haftaning to'tinchi kuni")
# 	case "Payshanba":
# 		print("Haftaning beshinchi kuni")
# 	case "Juma":
# 		print("Haftaning oltinchi kuni")
# 	case "Shanba":
# 		print("Haftaning yettinchi kuni")
	

# count = 0
# a = True
# while a:
# 	count += 1
# 	print(count)
# 	if count == 100:
# 		break



# count = 0
# print(count<100)
# while count < 100:
# 	count += 1
# 	if bool(count % 2):
# 		print(count)


# a = "Python", "Django", "Flask"
# print(a)
# print(type(a))
# print('-'*20)
# a = "Atom"
# print(a)
# print(type(a))
# print('-'*20)
# a = "Atom", 'SublimeText'
# print(a)
# print(type(a))
# print('-'*20)
# a = 1, 'SublimeText', bool(12), 2+3j
# print(a)
# print(type(a))

#TUPLE
# a = "Python", "Django", "Flask"
# a[1] = True    # ❌
# print(a)
# print("Tuple tipini elementini hech qachon o'zgartirib bo'lmaydi.")  # ✅

# STR
# a = "Django"
# a[3] ='g'	 # ❌
# print(a)
# print("String tipini elementini hech qachon o'zgartirib bo'lmaydi.")  # ✅


# a = "Hello"
# print(a)

# a, b, c, d, e = "Hello" # ❌
# print(a)
# print(e)

# a, b, c, d, e, r= "Hello" # ❌
# print(a)
# print(d)


# a, b, c = 12, 13, 14  # ✅
# print(a)
# print(c)


# a = 12 -1j

# if a.imag >0 or a.imag <0:
#     print("Complex son")
# else:
#     print("Complex son emas")
 
# import math

# a = input("Doira Radiusini kiriting: ")

# L = 2*math.pi*float(a)
# print("Doira uzunligi {:.2f} ga teng".format(L))


# A.musobaqa
# a = int(input("O'quvchilar sonini kirting: "))
# from datetime import datetime
# time1 = datetime.now()
# jamoa = 0
# if a%6 > 0:
# 	jamoa = a//6 + 1
# else:
# 	jamoa = a//6
# time2 = datetime.now()
# print(f"Minmal yig'iladigan jamoa: {jamoa}  ta")
# print("time: ", time2-time1)


# D.o'yin
# time1 = datetime.now()
# n = input("O'yinlar soni: ")
# x = input("Achkolarni kriting: ")
# player_1 = input("Birinchi o'yinchi nomi: ")
# player_2 = input("Ikkinchi o'yinchi nomi: ")
# list_mark = x.split(" ")
# if int(n) == len(list_mark):
# 	total_1 = 0
# 	total_2 = 0
# 	for dx, ue in enumerate(list_mark, start=1):
# 		if dx%2 == 1:
# 			total_1 += int(ue)
# 		else:
# 			total_2 += int(ue)
# 	print(f"{player_1} natijasi: ", total_1)
# 	print(f"{player_2} natijasi: ", total_2)

# time2 = datetime.now()
# print("Sarflangan vaqt: ", time2 - time1)

# If else ishlatmaslik kerak.
# a = int(input())
# print({True: "Juf son", False: "Toq son"} [a%2==0])

# print(["Qoldiq qolmaydi", "Bir qoldiq qoladi.", "Ikki qoldiq oqladi.", "uch qoldiq qoladi."][a%3])

# print(f"{1202191.892312:,.2f}")

