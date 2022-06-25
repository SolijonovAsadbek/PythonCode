# # while 16
# # begin = 10
# # day = 1
# # km = begin
# # precent = int(input("foiz: "))
# # precent = (precent + 100) / 100
# # # list_ = []
# # while km < 200:
# #     day += 1
# #     begin *= precent
# #     # list_.append(begin)
# #     km += begin
# # print(day)
# # # print(list_)
# # # print(sum(list_))
#
# # while 16
# # n = int(input("n: "))
# # m = n
# # count = 0
# # while n > 0:
# #     m %= 10
# #     n //= 10
# #     if m % 2 != 0:
# #         count += 1
# #     m = n
# # print(count)
# # print(count > 0)
#
#
# # while 22
# # n = int(input("n: "))
# # div = 0
# # count = 1
# # while count < n-1:
# #     count += 1
# #     if n % count == 0:
# #         div += 1
# # print(div == 0)
#
# # while 27
# fib = int(input("fib: "))
# start = 0
# end = 1
# next_ = start + end
# had = 3
# s = ""
# while next_ < fib:
#     start = end
#     end = next_
#     next_ = start + end
#     had += 1
#     if fib == next_:
#         s += f"{fib} fibonachi soni va {had}-had ga to'g'ri keladi"
#
# if s:
#     print(s)
# else:
#     print(f"{fib} Fibonachi soni emas")

# array 5
# m_v = [(12, 144), (3, 90), (7, 12), (3, 100)]
# my_list = []
# for massa, hajm in m_v:
#     my_list.append([massa, massa/hajm, hajm])
# print(my_list)
#
# max_ = my_list[0][1]
# min_ = my_list[0][1]
# for i in range(len(my_list)):
#     if max_ <= my_list[i][1]:
#         max_ = my_list[i][1]
#     if min_ >= my_list[i][1]:
#         min_ = my_list[i][1]
# print(min_)
# print(max_)


# array 11, 16, 21
# massiv = [-1, -3, 9, 100, 12, -3, -8, 73]
# max_ = massiv[0]
# min_ = max_
# min_index = 0
# max_index = 0
# sum_ = 0
# for i in range(len(massiv)):
#     if min_ >= massiv[i]:
#         min_ = massiv[i]
#         min_index = i
#
#     if max_ <= massiv[i]:
#         max_ = massiv[i]
#         max_index = i
#     sum_ += massiv[i]
# print("O'rta arif: ", (sum_ - max_ - min_) / (len(massiv) - 2))
# print(max_, f'indeks: {max_index}')
# print(min_, f'indeks: {min_index}')

# array 26
# massiv = [12, 56, 57, 59, 90, 82, 32, 35, 87]
#
# count = 0
# for i in range(len(massiv)-1):
#     if (massiv[i] % 2 == 0 and massiv[i+1] % 2 != 0) or (massiv[i] % 2 != 0 and massiv[i+1] % 2 == 0):
#         count += 1
# print("Ketma-ket juft sonlar max qiymati: ", count)

