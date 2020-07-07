"""
Provide full program code of fibo(n) function which returns array with
elements of Fibonacci sequence

n - length of Fibonacci sequence.

NOTE: The Fibonacci sequence it's a sequence where some element it's a
sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...

EXAMPLE OF Inputs/Ouputs when using this function:

print fibo(6)
[1, 1, 2, 3, 5, 8]

"""


def fibo(n):
    """This function returns n-first numbers from the Fibonacci list"""
    a = 0
    b = 1
    fibonacci_list = [a, b]
    for i in range(n):
        a, b = b, a + b
        fibonacci_list.append(b)
    return fibonacci_list[0:n]


print(fibo(10))
