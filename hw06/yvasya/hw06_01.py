"""
Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence
n - length of Fibonacci sequence.
NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two
previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
EXAMPLE OF Inputs/Ouputs when using this function:
print fibo(6)
[1, 1, 2, 3, 5, 8]
"""
fib_sequence = []
def fibo(n):
    elem1 = 1
    elem2 = elem1 + 0
    fib_sequence.append(elem1)
    fib_sequence.append(elem2)

    for i in range(n-2):
        elem_next = elem1 + elem2
        elem1, elem2 = elem2, elem_next
        fib_sequence.append(elem_next)
    return fib_sequence

print(fibo(6))
