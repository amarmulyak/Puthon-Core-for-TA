"""
В даному списоку визначити значення яке(і) найбільше зустрічається.

from random import random

a = [int(random()*5) for i in range(15)]
print(a)
"""

from random import random

a = [int(random()*5) for i in range(15)]
print(a)

count_previous_element = 0
max_element = 0
for element in a:
    count_element = 0
    for compare_element in a:
        if compare_element == element:
            count_element += 1
    # print(f"{element}: {count_element}")
    if count_element > count_previous_element:
        max_element = count_element
        count_previous_element = count_element
# print(max_element)

often_elements = []
for element in a:
    count_element = 0
    for compare_element in a:
        if compare_element == element:
            count_element += 1
    if count_element == max_element and element not in often_elements:
        often_elements.append(element)
print(f"""The most resent element(s) in the list:
{often_elements}""")
