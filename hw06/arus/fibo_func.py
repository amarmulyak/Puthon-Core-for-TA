"""Provide full program code of fibo(n) function which returns array with elements of Fibonacci sequence

n - length of Fibonacci sequence.

NOTE: The Fibonacci sequence it's a sequence where some element it's a sum of two previous elements --> 1, 1, 2, 3, 5, 8, 13, 21, 34,...
"""


def fibo_func(n):
    i = 1
    i1 = 1
    list_value = 1
    fibo_list = [list_value]
    while n > len(fibo_list):
        fibo_list.append(list_value)
        i = i1
        i1 = list_value
        list_value = i + i1
    print(fibo_list)


n = int(input("Enter any value "))
print(fibo_func(n))
