# Дана матриця. Знайти в ній рядок з максимальною сумою елементів, а також стовпець.

from random import random

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

# sum of the row
biggest_row = []
for row in matrix:
    row_sum = 0
    for i in range(len(row)):
        row_sum += row[i]
    biggest_row.append(row_sum)

print("The sum of the rows is as following: ", biggest_row)
print("")

biggest_row = max(biggest_row)

print("The maximum sum of the rows is: ", biggest_row)
print("")

# sum of the column
biggest_col = []

for column in range(len(matrix[0])):
    col_sum = 0
    for row in matrix:
        col_sum += row[column]
    biggest_col.append(col_sum)

print("The sum of the columns is as following: ", biggest_col)
print("")

biggest_col = max(biggest_col)

print("The maximum sum of the column is: ", biggest_col)
