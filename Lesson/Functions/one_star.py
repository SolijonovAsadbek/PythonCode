a = [1, 2, 3.5, 4.57, 0, -3, -101.5]
b = (2.5, -0.7, 0.9, 1, 0)

# *(bitta yulduzcha) - ning pythonda tutgan o'rni.
# def my_func(*args) da formal parametrga qo'yilgan *(yulduzcha) - istalgancha qiymatlarni olish
# manosida ishlatilgan bo'ladi.

# my_func(*a, *b) actual parametrda qo'yilgan *(yulduzcha) - o'ramlarni ochish maqsadida ishlatilgan bo'ladi.
# 1 - usul
# def my_func(*args):
#     print(args)
#
#
# my_func(a, b)      # ([1, 2, 3.5, 4.57, 0, -3, -101.5], (2.5, -0.7, 0.9, 1, 0))


# 2 - usul
# def my_func(*args):
#     print(args)
#
#
# my_func(*a, *b)      # (1, 2, 3.5, 4.57, 0, -3, -101.5, 2.5, -0.7, 0.9, 1, 0)


# def square(*numbers):
#     my_list = []
#     for num in numbers:
#         x = num ** 2
#         my_list.append(x)
#     return tuple(my_list)
#
#
# result = square(1, 2, 4, 5, 6)
# print(result)

from pprint import pprint


def total_dev(*numbers):
    """Bu funksiya barcha berilgan sonlarni bo'linuvchilarini sonini aniqlaydi."""

    if numbers:
        my_dict = {}
        for num in numbers:
            count = ("barcha natural sonlar" if num == 0 else 0)
            if len(str(num)) < 5:
                for i in range(1, num + 1):
                    if num % i == 0:
                        count += 1

                my_dict.update(dict([(num, f"{count}{('' if isinstance(count, str) else ' ta')}")]))
            else:
                my_dict.update(dict([(num, "Kichikroq son yoz inson")]))
                break
    else:
        my_dict = None

    return my_dict


res = total_dev(0, 2, 10, 4, 5, 6, 7902)
pprint(res)
