"""2. Вихідний список містить позитивні і негативні числа.
Потрібно позитивні помістити в один список, а негативні - в інший."""
import random
int_list = [random.randint(-100,100) for i in range(25)]

positive = []
negative = []
for i in int_list:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)
print(int_list)
print(positive)
print(negative)