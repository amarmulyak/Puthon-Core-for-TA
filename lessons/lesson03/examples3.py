# a = True
# b = False
# x = 5
# y = 5
# print(x == y)
# print(x > y)
# print(x < y)
# print(x >= y)
# print(x <= y)
# print(b == a)
# print(b != a)

# x = 1
# y = 5
# z = 10
# print(x < y and y < z)
# print(x < y < z)
# print(True and True and False)
# print(True and True and 10 and [] and [1])
# print(True and True and 1 and [10] and [1])
# print(True or 1 or [10] or [1])
# print(False or 1 or [10] or [1])
# print(False or 0 or [10] or [1])
# print(False or 0 or [] or [1])
# print(False or 0 or [] or [])
# print(not "")
# print(not "1")
# print(not False and 1 or 6)
# print(((not False) and 0) or 6)
# not ^
# and *
# or +
# False^ *0 + 6

# score = 12
#
# if score > 8:
#     print("You have passed the exam")
#     print("You have passed the exam")
#
# print("Exam was finished.")
# temperature = 31
#
# if temperature > 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
# print('Get some exercise outside.')

# age = 52
# if age < 12:
#     print('kid')
#     print('kid')
#     print('kid')
# elif age < 18: #12->17
#     print('teenager')
# elif age < 50:#18->49
#     print('adult')
# elif age <= 55:#50->55
#     print('adult 55')
# else:#56->
#     print('you are not old')

# l = []
# if len(l) > 0:
#     print("s")
# if l:
#     print("s")
# a = -10
# if a > 0:
#     x = "+"
# else:
#     x = "-"
# print(x)
# a = 10
# # x = a>0 ? "+" : "-"
# x = "+" if a > 0 else "-"
# print(x)
# print(1 in [1, 2, 3])
# print(1 in [2, 3])
# print("sd" in "asdf")
# s1 = "1234"
# s2 = "12"
# s2 += "34"
# print(id(s1), s1)
# print(id(s2), s2)
# print(s1 == s2)
# print(s1 is s2)

a = 8835
a1 = a // 1000
a2 = (a // 100) % 10
a3 = (a % 100) // 10
a4 = a % 10
print(a1, a2, a3, a4)
a = str(a)
a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])
print(a1, a2, a3, a4)
for i in a:
    print(int(i))

import this

print("="*10)
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

mystr = "".join([d.get(c, c) for c in this.s])

print(mystr)