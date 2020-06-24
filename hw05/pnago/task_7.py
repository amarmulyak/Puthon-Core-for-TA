# Дана матриця цілих чисел.
# Вводиться число.
# З'ясувати, які рядки і стовпці матриці містять дане число.
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

# My solution
numExists = False
position = []
num = int(input("Enter any int value:"))
for row in range(N):
    for column in range(M):
        if matrix[row][column] == num:
            numExists = True
            item = str(row + 1) + "\t" + str(column + 1)
            position.append(item)

if not numExists:
    print("Your number: %s is not in matrix." % num)
else:
    print("You can find your number: %s on the next positions:" % num)
    print("Row\tColumn")
    for item in position:
        print(item)

