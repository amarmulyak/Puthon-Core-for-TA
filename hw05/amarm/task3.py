"""
Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.

listOrigin = [10, -15, 3, 8, 0, 9, -6, 13, -1, 5]
listMask = []
"""
print("Solution 1 creates a new list")
listOrigin = [10, -15, 3, 8, 10, 0, 9, -6, 13, -1, 5]
print(listOrigin)
listMask = []
for element in listOrigin:
    if element > 0:
        listMask.append(1)
    elif element < 0:
        listMask.append(-1)
    else:
        listMask.append(0)
print(listMask)

print("""
Solution 2 changes elements in the origin list""")
listOrigin = [10, -15, 3, 8, 10, 0, 9, -6, 13, -1, 5]
print(listOrigin)
for element in listOrigin:
    index_element = listOrigin.index(element)
    if element > 0:
        listOrigin.remove(element)
        listOrigin.insert(index_element, 1)
    elif element < 0:
        listOrigin.remove(element)
        listOrigin.insert(index_element, -1)
print(listOrigin)
