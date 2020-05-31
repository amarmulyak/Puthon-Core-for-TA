from random import random

"""
Дана матриця. Знайти в ній рядок з максимальною сумою елементів, а також стовпець.

from random import random

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)
"""

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

highest_row_sum = 0
for row in matrix:
    row_sum = 0
    for element in row:
        row_sum += element
    # print(row_sum)  # To print sum of each row uncomment this row
    if row_sum > highest_row_sum:
        highest_row_sum = row_sum
        highest_row = []
        for element in row:
            highest_row.append(element)

print(f"""
The row with the greatest sum of elements is:
{highest_row}""")

highest_column_sum = 0
for j in range(5):
    column_sum = 0
    for i in range(5):
        column_sum += matrix[i][j]
    # print(column_sum)  # To print sum of each column uncomment this row
    if column_sum > highest_column_sum:
        highest_column_sum = column_sum
        highest_column = []
        for i in range(5):
            highest_column.append(matrix[i][j])
print(f"""
The column with the greatest sum of elements is:
{highest_column}""")
