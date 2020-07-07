# Provide full program code of fibo_element(n) function which returns element of Fibonacci sequence which index has a value equal n.
# n - index of element of Fibonacci sequence.
# NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements
# --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....
# EXAMPLE OF Inputs/Ouputs when using this function:
#
# >>> print fibo_element(6)
# 8

def fibo_element(n):
    """
    Returns element of Fibonacci sequence
    :param n: index of element of Fibonacci sequence
    :return: index has a value equal n
    """
    f = ()
    if n < 0:
        print("Incorrect number")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_element(n-1) + fibo_element(n-2)


n = int(input("Please enter number: "))
print(fibo_element(n))
