# Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.

listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
for n, i in enumerate(listOrigin):
    if i > 0:
        listOrigin[n] = 1
    elif i < 0:
        listOrigin[n] = -1
print(listOrigin)