# l = [1, 2, 3, 4]
# print(sum(l))
# s2 = sum
# def sum():
#     print("sum")
# print(sum())
# print(s2(l))
# sum = s2
# print(sum(l))


# def greet(name):
#     """This function greets to
#      the person passed in as
#      parameter"""
#     print("Hello, " + name + ". Good morning!")
#
#
# print("foo")
# a = greet("Andrii")
# print("p:", greet("Anna"))
# print(a)
#
#
# def greet(name):
#     """This function greets to
#      the person passed in as
#      parameter"""
#     return "Hello, " + name + ". Good morning!"
# print("boo")
# a = greet("Andrii")
# print("p:", greet("Anna"))
# print(a)
#
# print(dir(greet))
# print(greet.__doc__)

# sum()
# def foo(a, b):
#     """
#     calculate a+b
#     :param a: type int
#     :param b: type int
#     :return:
#     """
#     return a+b

# def my_sum(arg1, arg2):
#     total = arg1 + arg2
#     print("Inside the function : ", total)
#     return total
#     print("After operator the return ")
#
# print("sum: ", my_sum(1,2))

# arg1 = 3
#
# def foo(a):
#     return a ** a
# print(foo(arg1))


# def my_pow(x, y):
#     return x**y
# print(my_pow(2, 10))
# print(my_pow(y=10, x=2))


# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)
#
# print_info("Alex")
# print("-" * 10)
# print_info("Ogi", 25)
# print("-" * 10)
# print_info(name="Ogi", age=25)
# print("-" * 10)
# print_info(age=25, name="Ogi")

# def print_info(name, sex, age=18):
#     print("Name: ", name)
#     print("Age: ", age)
#     print("Sex: ", sex)
#
#
# print_info("Ogi", 25, "women")
# print_info(name="Ogi", sex=25, age=99 )
# print_info(name="Ogi", sex=25 )
#
# print_info(1,2,3,4)

# def print_numbers(arg, *var_tuple, arg2=1, **vars_dict):
#     print("arg: ", arg)
#     print("vartuple: ", var_tuple)
#     # for var in var_tuple:
#     #     print(var)
#     print("arg2: ", arg2)
#     print(vars_dict)

# print_numbers(1)
# print_numbers(1,2,3,4,5,6)
# print_numbers(1,2,3,4,arg2=5, arg3=4, arg5=6)
# print_numbers(1,2,3,4,arg4=5, arg3=4, arg5=6)
# d = {"arg": 1, "arg2":2, "a":3}
# l = (1,2,3,4,5,6)
# print_numbers(l)
# print_numbers(*l)
# print_numbers(d)
# print()
# print_numbers(*d)
# print()
# print_numbers(**d)
# print(dir())
# l = []
# a = 1
# def func(x):
#     # print(a)
#     global a
#     print(dir())
#     ll = l
#     # l.append("aa")
#     ll.append("aa")
#     a = 20
#     print(a)
#     print(dir())
#
# print(dir())
# func(1)
# print(dir())
# print(a)
# print(l)
# def foo(a=[]):
#     a.append(1)
#     print(a)
#
#
# foo()
# foo()
# foo([2, 3, 5])
# foo()

def fuc(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


print(fuc(5))


def rfuc(n):
    if n == 0:
        return 1
    print(f"{n}*f({n - 1})")
    return n * rfuc(n - 1)


# Rf(5)
# 5*rf(4)
# =>5*(4*rf(3))
# =>5*(4*(3*rf(2)))
# =>5*(4*(3*(2*rf(1))))
# =>5*(4*(3*(2*(1*rf(0)))))
# =>5*(4*(3*(2*(1*1))))
# import sys
# sys.setrecursionlimit(10000)
# print(rfuc(995))
print(dir())
f = lambda a, b: a + b;
print("aa")
print(f(1, 2))
print(f(4, 7))
