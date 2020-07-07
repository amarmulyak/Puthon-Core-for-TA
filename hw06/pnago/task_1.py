"""Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence
n - length of Fibonacci sequence.
NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
EXAMPLE OF Inputs/Ouputs when using this function:
```
print fibo(6)
[1, 1, 2, 3, 5, 8]
```
"""
i = 0
while i <= 0:
    i = int(input("Provide a number: "))


def fib(n):
    a, b = 1, 1
    fib_arr = [a]
    if n > 1:
        fib_arr = [a, b]
    for n in range(2, n):
        c = a + b
        a = b
        b = c
        fib_arr.append(b)
    print(fib_arr)


fib(i)

