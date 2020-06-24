"""1. Генерується список випадкових цілих чисел.
Визначається, скільки в ньому парних чисел, а скільки непарних.
"""
import random
int_list = [random.randint(0,100) for i in range(25)]

odd = 0
even = 0
for i in int_list:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print(int_list)
print(even)
print(odd)