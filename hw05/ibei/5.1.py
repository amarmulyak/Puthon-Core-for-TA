# Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
import random

a = []
for i in range(10):
    a.append(int(random.random() * 100))

print(a)

b =[]
c =[]

for i in a:
    if i%2:
        b.append(i)
    else:
        c.append(i)

print (b, 'not even:', len(b), c, 'even:',len(c))

