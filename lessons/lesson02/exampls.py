# a = 9999**9999
# print(a)
# print(len(str(a)))
# a = a+1

# x = 'foo'
# y = x
# print(x, id(x))  # foo
# print(y, id(y))  # foo
# y += 'bar'
# print(x, id(x))  # foo
# print(y, id(y))  # foo

# x = [1, 2, 3]
# y = x
# print(x, id(x))
# print(y, id(y))
# y += [3, 2, 1]
# print(x, id(x))
# print(y, id(y))


# a=1
# print(type(a))
# a=int()
# print(type(a))
# a = int("34")
# print(a)  # a = 34
# a = int("10", 36)  # a = 4
# print(a)
# a = int(6.7)  # a = 6
# b = int("0xfe76214", 16)  # long  b=266822164L
# b = int("70", 8)  # b=56
# b = float("3")  # b = 3.0
# c = eval("3, 5, 6")  # c = (3,5,6)
# c = eval("3 + 5 + 6")  # c = 14
# print(c)
# c = eval("print('FOO')")  # c = 14
# print(c)
# x = 1
# print(chr(x))
# for i in range(256):
#     print(i, chr(i))
# x = "a"
# print(ord(x))
# print(hex(10))
#
# print(type(x))
# print(type([]))

# st = 'abc'
# print(st, st[1])
# st = "foo" \
#      "boo"
# print(st)
# st = """foo
#  fvbbjdf
#   'fvbjdfj'
#    fbvjdf
#      boo"""
# print(st)

# name = "John"
# print("Hello, " + name + "!")
#
# print("Hello, %s!" % name)
#
# name = "John"
# age = 23
# print("%s is %d years old." % (name, age))
# print("%s is %s years old." % (name, age))
#
# name = "John"
# age = 23
# salary = 999.99
# print("%s is %d years old. Your sallary is %.6f $ %.1f $" % (name, age, salary, salary))
#
# default_order = "{}, {} and {}".format('John', 'Bill', 'Sean')
# print(default_order)
# # order using positional argument
# positional_order = "{1}, {0} and {2}".format('John', 'Bill', 'Sean')
# # order using keyword argument
# keyword_order = "{s}, {b} and {j}".format(j='John', b='Bill', s='Sean')

# str = 'programiz'
# print('str = ', str)
#
# #first character
# print('str[0] = ', str[0])
#
# #last character
# print('str[-1] = ', str[-1])
#
# #slicing 2nd to 5th character
# print('str[1:5] = ', str[1:5])
#
# #slicing 6th to 2nd last character
# print('str[5:-2] = ', str[5:-2])
#
# #slicing 6th to 2nd last character
# print('str[5:-2] = ', str[:3])
# print('str[5:-2] = ', str[1:])
# print('str[:] = ', str[:])
# print('str[::2] = ', str[::2])
# print('str[::2] = ', str[::3])
# print('str[::2] = ', str[::-1])
a = list()
print([i for i in dir(a) if not i[0] == "_"])
a = tuple()
print([i for i in dir(a) if not i[0] == "_"])

a = "tuple()"
print([i for i in dir(a) if not i[0] == "_"])

print("This will split all words into alist".split('al'))
print("--:--".join(["all", "ffff", "sdfsd"]))
print("This will split all wiords into alist".find("wi"))
print("This will split all wiords into alist".find("wi", 6))
print("This will split all wiords into alist".find("wiwww"))
print("This will split all wiords into alist".replace("wi", "WI"))

# import math
#
# print(math.floor(-87.15))  # -88
# print(math.floor(65.11))  # 65
# print(math.floor(69.86))  # 69
# print(math.floor(math.pi))  # 3


