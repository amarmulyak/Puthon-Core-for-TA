# class A:
#     pass
#
# class A():
#     pass
#
# class A(object): #for python 2
#     pass

# class Class:
#     """
#     is class
#     """
#     name = ""
#     size = 0
#
#
#     def print(self):
#         print(f"name:{self.name} size:{self.size}")
#
#
# c = Class()
# c.print()
# c.name = "r9111"
# c.size = 10
# c.print()
# print(c.name)
# print(c)
# print(c.print)
# print(c.__dir__())
# c.f = 10
# print(c.__dir__())
# def my_print(self):
#     print(f"name:{self.name} size:{self.size} f:{self.f}")
#
# Class.m = my_print
# c.m()
#
# def my_print(r, str):
#     print(f"name:{r.name} size:{r.size} f:{r.f} {str}")
# Class.m = my_print
# c.m("DDDDDD")
# my_print(c, "DDDDDD")


# class Class:
#     """
#     is class
#     """
#
#     def __init__(self, name, size=10):
#         self._name = name
#         self._size = size
#
#
#     def print(self):
#         print(f"name:{self._name} size:{self._size}")
#
#
# c1 = Class("r111")
# c2 = Class("r112", 5)
# print(c1)
# print(c2)
# c1.print()
# c2.print()


# class A:
#     cm = []
#     ci = "ci"
#
#     def __init__(self):
#         self.im = []
#         self.ii = "ii"
#
#     def __str__(self):
#         return f"cm:{self.cm} ci:{self.ci} im:{self.im} ii:{self.ii}"
#
#     def __repr__(self):
#         return f"({self.cm}, {self.ci}, {self.im}, {self.ii})"
#
#     def __del__(self):
#         print("del ", self)
#     def __eq__(self, other):
#         if isinstance(other, str):
#             return self.ii == other
#         return self.im == other.im and self.ii == other.ii
# a1 = A()
# print("a1", a1.cm, a1.ci, a1.im, a1.ii)
# a2 = A()
# a2.cm.append(11)
# a2.ci = "new ci"
# a2.im.append(99)
# a2.ii = 22
# print("a1", a1.cm, a1.ci, a1.im, a1.ii)
# print("a2", a2.cm, a2.ci, a2.im, a2.ii)
# print(a1)
# print(a2)
# print([a1, a2])
# # print(A.cm)
# # # print(A.ii)
# # print(dir(A))
# # print(dir(a1))
# # print(A.__dict__)
# # print(a1.__dict__)
# # print(a2.__dict__)
# # print(A.__mro__)
# # del a2
# a3 = A()
# a4 = A()
# print(a3)
# print(a4)
# print(a3 == a4)
# print(a2)
# print(a2 == a4)
# a2.ii = "ii"
# print(a2 == "ii")


# class Singleton:
#     obj = None  # attribute for storing a single copy
#
#     def __new__(cls, *dt, **mp):  # class Singleton.
#         print(type(cls))
#         if cls.obj is None:
#             # If it does not yet exist, then
#             # call __new__ of the parent class
#             cls.obj = object.__new__(cls, *dt, **mp)
#             # cls.obj = {1,2}
#             cls.obj.a = {1,2,3}
#             print("obj:", cls.obj)
#         return cls.obj  # will return Singleton
#     def __init__(self):
#
#         print("__init__", type(self), self.__dict__)
# s1 = Singleton()
# s2 = Singleton()
# print(id(s1), id(s2))