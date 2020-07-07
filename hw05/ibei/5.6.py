#Генерується квадратна матриця. Знайти сума елементів її головнї та побічної діагоналей.
# Головна діагональ йде з верхнього лівого кута в правий нижній, побічна - з верхнього правого кута в лівий нижній.
from random import random
N = 5
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)
##
maxRow = 0
idRow = 0
i = 0
for row in matrix:
    if sum(row) > maxRow:
        maxRow = sum(row)
        idRow = i
    i += 1

print(idRow, '-', maxRow)

maxCol = 0
idCol = 0
for i in range(5):
    colSum = 0
    for j in range(5):
        colSum += matrix[j][i]
    if colSum > maxCol:
        maxCol = colSum
        idCol = i

print(idCol, '-', maxCol)

