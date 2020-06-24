"""Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
"""
listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
list_new = []

for i in listOrigin:
    if i > 0:
        list_new.append(1)
    elif i < 0:
        list_new.append(-1)
    else:
        list_new.append(i)
#print(int_list)
print(list_new)