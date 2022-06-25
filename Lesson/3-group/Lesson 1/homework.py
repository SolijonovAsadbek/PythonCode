# Kvatratning tomoni a berilgan, Uning
# Perimetirini topish dasturi.
# a = float(input("Kvatrat tomoni a: "))
# P = 4*a
# print("Kvatratning Perimetiri: ", P)

# Begin 40
a1 = float(input("A1: "))
b1 = float(input("B1: "))
c1 = float(input("C1: "))
a2 = float(input("A2: "))
b2 = float(input("B2: "))
c2 = float(input("C2: "))
print(f"|{a1}x+{b1}y = {c1}")
print(f"|{a2}x+{b2}y = {c2}")   
D = a1*b2 - a2*b1
x = (c1*b2 - c2*b1)/ D
y = (a1*c2 - a2*c1)/ D

print("|x: ", x)
print("|y: ", y)
    
