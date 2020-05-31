"""
Дана матриця цілих чисел. Вводиться число. З'ясувати, які рядки і стовпці
матриці містять дане число.

from random import random
N = 10
M = 15
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(random()*40)+10)
    matrix.append(row)

for row in matrix:
    print(row)

"""
numb = int(input("Type your number from 10 to 49: "))

from random import random
N = 10
M = 15
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(int(random()*40)+10)
    matrix.append(row)

for row in matrix:
    print(row)

row_number = 0
list_rows_with_numb = []
for row in matrix:
    row_number += 1
    if numb in row:
        list_rows_with_numb.append(row_number)
print(f"List of rows which contain '{numb}': {list_rows_with_numb}")

column_number = 0
list_columns_with_numb = []
for j in range(M):
    column_number += 1
    column_list = []
    for i in range(N):
        column_list.append(matrix[i][j])
    if numb in column_list:
        list_columns_with_numb.append(column_number)
print(f"List of columns which contain '{numb}': {list_columns_with_numb}")



