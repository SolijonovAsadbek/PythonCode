while True:
    n = int(input("n = "))
    if n <= 1:
        print("Bir sonidan katta son kiriting!")
        continue
    else:
        break
toplam = []
for i in range(1, n + 1):
    a = int(input(f"a{i} = "))
    toplam.append(a)
toplam_new = []
min_ = toplam[0] + toplam[1]
max_ = toplam[0] + toplam[1]
for j in range(len(toplam) - 1):
    toplam_new.append(toplam[j] + toplam[j + 1])
    if min_ >= (toplam[j] + toplam[j + 1]):
        min_ = (toplam[j] + toplam[j + 1])
    if max_ <= (toplam[j] + toplam[j + 1]):
        max_ = (toplam[j] + toplam[j + 1])
print(toplam)
print(toplam_new)
print(f"Minimal yig'indi: {min_} , Maximal yig'indi: {max_} ")
