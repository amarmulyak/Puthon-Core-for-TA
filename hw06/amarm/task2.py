"""
Provide full program code of fibo_element(n) function which returns element
of Fibonacci sequence which index has a value equal n.

n - index of element of Fibonacci sequence.

NOTE: The Fibonacci sequence it's a sequence where some element it's a sum
of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....

EXAMPLE OF Inputs/Ouputs when using this function:

print fibo_element(6)
8
```
"""


def fibo_element(n):
    """This function returns n-element from the Fibonacci list"""
    a = 0
    b = 1
    fibonacci_list = [a, b]
    for i in range(n):
        a, b = b, a + b
        fibonacci_list.append(b)
    print(fibonacci_list[0:n])  # To see Fibonacci list uncomment this line
    if n <= 0:
        return f"'{n}'-element is not correct. Type number grater then 1!"
    else:
        return fibonacci_list[n-1]


print(fibo_element(7))
