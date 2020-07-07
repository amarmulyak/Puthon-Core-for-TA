"""
Provide full program code of fibo_element(n) function which returns element of Fibonacci sequence
which index has a value equal n.
n - index of element of Fibonacci sequence.
NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two
previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....
EXAMPLE OF Inputs/Ouputs when using this function:
print fibo_element(6)
8
"""
def fibo_element(n):

    sequence = fib_sequence(n, [], 0, 1)
    print(sequence)
    return sequence[n - 1]

def fib_sequence(n, sequence, prevel, nextel):
    if len(sequence) > n - 1:
        return sequence
    elif not sequence:
        prevel = 1
        sequence.append(prevel)
    else:
        sequence.append(nextel)
        sumelem = prevel + nextel
        return fib_sequence(n, sequence, nextel, sumelem)
    return fib_sequence(n, sequence, prevel, nextel)

print(fibo_element(6))
