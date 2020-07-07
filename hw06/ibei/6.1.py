#Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence

#n - length of Fibonacci sequence.

#NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...

#EXAMPLE OF Inputs/Ouputs when using this function:

#>>> print fibo(6)
#[1, 1, 2, 3, 5, 8]

def fibo(n):
    list = []
    n1 = 0
    n2 = 1
    count = 0
    while count < n:
        m = n1 + n2
        n1 = n2
        n2 = m
        count += 1
        list.append(n1)
    print (list)

fibo(12)

