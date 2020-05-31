from random import random

"""
Генерується квадратна матриця. Знайти сума елементів її головнї та побічної
діагоналей. Головна діагональ йде з верхнього лівого кута в правий нижній,
побічна - з верхнього правого кута в лівий нижній.

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
"""

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
for i in range(N):
    main_diagonal_sum += matrix[i][i]
    # print(matrix[i][i])  # To print elements of main diagonal
# print(main_diagonal_sum)  # To print sum of elements in the main diagonal

side_diagonal_sum = 0
count = N - 1
for i in range(0, N, 1):
    for j in range(count, 0 - 1, -1):
        count -= 1
        side_diagonal_sum += matrix[i][j]
        # print(matrix[i][j])  # To print elements of side diagonal
        break
# print(side_diagonal_sum)  # To print sum of elements in the side diagonal

total_sum = main_diagonal_sum + side_diagonal_sum
print(f"Total sum of elements of main and side diagonals is: {total_sum}")
