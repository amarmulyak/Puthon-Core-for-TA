# В даному списоку визначити значення яке(і) найбільше зустрічається.
from random import random

a = [int(random()*5) for i in range(15)]
print(a)
digit = []
# a.sort()
a = str(a)
# print(type(a))
zero = a.count('0')
one = a.count('1')
two = a.count('2')
three = a.count('3')
four = a.count('4')
digit.append(zero)
digit.append(one)
digit.append(two)
digit.append(three)
digit.append(four)
print(digit)
print(max(digit))






