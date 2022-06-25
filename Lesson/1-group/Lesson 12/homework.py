# while4
# n = int(input("n: "))
# count = 0
# multiple = 1
# while multiple <= n:
#     multiple *= 3
#     count += 1
#     if multiple == n:
#         print(f"{n} 3 ning {count} darajasiga teng.")
#         break
# else:
#     print(f"{n} soni 3 ning darajasi emas.")

# array 11
# arrs = [12, 23, 43, 45, 190, 290, 2302, 230, 290]
#
# while True:
#     k = int(input("k: "))
#     for index in range(k, len(arrs)):
#         inx = dict(true=index, false=0)
#         inx_bool = f'{index % k == 0}'.lower()
#         arrs[0] = ""
#         print(arrs[inx.get(inx_bool)], end=".")
#     print()
# import math
# x= int (input('x = '))
# n= int (input('n = '))
# summ=0
# d=-1
# count=1
# fact=1
# for i in range(1,n):
#     if n==0:
#         fact=1
#     else:
#         count+=1
#         fact*=count
#         count+=1
#         fact*=count
#         summ=(d**n*x**2*n+1)/fact
# print(summ)
# print(math.sin(x))
# n = int(input('A = '))
# a = 2
# for i in range(1, n + 1):
#     ak = 2 + 1 / a
#     print(f'{i}','- hadi', a)
#     a = ak
#
# a = int(input('a = '))
# b = int(input('b = '))
#
# for i in range(a + 1, b):
#     for j in range(i):
#         print(i, end=('.'if j!=i-1 else '\n'))
# for 37
# n = int(input('a = '))
# summ = 0
# for i in range(0, n + 1):
#     c = 1
#     k = n + 1
#     for j in range(k - i):
#         c *= i
#     summ += c
#     print(c)
#     print('-->', summ)
# mas = [1,-2,3,5,4,6]
# minn = mas[0]
# for i in range(len( mas )):
#     if minn >= mas[i]:
#         minn = mas[i]
# print(minn)

#
# def f(a: int, b: float) -> float:
#     return a * b
#
#
# a = f('Salom', 12)
# print(a)
# print(f.__annotations__['a'])
