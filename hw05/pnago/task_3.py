# Дано список цілих чисел.
# Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.

listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []
for i in listOrigin:
    if i < 0:
        i = -1
        listMask.append(i)
    elif i > 0:
        i = 1
        listMask.append(i)
    else:
        listMask.append(i)
print(listMask)
# for i in range(len(listOrigin)):
#     if listOrigin[i] < 0:
#         listOrigin[i] = -1
#     elif listOrigin[i] > 0:
#         listOrigin[i] = 1
# print(listOrigin)
