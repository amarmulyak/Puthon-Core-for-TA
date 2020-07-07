# Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence
# n - length of Fibonacci sequence.
# NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements
# --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
# EXAMPLE OF Inputs/Ouputs when using this function:
#
# >>> print fibo(6)
# [1, 1, 2, 3, 5, 8]

def fibo(n):
    """
    Returns array with elements of Fibonacci sequence
    :param n: length of Fibonacci sequence
    :return: Fibonacci sequence
    """
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f


n = int(input("Please enter number: "))
print(fibo(n))
