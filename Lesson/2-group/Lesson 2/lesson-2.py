# Misol
# a = "Python"
# print(a)
# print("a[0]: ", a[0])  # Birinchi indexga murojat
# print("a[-1]: ", a[-1])   # Oxirgi indexga murojat
# middle = len(a) // 2
# print("a[middle]: ", a[middle])   # O'tasidagi elementga murojat.

# Natijasi:
# Python
# a[0]:  P
# a[-1]:  n
# a[middle]:  h


# =============================
# String Slice  - Satrni kesish
# a = "Python"
# print(a)   # Python
# print(a[0:len(a)])  # Python
# print(a[:])   # Python
# print(a[-6:])  #Python
# print(a[:3])  # Pyt

# a = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Quasi sapiente soluta vitae fugiat eligendi minus saepe odit? Soluta ullam laborum perferendis minus repellendus veritatis. Corrupti enim facere illo temporibus dolorem.            Maxime, eveniet obcaecati labore non commodi, dicta iusto laudantium reprehenderit sed veniam, consectetur minus perspiciatis nostrum aspernatur nobis accusamus! Beatae optio dolores soluta sed amet id blanditiis in, ipsum"
# print(a)
# print('='*20)
# print(a[10:30])

# a = "Durbek"
# print(a)  # Durbek
# print(a[::2])   # Dre
# print(a[::-1])  # kebruD
# print(a[::-2])  # kbu


# Palindrom son.  111 = 111, 121 = 121, 
# print("Palindrom sonni aniqlovchi dastur.")

# a = input("Son: ")
# if int(a) == int(a[::-1]): ✅
# 	print("Palindrom son ekan.")
# else:
# 	print("Palindrom emas.")


# a = int(input("Son: ")) 
# if a == a[::-1]:  ❌
# 	print("Palindrom son ekan.")
# else:
# 	print("Palindrom emas.")


# a = "PytHoN ProGramMing Language"
# print("a= ", a)    # PytHoN ProGramMing Language
# print("a.capitalize(): ", a.capitalize())  # Python programming language
# print("a.upper(): ", a.upper())  # PYTHON PROGRAMMING LANGUAGE
# print("a.lower(): ", a.lower())  # python programming language
# print("a.swapcase(): ", a.swapcase())  # pYThOn pROgRAMmING lANGUAGE
# print("a.title(): ", a.title())  # Python Programming Language


# a = "Meni ismim Toshpo'lat. Meni yoshim 16 da. Men katta bo'lsam dasturchi bo'laman. Dasturchilar zamon bilan doim hamnafas bo'lishadi."
# print(a)

# print("Meni: ", a.count("Meni", 1, 10), " ta ekan.") # 0
# print("INDEX: ", a.find("kattaman"))  # -1
# print("Oxirini tekshiradi: ", a.endswith("po'lat."))  # False
# print("Oxirini tekshiradi: ", a.endswith("bo'lishadi."))  # True

# a = "Django"
# print(a)
# print(a.replace("n", "g"))