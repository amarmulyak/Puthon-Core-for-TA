# Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
import random

a = []
for i in range(10):
    a.append(int(random.random() * 100))
print(a)
odd = [i for i in a if i % 2 != 0]
even = [i for i in a if i % 2 == 0]

# for the second solution remove code in the square brackets
# for i in a:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

print("%s odd numbers in a" % (len(odd)))
print("%s even numbers in a" % (len(even)))

