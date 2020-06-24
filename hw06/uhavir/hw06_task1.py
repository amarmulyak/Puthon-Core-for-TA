# Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence
# n - length of Fibonacci sequence.
# NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements
# --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
# EXAMPLE OF Inputs/Ouputs when using this function:
# ```
# >>> print fibo(6)
# [1, 1, 2, 3, 5, 8]
# ```


def fibonacci(n_terms):
    # check if the number of terms is valid
    n1 = 0
    n2 = 1
    # count = 0
    if n_terms <= 0:
        print("Please enter a positive integer")
    elif n_terms == 1:
        print("Fibonacci sequence upto", n_terms, ":")
        print(n1)
    else:
        l = []
        while len(l) < n_terms:
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            # count += 1
            l.append(n1)
        return l


print(fibonacci(6))
