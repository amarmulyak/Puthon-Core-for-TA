# Дана матриця цілих чисел. Вводиться число. З'ясувати, які рядки і стовпці матриці містять дане число.
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

n = input("Enter number ")
n = int(n)

print("Rows (index):", end=" ")
for i in range(N):
    if n in matrix[i]:
        print(i, end=" ")
print()

print("Columns (index):", end=" ")
for j in range(M):
    for i in range(N):
        if matrix[i][j] == n:
            print(j, end=" ")
            break
print()