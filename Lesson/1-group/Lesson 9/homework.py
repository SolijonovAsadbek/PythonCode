# while 28
# e = float(input("e: "))
# next_ = 0
# k = 2
# start = 2
# end = 2 + 1 / start
# while True:
#     if abs(start - end) < e:
#         print("eng kichigi k=", k)
#         print(f"a{k - 1}: ", start)
#         print(f"a{k}: ", end)
#         break
#     else:
#         start = end
#         end = 2 + 1 / start
#         k += 1
#         continue


# while 30
a = int(input("a: "))
CONST = a
b = int(input("b: "))
c = int(input("c: "))
count = 0
while True:
    if a >= c:
        a -= c
        count += 1
    else:
        if b >= c:
            b -= c
            a = CONST
            if b == 0:
                break

print(count)
