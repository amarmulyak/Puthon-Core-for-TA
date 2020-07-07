# В даному списоку визначити значення яке(і) найбільше зустрічається.
from random import random

a = [int(random()*5) for i in range(15)]
print(a)
##
b = set(a)

m = None
q = 0

for it in b:
    qt = a.count(it)
    if qt > q:
        q = qt
        m = it

print(m)

