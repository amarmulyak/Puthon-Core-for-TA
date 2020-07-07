#Provide full program code of fibo_element(n) function which returns element
#  of Fibonacci sequence which index has a value equal n.
#n - index of element of Fibonacci sequence.
#NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements
# --> 1, 1, 2, 3, 5, 8, 13, 21, 34,....
#EXAMPLE OF Inputs/Ouputs when using this function:
#>>> print fibo_element(6)
#8

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
    print (list[n-1])

fibo(8)

