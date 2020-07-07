"""
Генерується квадратна матриця. Знайти сума елементів її головнї та побічної діагоналей.
Головна діагональ йде з верхнього лівого кута в правий нижній, побічна - з верхнього правого кута в лівий нижній.
"""

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


main_diagonal_sum = 0
secondary_diagonal_sum = 0

for r in range(len(matrix)):
    for c in range(len(matrix[0])):
        if r == c:  # The row-column condition is row = column.
            main_diagonal_sum += matrix[r][c] #
        if r == len(matrix) - c - 1: # The row-column condition is row = numberOfRows – column -1.
            secondary_diagonal_sum += matrix[r][c]

print("The sum of elements in the principal diagonal is:" , main_diagonal_sum)
print("")
print("The sum of elements in the secondary diagonal is:" , secondary_diagonal_sum)
print("")

total_sum = main_diagonal_sum + secondary_diagonal_sum
print("The sum of primary and secondary diagonals is: ", total_sum)
