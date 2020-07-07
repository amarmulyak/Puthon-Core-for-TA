# В даному списоку визначити значення яке(і) найбільше зустрічається.

from random import random

a = [int(random()*5) for i in range(15)]
print(a)
set_a = set(a)
max_value = None
quantity = 0
for i in set_a:
    qty = a.count(i)
    if qty > quantity:
        quantity = qty
        max_value = i
print(max_value)

