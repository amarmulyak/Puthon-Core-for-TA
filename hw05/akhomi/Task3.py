# Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []
for number in listOrigin:
    if number < 0:
        number = -1
        listMask.append(number)
    elif number > 1:
        number = 1
        listMask.append(number)
    elif number == 0:
        number = number
        listMask.append(number)
print(listMask)
