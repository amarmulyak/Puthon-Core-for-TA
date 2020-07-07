# Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.

listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []

for i in range(len(listOrigin)):
    if listOrigin[i] > 0:
        listMask.append(listOrigin[i])
        listMask[i] = 1
    elif listOrigin[i] < 0:
        listMask.append(listOrigin[i])
        listMask[i] = -1
    else:
        listMask.append(listOrigin[i])

print("Original list: " + str(listOrigin))
print("Converted list: " + str(listMask))