# Вихідний список містить позитивні і негативні числа.
# Потрібно позитивні помістити в один список, а негативні - в інший.

import random

a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)
print(a)

positive = [i for i in a if i >= 0]
negative = [i for i in a if i < 0]

print(positive)
print(negative)