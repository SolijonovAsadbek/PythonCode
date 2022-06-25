# Array6
# n = int(input("n: "))
# a = float(input('a[0]: '))
# b = float(input('a[1]: '))
#
# my_list = [a, b]
# if n > 2:
#     for j in range(n-2):
#         c = 0
#         for x in range(len(my_list)):
#             c += my_list[x]
#         my_list.append(c)
#
# print(my_list)

# Array10
# arr = [0, 12, 34, 21, 23, 32, 10]
# even_arr = []
# odd_arr = []
#
# for i in arr:
#     if i % 2 == 0:
#         even_arr.append(i)
#     else:
#         odd_arr.append(i)
#
# arr.clear()
# arr.extend(even_arr)
# arr.extend(odd_arr[::-1])
#
# print(arr)

# Array16
# arr = [1, 23, 3, 23121, 2101, 0]
# new_arr = []
# for i in range(0, len(arr)):
#     new_arr.append(arr[i])
#     new_arr.append(arr[(len(arr) - 1) - i])
# print(new_arr)


# Array17ch
# arr = [12, 123, 1, 0, 89, 129]
#
# new_arr = []
#
# for i in range(0, len(arr) - 1, 2):
#     new_arr.append(arr[i])
#     new_arr.append(arr[i + 1])
#     new_arr.append(arr[(len(arr) - 1) - i])
#     new_arr.append(arr[(len(arr) - 1) - (i + 1)])
#
# print(new_arr)

# def f(my_list=None):
#     if my_list is None:
#         my_list = []
#     my_list.append('*new*')
#     return my_list

n = int(input("n: "))

start = n // 100
mid = (n // 10) % 10
end = n % 10
s = ""
indx = -1
args = [start, mid, end]
for i in args:
    indx += 1
    match i:
        case 1:
            s += ["bir yuz", ' o\'n', ' bir'][indx]
        case 2:
            s += ["ikki yuz", ' yigirma', ' ikki'][indx]
        case 3:
            s += ['uch yuz', ' o\'ttiz', ' uch'][indx]
        case 4:
            s += ["to'rt yuz", ' qiriq', ' to\'rt'][indx]
        case 5:
            s += ["besh yuz", ' ellik', ' besh'][indx]
        case 6:
            s += ['olti yuz', ' oltmish', ' olti'][indx]
        case 7:
            s += ['yetti yuz', ' yetmish', ' yetti'][indx]
        case 8:
            s += ['sakkiz yuz', ' sakson', ' sakkiz'][indx]
        case 9:
            s += ['to\'qqiz yuz', ' to\'qson', ' to\'qqiz'][indx]

print(s)
