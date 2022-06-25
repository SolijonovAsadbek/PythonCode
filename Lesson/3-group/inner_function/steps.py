# def integer(integer_num):
# 	# 1-qadam
# 	# integer_num ni validatsiya qilamiz
# 	if not isinstance(integer_num, int):
# 		raise TypeError(f"funksiya faqat <class, 'int'> qabul qiladi, {type(integer_num)} emas.")

# 	def float_(float_num):
# 		# 2-qadam
# 		# float_num ni validatsiya qilamiz
# 		if not isinstance(float_num, float):
# 			raise TypeError(f"funksiya faqat <class, 'float'> qabul qiladi, {type(float_num)} emas.")

# 		def boolean(boolean_value):
# 			# 3-qadam
# 			# boolean_value ni validatsiya qilamiz
# 			if not isinstance(boolean_value, bool):
# 				raise TypeError(f"funksiya faqat <class, 'bool'> qiymat qabul qiladi, {type(boolean_value)} emas.")

# 			# Hamma olingan natijani birlashtirish
# 			def total():
# 				print(f"Butun son: {integer_num}")
# 				print(f"Float son: {float_num}")
# 				print(f"Boolean qiymat: {boolean_value}")

# 			# Hamma qiymat tekshiruvdan muvoffaqqiyatli o'tsa total() funsiya ishlaydi.
# 			return total()

# 		# boolean funksiyani kutib turadi
# 		return boolean

# 	# float_ funksiyani kutib turadi
# 	return float_

# i = integer(2)
# f = i(12.0)
# b = f(False)



# def chr_ascii(arg:str) -> dict:
     
# 	if not isinstance(arg, str):
# 	    raise TypeError(f'Sorry, argument expect str, not {type(arg)}')     
# 	def inner_ascii():
# 	    result = []
# 	    for i in set(list(arg)):
# 	        result.append((i, ord(i)))
# 	    return result
# 	return inner_ascii()
   

# print(chr_ascii("Python is very easy to learn!"))


# # himoyalangan a'zolarni ko'rsatish
 
# # Asosiy sinf yaratish
# class Base:
#     def __init__(self):
 
#         # Himoyalangan a'zo
#         self._a = 2
 
# # bola sinf yaratish
# class Derived(Base):
#     def __init__(self):
 
#         # Asosiy sinfning konstruktorini chaqirish
#         Base.__init__(self)
#         print("Asosiy sinfning himoyalangan a'zosini chaqirish: ", self._a)
 
#         # Himoyalangan o'zgaruvchini o'zgartiring:
#         self._a = 3
#         print("O'zgartirilgan himoyalangan a'zoni sinfdan tashqari chaqirish:", self._a)
 
 
# obj1 = Derived()
 
# obj2 = Base()
 
# # Himoyalangan a'zoni chaqirish
# # Kirish mumkin, lekin konventsiyaga ko'ra amalga oshirilmasligi kerak
# print("obj1 ning himoyalangan a'zosiga kirish:", obj1._a)
 
# # Himoyalangan o'zgaruvchiga tashqaridan kirish
# print("obj2 ning himoyalangan a'zosiga kirish:", obj2._a)



# Python program to
# demonstrate private members
 
# Creating a Base class
 
 
# class Base:
#     def __init__(self):
#         self.a = "GeeksforGeeks"
#         self.__c = "GeeksforGeeks"

#     # def _get_info(self):
#     #     return self.__c

#     def __get_info(self):
#         return self.__c

#     def get_info(self):
#         self.__c = 'Real python'
#         return self.__c
 
# # Creating a derived class
# class Derived(Base):
    

#     def base_info(self):
#         return Base._Base__get_info(self)

 
 
# # Driver code
# obj1 = Base()
# print(obj1.a)
# # print(obj1.__c)
# # print(obj1._get_info())

# obj2 = Derived()
# print(obj2.base_info())

# name = 'Alisher'

# if name == 'Elmurod':
#     print('Hello Elmurod')

# elif name == 'Xondamir':
#     print('Hello Xondamir')

# elif name == 'Alisher':
#     print('Hello Alisher')

# elif name == 'Asror':
#     print('Hello Asror')

# else:
#     print("Men kimligingni bilmayman!")

# # Hello Alisher

# names = {
#     'Alisher': 'Salom Alisher',
#     'Xondamir': 'Salom Xondamir',
#     'Asror': 'Salom Asror',
#     'Elmurod': 'Salom Elmurod'
# }

# a = int(input("sana:"))

# start = a // 10
# end = a % 10

# s = ""
# match start:
#     case 1:
#         s += 'O\'n'
#     case 2:
#         s += 'Yigirma'
#     case 3:
#         s += 'O\'ttiz'

# match end:
#     case 1:
#         s += " " + 'bir'
#     case 2:
#         s += " " + 'ikki'
#     case 3:
#         s += " " + 'uch'
#     case 4:
#         s += " " + 'turt'
#     case 5:
#         s += " " + 'besh'
#     case 6:
#         s += " " + 'olti'
#     case 7:
#         s += " " + 'yetti'
#     case 8:
#         s += " " + 'sakkiz'
#     case 9:
#         s += " " + 'tuqqiz'
#     case 0:
#         s += " "


# oy = int(input("Oy: "))

# match oy:
#     case 1:
#         s += ' - Yanvar'
#     case 2:
#         s += ' - Fevral'
#     case 3:
#         s += ' - Mart'
#     case 4:
#         s += ' - Aprel'
#     case 5:
#         s += ' - May'
#     case 6:
#         s += ' - Iyun'
#     case 7:
#         s += ' - Iyul'
#     case 8:
#         s += ' - Avgust'
#     case 9:
#         s += ' - Sentabr'
#     case 10:
#         s += ' - Oktabr'
#     case 11:
#         s += ' - Noyabr'
#     case 12:
#         s += ' - Dekabr'
#     case _:
#         print("Bunday oy mavjud emas")
    
# print(s)

# case 20

# kun_oy = float(input("Kun.Oy: "))
# kun = int(kun_oy)
# oy = round(kun_oy - kun, 2)

# match kun_oy:

#     case kun_oy if (20 <= kun <= 31 and oy == 0.1) or (1 <= kun <= 18 and oy == 0.2):
#         print("Qovga")

#     case kun_oy if (19 <= kun <= 28 and oy == 0.2) or (1 <= kun <= 20 and oy == 0.3):
#         print("Baliq")

#     case kun_oy if (21 <= kun <= 31 and oy == 0.3) or (1 <= kun <= 19 and oy == 0.4):
#         print("Qo'y")

#     case kun_oy if (20 <= kun <= 30 and oy == 0.4) or (1 <= kun <= 20 and oy == 0.5):
#         print("Buzoq")

#     case kun_oy if (21 <= kun <= 31 and oy == 0.5) or (1 <= kun <= 21 and oy == 0.6):
#         print("Egizaklar")

#     case kun_oy if (22 <= kun <= 30 and oy == 0.6) or (1 <= kun <= 22 and oy == 0.7):
#         print("Qisqichbaqa")

#     case kun_oy if (23 <= kun <= 31 and oy == 0.7) or (1 <= kun <= 22 and oy == 0.8):
#         print("Arslon")

#     case kun_oy if (23 <= kun <= 31 and oy == 0.8) or (1 <= kun <= 22 and oy == 0.9):
#         print("Parizod")

#     case kun_oy if (19 <= kun <= 30 and oy == 0.9) or (1 <= kun <= 22 and oy == 0.10):
#         print("Tarozi")

#     case kun_oy if (23 <= kun <= 31 and oy == 0.10) or (1 <= kun <= 22 and oy == 0.11):
#         print("Chayon")

#     case kun_oy if (23 <= kun <= 30 and oy == 0.11) or (1 <= kun <= 21 and oy == 0.12):
#         print("O'q otar")

#     case kun_oy if (22 <= kun <= 31 and oy == 0.2) or (1 <= kun <= 19 and oy == 0.1):
#         print("Echki")


# from datetime import datetime
# from os import scandir

# def convert_date(timestamp):
#     d = datetime.utcfromtimestamp(timestamp)
#     formated_date = d.strftime('%d %b %Y')
#     return formated_date

# def get_files():
#     dir_entries = scandir('D:/install')
#     for entry in dir_entries:
#         info = entry.stat()
#         print(f"{entry.name}  Last modified: {convert_date(info.st_mtime)}")





















































