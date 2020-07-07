""" Provide full program code of fibo_element(n) function
which returns element of Fibonacci sequence which index
has a value equal n.
n - index of element of Fibonacci sequence.
NOTE: The Fibonacci sequence it's a sequence where some
element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....
EXAMPLE OF Inputs/Ouputs when using this function:"""


def fibo_element(n):
    if n < 0:
        print("Wrong number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fibo_element(n - 1) + fibo_element(n - 2)


print(fibo_element(6))
