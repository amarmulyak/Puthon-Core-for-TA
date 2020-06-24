# В даному списоку визначити значення яке(і) найбільше зустрічається.

from random import random

a = [int(random() * 5) for i in range(50)]
print(a)
x = 0
for i in range(5):
    count_i = a.count(i)

    if count_i > x:
        elem = i
        x = count_i
print("The most frequent value is %s:" % elem, "It occurs %s times." % x)
# d = {}
# for i in a:
#     if not d.get(i):
#         d[i] = 0
#     d[i] += 1
# max_value = max(d.values())
# for k, v in d.items():
#     if v == max_value:
#         print(k)
# from pprint import pprint
# pprint(d)
