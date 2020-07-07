#Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []
for n in listOrigin:
    if n<0:
        n_neg= -1
        listMask.append(n_neg)
    elif n>0:
        n_pos = +1
        listMask.append(n_pos)
    else:
        listMask.append(n)
print(listMask)



