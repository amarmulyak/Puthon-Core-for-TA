# В даному списоку визначити значення яке(і) найбільше зустрічається.

from random import random
import operator

a = [int(random()*5) for i in range(15)]
print(a)
print("")

counter = {}
for i in a:

    if i in counter:
        counter[i] += 1
    else:
        counter[i] = 1

a_sorted = sorted(counter, key = counter.get, reverse = True)
top_elem = a_sorted[:3]
print("Three most frequent elements are: ", top_elem)
print("")

sorted_counter = sorted(counter.items(), key=operator.itemgetter(1), reverse=True)

print("The elements of the list and their frequency is as following: ", sorted_counter)
