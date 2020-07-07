#Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
import random

a = []
b = []
c = []
for i in range(10):
    a.append(int(random.random() * 100))
for x in a:
    if x%2 == 0 and x!=0:
        b.append(x)
    else:
        c.append(x)


print(a)
print("Paired numbers in list {} ".format(b), "is", len(b))
print("Unpaired numbers in list {} ".format(c), "is", len(c))