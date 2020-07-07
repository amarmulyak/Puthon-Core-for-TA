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

num_str = input("Enter an integer: ")
while not num_str.isnumeric():
    num_str = input("Enter an integer: ")
else:
    num = int(num_str)

position = [(column, row.index(num)) for column, row in enumerate(matrix) if num in row]
if position:
    print("Your number is found at the following rows and columns: ", position)
else:
    print('Number is not in matrix')
