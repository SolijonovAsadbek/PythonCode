# from itertools import cycle
# from time import sleep
#
# # cycle(r'')  - vazifasi rekursiyani taminlab beradi
# # Rekursiya bu cheksizlikni bir yana bir nomlanishi
# count = 0
# for frame in cycle(r'--\\||//--\\||//'):
#     count += 1
#     if count == 4:
#         count = -1
#         continue
#     print('\r', frame, '.' * count, sep='', end='', flush=True)
#     sleep(0.5)


from itertools import cycle
from time import sleep

for frame in cycle(r'-\|/-\|/'):
    print('\r', frame, sep='', end='', flush=True)
    sleep(0.2)
