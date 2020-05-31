import random

'''
Вихідний список містить позитивні і негативні числа. Потрібно позитивні
помістити в один список, а негативні - в інший.

import random

a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)

print(a)
'''

a = []
for i in range(20):
    a.append(int(random.random() * 20) - 10)
print(a)

positive = []
negative = []

for element in a:
    if element >= 0:
        positive.append(element)
    else:
        negative.append(element)
print(f'''From the list above we have:
List of positive numbers {positive}
List of negative numbers {negative} 
''')
