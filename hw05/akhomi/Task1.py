# # # Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
import random

a = []
pair_a = 0
not_pair = 0
for i in range(10):
    a.append(int(random.random() * 100))
print(a)
even = 0
odd = 0

for number in a:
    if number%2 == 0:
        even += 1
    else:
        odd += 1
print(f'Even numbers: {even}')
print(f'Odd numbers: {odd}')






