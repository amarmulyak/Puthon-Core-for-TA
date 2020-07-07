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
number = int(input("Number: "))
for i in matrix:
    if number in i:
        print(i)