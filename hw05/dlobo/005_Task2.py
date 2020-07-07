# 1. Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
# 2. Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.
import random
a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)
print(a)

positive = [x for x in a if x > 0]
negative = [x for x in a if x < 0]
print("Positive numbers are", positive)
print("Negative numbers are", negative)