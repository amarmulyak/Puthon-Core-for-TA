# Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.

import random

a = []
even_num = 0
odd_num = 0
for i in range(10):
    a.append(int(random.random() * 100))

    if a[i] % 2 == 0:
        even_num += 1
    else:
        odd_num +=1

print("The list " + str(a) + " has " + str(even_num) + " even numbers and " + str(odd_num) + " odd numbers")