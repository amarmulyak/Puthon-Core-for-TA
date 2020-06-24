# # a = 2
# # try:
# #     b = 1
# #     a = 0/0
# # except EOFError:
# #     print("ERROR")
# # except ZeroDivisionError:
# #     print("/0")
# # else:
# #     print("good")
# #
# # print("safdxdfxa", b, a)
# #
# # y=1
# # try:
# #     print(y)
# # except:
# #     print("Something went wrong when your code execute")
# # finally:
# #     print("Program code finished")
# # Program to handle multiple errors with one except statement
#
# # try:
# #     a = 5
# #     if a < 4:
# #         b = a / (a - 3)  # throws ZeroDivisionError for a = 3
# #
# #     if a >= 4:
# #         print("Value of b = ", b)  # throws NameError
# #
# # # note that braces () are necessary here for multiple exceptions
# # except (ZeroDivisionError, NameError) as e:
# #     print("Error Occurred and Handled")
# #     print(e)
# # # except ZeroDivisionError:
# # #     print("Error Occurred and Handled ZeroDivisionError")
# # # except NameError:
# # #     print("Error Occurred and Handled NameError")
#
# #
# # class MyError(Exception):
# #     pass
# #
# #
# # def f():
# #     raise ZeroDivisionError("myError")
# #     raise MyError(" fbjdh h")
# #
# # import lessons.lesson07.pathEx.p1 as l
# # l.f()
# # f()
# # # try:
# # #     f()
# # # except ZeroDivisionError as e:
# # #     print("EEE", e)
# # # except MyError as e:
# # #     print(e)
#
#
# # try:
# #     0/0
# # except ArithmeticError as e:
# #     print("ArithmeticError", e)
# # except ZeroDivisionError as e:
# #     print("ZeroDivisionError", e)
# # except Exception as e:
# #     print("Exception", e)
#
#
# class MyZeroDivisionError(ZeroDivisionError):
#     def __init__(self, data):
#         self.data = data
#     def __str__(self):
#         return "MyZeroDivisionError: " + repr(self.data)
#
#
# def division(a, b):
#     if b == 0:
#         raise MyZeroDivisionError("b == 0")
#     return a/b
#
# try:
#     division(3, 0)
# except MyZeroDivisionError as e:
#     print(e.__traceback__)

l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in l:
#     # print(i)
#     for j in i:
#         print(j.subj, end="\t")
#     print()
import copy

d = copy.deepcopy(l)

d[1][1] = "dsfsd"


# for i in l:
#     # print(i)
#     for j in i:
#         print(j, end="\t")
#     print()
# for i in d:
#     # print(i)
#     for j in i:
#         print(j, end="\t")
#     print()
#

# def __repr__(self):
#     st = ""
#     for i in range(len(self)):
#         for j in range(len(self[i])):
#
#             if self[i][j]:
#                 st += str(self[i][j]) + "\t"
#             else:
#                 st += "empty" + "\t"
#         st += "\n"
#     return st
# print(__repr__(d))


class A:
    def __repr__(self):
        return [1, 2, 3]

    def __str__(self):
        return "A"


a = A()
b = A()
c = a, b
print(a)
print(a.__repr__())
print(c)
