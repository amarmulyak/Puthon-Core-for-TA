# Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.
import random

a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)

print(a)
positive_numbers = []
negative_numbers = []
for number in a:
    if number >= 0:
        positive_numbers.append(number)
    else:
        negative_numbers.append(number)
print(positive_numbers)
print(negative_numbers)