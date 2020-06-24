# Дана матриця.
# Знайти в ній рядок з максимальною сумою елементів, а також стовпець.

from random import random

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(int(random()*10))
    matrix.append(row)

for row in matrix:
    print(row)

# My solution
# Find the grater row:
rowSum = [sum(row) for row in matrix]

# Find the grater column:
colSum = []
for x in range(len(matrix[0])):
    y = 0
    for i in matrix:
        y += i[x]
    colSum.append(y)
# Print answers:
print("The row with grater sum is:", rowSum.index(max(rowSum))+1)
print("The column with grater sum is:", colSum.index(max(colSum))+1)
