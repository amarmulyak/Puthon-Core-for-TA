# # import requests
# # import pprint
# # API_KEY = '0750a6488847b8d2571c04d4333f3a98'
# # city = 'lviv'
# # url = f"https://samples.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
# # response = requests.get(url)
# # pprint.pprint(response.json())
# import lessons.lesson07.test1.m1 as t
# import sys
# from pprint import pprint
# sys.path.append('D:\\github\\pythonCore07052020')
# pprint(sys.path)
#
#
# from lessons.lesson07.test1.m1 import (t1 as T,
#                                        test,
#                                        sum as my_sum,
#                                        t2)
#
# t1 = 20
# print(T, t1)
# test()
# print(__name__)
#
# print(sum([1, 2, 3, 4, 5]))
# print(my_sum(1, 2))
# print(t2)
# print(dir())
# import pathEx.p1
# from pathEx.p2 import Variable, l
#
# print(pathEx.p1.Variable, Variable)
# print(pathEx.p1.l, l)
#
# Variable = 88
# l.append("a")
# pathEx.p1.Variable = 99
# pathEx.p1.l.append("b")
# print("="*10)
# print(pathEx.p1.Variable, Variable)
# print(pathEx.p1.l, l)
#
# import pathEx.p1
# from pathEx.p2 import Variable, l
# print("="*10)
# print(pathEx.p1.Variable, Variable)
# print(pathEx.p1.l, l)
#
# def pr():
#     from pathEx.p2 import TEXT
#     print("hfdjgdf",TEXT)
# pr()
# print(TEXT)
# from pathEx.p1 import *
# import pathEx.p2

# if __name__ == '__main__':
#     print(">>> ", "RUN")
# print(dir())
# from all import _a, __a, a
# print(dir())
# print(a)
# print(_a)
# print(__a)

# print(dir())
# from all import *
# print(dir())
import all
from all import _a
# print(all.a, _a)
# other.my_print()
all.a = 100
_a = 200
# print(all.a, _a)
import other
other.my_print()
all.a = 300
import all
from all import _a
# print(all.a, _a)
other.my_print()

