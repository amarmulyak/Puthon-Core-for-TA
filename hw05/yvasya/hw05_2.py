# Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.

import random

a = []
a_pos = []
a_neg = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)

    if a[i] > 0:
        a_pos.append(a[i])
    else:
        a_neg.append(a[i])

print("The whole list: " + str(a)+ "\n")
print("The list with positive numbers: " + str(a_pos) + "\n")
print("The list with negative numbers: " + str(a_neg) + "\n")