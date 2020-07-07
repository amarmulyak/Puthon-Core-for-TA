"""
Provide full program code of fibo_element(n) function which returns element of Fibonacci sequence which index has a value equal n.
n - index of element of Fibonacci sequence.
NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....
EXAMPLE OF Inputs/Ouputs when using this function:
```
print fibo_element(6)
8
```
"""
i = 0
while i <= 0:
    i = int(input("Provide a number: "))


def fib_element(n):
    a, b = 1, 1
    c = a
    for n in range(2, n):
        c = a + b
        a = b
        b = c
    print(c)


fib_element(i)
