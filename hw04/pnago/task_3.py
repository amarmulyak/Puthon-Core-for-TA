# •	Задано ціле число N, вивести перші N чисел фібоначі.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711 ...

N = int(input("Provide the N:"))
a = 0
b = 1
if N < 0:
    print("Incorrect input")
# First Fibonacci number is 0
elif N == 1:
    print(a)
# Second Fibonacci number is 1
elif N == 2:
    print(b)
else:
    for i in range(2, N):
        c = a + b
        a = b
        b = c
    print(b)
