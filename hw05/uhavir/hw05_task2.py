# Вихідний список містить позитивні і негативні числа.
# Потрібно позитивні помістити в один список, а негативні - в інший.
import random

a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)

print(a)
positive = [j for j in a if j > 0]
negative = [j for j in a if j < 0]
print(positive)
print(negative)
