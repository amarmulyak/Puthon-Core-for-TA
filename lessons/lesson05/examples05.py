# # l = [1, 2, "dhsfbjs", 2.2, lambda a: a * a]
# # print(l)
# # l = []
# # print(l)
# # l = list()
# # print(l)
# # l = list("abc")
# # print(l)
# # l = list(1) #error
# # print(l)
#
# print([i for i in dir(list) if i[0] != "_"])
# a = [1, 2]
# b = [3, 4]
# b.append(a)
# print(a)
# print(b)
# a = [5, 6]
# print(a)
# print(b)
# b = [3, 4, a]
# a.append(9)
#
# print(a)
# print(b)
# d = b.copy()
# print(id(b), id(d))
# print(b, d)
# a.append("a")
# print(b, d)
# print(all([1, [1, 2], True, []]))
# print(len(a))
# print(a.__len__())
# print(max([1, 2, 100]))
# a = [2,5,1,6,2,7]
# d = sorted(a)
# print(a, d)
# a.sort()
# print(a, a.sort())
# print(sum([1,2,3,4]))
# print(sum(["1","2","3","4"]))

#
# x = ['apple', 'banana', 'cherry']
# y = enumerate(x)
# print(list(y))
#
# for i in x:
#     print(i)
# for i in range(len(x)):
#     print(i, x[i])
#
# for i, v in enumerate(x):
#     print(i, v)
# for k in enumerate(x):
#     print(k)
#     i = k[0]
#     v = k[1]
#     print(i, v)

# print([i for i in range(10)])
# print([i for i in range(10) if i % 2])
# print([(i, j) for i in range(10) for j in range(i)])
# print([i**j for i in range(10) for j in range(i)])
# l = tuple()
# print(l)
# l = tuple("dhfbjs")
# print(l)
# l = ()
# print(l)
# l = (1, )
# print(l)
# print([i for i in dir(l) if i[0] != "_"])
# print(l.index(1))
# # print(l.index(99))
# print(99 in l)
# s = "vfdhv dfj" + \
#     "vbd " +\
#     "dgdf"
# print(s)
# s = ("vfdhv dfj"
#     "vbd "
#     "dgdf")
# print(s)
#
# d = {}
# print(d)
# d = dict()
# print(d)
# d = dict([(1, 2),
#           (2, 2),
#           (3, 2),
#           ("1", 9)])
# print(d)
# print([i for i in dir(dict) if i[0] != "_"])
# print(d[1])
# print(d["1"])
# print(d.get("1"), d.get(1, "N"))
# print(d.get("vdhvgf"))
# print(d.get("vdhvgf", "N"))
# print(d["vdhvgf"]) #error
# print(d.items())
# for key in d:
#     print(key, d[key])
# for key, value in d.items():
#     print(key, value)
# print(d.keys())
# print(d.values())
# l = [1,2,3,4,5]
# print(l.pop())
# print(l.pop(2))
# print(l)
# d.pop('1')
# print(d)
# d.update({"1":99})
# print(d)
# print({i:i**i for i in range(10)})
# print((i for i in range(10)))
# s = set()
# print(s)
# s = {}# not set, is dict
# print(s)
# s = {1,2,3,4,5,6,1,2,3,4,5}# not set, is dict
# print(s)
#
# print([i for i in dir(set) if i[0] != "_"])
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 | s2)
print(s1 - s2)
print(s2 - s1)
print(s2 ^ s1)
print(s2 & s1)
