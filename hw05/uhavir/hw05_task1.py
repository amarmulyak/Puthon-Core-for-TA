# Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
import random

a = []
for i in range(10):
    a.append(int(random.random() * 100))
print(a)
even = [i for i in a if i % 2 == 0]
odd = [i for i in a if i % 2 == 1]
print(len(even))
print(len(odd))
