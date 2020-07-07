# Дана матриця. Знайти в ній рядок з максимальною сумою елементів, а також стовпець.
from random import random

matrix = []
matrix_row = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)
    print(row)

for item in range(len(matrix)):
    x = sum(matrix[item])
    matrix_row.append(x)
print(max(matrix_row))

y = 0
column = 1
for row in range(len(matrix)):
    y += matrix[row][column]
print(y)