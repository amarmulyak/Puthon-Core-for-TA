# Задано ціле число N, вивести перші N чисел фібоначі

n = int(input('Enter number '))

def fibonacci(n):
    if n <= 2: return 1
    f1 = f2 = 1
    for i in range(2, n):
        fib = f1 + f2
        f1 = f2
        f2 = fib
    return fib

def fibonacci_sequence(n):
    L = [1, 1]
    for i in range(1, n - 1):
        L.append(L[i] + L[i - 1])
    return L  # return L[-1] если нужно вывести н-й элемент последовательности

print(fibonacci(n))
print(fibonacci_sequence(n))
