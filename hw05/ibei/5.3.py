# Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []


for i in listOrigin:
    if i < 0:
        listMask.append(-1)
    elif i > 0:
        listMask.append(1)
    elif i ==0:
        listMask.append(i)

print(listMask)

