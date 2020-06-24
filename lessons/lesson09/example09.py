# class Polygon:
#     name = "Poligon"
#     def __init__(self, no_of_sides):
#         print("init_Polygon")
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]
#
#     def inputSides(self):
#         self.sides = [float(input("Enter side " + str(i + 1) + " : ")) for i in range(self.n)]
#
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side", i + 1, "is", self.sides[i])
#
# # p = Polygon(4)
# # p.dispSides()
# # p.inputSides()
# # p.dispSides()
#
#
#
# class Triangle(Polygon):
#     name = "Triangle"
#
#     def __init__(self):
#         print("init_Triangle")
#         super().__init__(3)
#         self.name = "ins_Triangle"
#         self.x = 1
#         self._x = 2
#         self.__x = 3
#         # Polygon.__init__(self, 3)  # super().__init__(3)
#     def my_print(self):
#         print(f"{self.x} {self._x} {self.__x}")
#     def inputSides(self):
#         self.sides = [2, 3, 2]
#     def oldInputSides(self):
#         super().inputSides()
#
#     def findArea(self):
#         a, b, c = self.sides
#         s = (a + b + c) / 2
#         area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
#         print('The area of the triangle is %0.2f' % area)
#
#
#     @staticmethod
#     def print(sss):
#         print("obj, obj.__dict__", sss)
# t = Triangle()
# # t.inputSides()
# # t.oldInputSides()
# # print(t.__dict__)
# # t.findArea()
# #
# # print("====")
# # t2 = Polygon(3)
# # t2.inputSides()
# # print(t2.__dict__)
#
# # print(isinstance(t, Polygon))
# # print(isinstance(t, Triangle))
# # print(type(t))
# #
# # print(Polygon.__dict__)
# # print(Triangle.__dict__)
# # print(t.__dict__)
# # print(t.name)
# # print(t.__class__.name)
# # print(Triangle.__mro__)
#
# # t.print("A")
# # Triangle.print("B")
# # t.my_print()
# # print(t.x)
# # print(t._x)
# #
# # print(t._Triangle__x)


# class P:
#
#     def __init__(self, x):
#         self.__x = x
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     def __set_x(self, x):
#         print("__set_x")
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     def __repr__(self):
#         return f"{self.__x}"
#     x = property(__get_x, __set_x)
#
# p = P(8888)
# print(p)
# p.x = 99
# print(p.x)

#
# class Parent(object):
#     def isParOrPChild(self):
#         return True
#     def who(self):
#         return 'parent'
# class Child (Parent):
#     def who (self):
#         return 'child'
# x = Parent()
# Print(x.who(), x.isParOrPChild())
# x = Child()
# Print(x.who(), x.isParOrPChild())
#
# parent True
# child True


class Parent:
    def foo(self):
        return 'who'

class Parent2:
    def foo(self):
        return 'WHO!!!!'

x = Parent()
# print(x.foo("boo"))
print(x.foo())
print(type(x))
x.__class__ = Parent2

print(x.foo())
print(type(x))

