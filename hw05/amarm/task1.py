import random

'''Генерується список випадкових цілих чисел. Визначається, скільки в ньому
парних чисел, а скільки непарних.

import random

a = []
for i in range(10):
    a.append(int(random.random() * 100))

print(a)'''

a = []
for i in range(10):
    a.append(int(random.random() * 100))
print(a)

pair = []
odd = []

for element in a:
    if element % 2 == 0:
        pair.append(element)
    else:
        odd.append(element)
print(f'''In the list above {len(pair)} pair number(s)
and {len(odd)} odd number(s)''')
