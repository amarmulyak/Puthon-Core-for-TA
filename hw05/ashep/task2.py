#Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.
import random

a = []
b = []
c = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)
for x in a:
        if x<0:
            b.append(x)
        elif x>=0:
            c.append(x)

print(a)
print("Negative {} ".format(b))
print("Positive {} ".format(c))