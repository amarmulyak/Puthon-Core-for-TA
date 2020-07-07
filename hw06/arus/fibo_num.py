"""Provide full program code of fibo_element(n) function which returns element
of Fibonacci sequence which index has a value equal n.

n - index of element of Fibonacci sequence."""


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
    print(fibo_list[-1])


n = int(input("Enter any value "))
print(fibo_func(n))
