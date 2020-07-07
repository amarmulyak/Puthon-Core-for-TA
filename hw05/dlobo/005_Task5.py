# 1. Генерується список випадкових цілих чисел. Визначається, скільки в ньому парних чисел, а скільки непарних.
# 2. Вихідний список містить позитивні і негативні числа. Потрібно позитивні помістити в один список, а негативні - в інший.
# 3. Дан список цілих чисел. Замінити негативні на -1, позитивні - на число 1, нуль залишити без змін.
# 4. Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації. Програма будує список слів, знаки пунктуації виключаються.
#    Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації, за винятком відкриває дужки (пробіл перед нею).
# 5. Дана матриця. Знайти в ній рядок з максимальною сумою елементів, а також стовпець.
from random import random
matrix = []
tr_matrix = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)
for row in matrix:
    print(row)
row_sum = [sum([row[i] for i in range(len(matrix))]) for row in matrix]
print("Max row value is ", max(row_sum), "in row", row_sum.index(max(row_sum))+1 )
col_sum = [sum([row[i] for row in matrix]) for i in range(len(matrix))]
print("Max value", max(col_sum), "in column", col_sum.index(max(col_sum))+1)
