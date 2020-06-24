# Генерується квадратна матриця.
# Знайти сума елементів її головнї та побічної діагоналей.
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

# My solution
x = 0
mainDia = 0
for i in matrix:
    mainDia += i[x]
    x += 1
print('Main diagonal:', mainDia)

x = len(matrix[0]) - 1
antiDia = 0
for i in matrix:
    antiDia += i[x]
    x -= 1
print('Antidiagonal:', antiDia)