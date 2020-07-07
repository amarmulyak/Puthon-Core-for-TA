"""Provide full program code of fibo(n) function which returns array with elements
of Fibonacci sequence
n - length of Fibonacci sequence.
NOTE: The Fibonacci sequence it's a sequence where some element
it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
EXAMPLE OF Inputs/Ouputs when using this function:"""


def fibo(n):

    l = [0, 1]
    if n < 0:
        print("Wrong number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        a = 0
        b = 1
        for i in range(0, n - 1):
            b = a + b
            a = b - a
            l.append(b)
        return l

print(fibo(6))
# [1, 1, 2, 3, 5, 8]
