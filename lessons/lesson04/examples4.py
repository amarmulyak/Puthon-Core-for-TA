# # print("-" * 17)
# # for i in range(10):
# #
# #     print(f"|\t{i}\t|\t{i*2}\t| ")
# #     print("-"*17)
#
# a = 1
# b = 3
# h = 1
# #
# x = a
# # r = int((b-a)/h )
# # for x in range(r):
# #     x+=h
#
# import math
# while x <=b:
#     si = 1
#     s = 0
#     k = 1
#     while si > 10 ** (-5):
#         si = k * (k + 1) * (x ** k)
#         print(si)
#         s+=si
#         k+=1
#     y = 2*x/((1-x)**3)
#     p = math.fabs((s-y)/y)*100
#     print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
#     x+=h
#

# start = 0
# finish = 10
# while start < finish:
#     print(start)
#     start += 1
# else:
#     print ("The end")
# l = [1,2,3]
#
# while len(l)>0:
#     print(l)
#     l.pop()
# l = [1,2,3]
# while l:
#     print(l)
#     l.pop()
# l = "[1,2,3]"
# while l:
#     print(l)
#     l = l[:-1]
# l = 5
# while l:
#     print(l)
#     l -= 1
# else:
#     print(l)

# a = 0
# while a < 10:
#     b = 0
#     while b < 5:
#         print(a, b)
#         b += 1
#     a += 1
# print(b)

# a = "abc"
# for i in a:
#     print(i)
# for i in range(len(a)):
#     print(i, a[i])
# a = [1,2,3,4,5]
# for i in a:
#     print(i)
#     i **= i
#     print(i)
#     print(a)

# a = [[1, 2], 2, 3, 4, 5]
# for i in a:
#     print(i)
#     if (isinstance(i, list)):
#         i.append("bvdj")
#     print(a)

# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)
#     if i == 4:
#         a.insert(2, 9)
#     print(a)
# a = [i for i in range(10)]
# print(a)
# a = [i for i in range(10, 30)]
# print(a)
# a = [i for i in range(10, 30, 5)]
# print(a)
# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(i)
# n = 3
# for i in range(n):
#     print(f"n:{n}")
#     n += 1
#     print(f"n:{n}")
#     print(f"i:{i}")

# for i in range(10):
#     print(f"{i}")
#     if i % 2:
#         continue
#     print(f"i:{i}")
# else:
#     print("end")
#
# i=0
# while i < 10:
#     print(f"{i}")
#     i+=1
#     if i % 2:
#         continue
#     print(f"i:{i}")
# else:
#     print("end")

# for i in range(10):
#     print(f"{i}")
#     if i % 2:
#         break
#     print(f"i:{i}")
# else:
#     print("end_for")
# print("===========")
# i = 0
# while i < 10:
#     print(f"{i}")
#     i += 1
#     if i % 2:
#         break
#     print(f"i:{i}")
# else:
#     print("end")
#
# for i in range(5):
#     for j in range(i, i+5):
#         print(f"{i}-{j}")
#         if j%3:
#             break
#     if True:
#         break
#
# for i in range(3):
#     #ToDo
#     "dfsd"
#
# 5!
# 1*2*3*4*5


##### ==3==

# for n in range(1, 6):
#     print(f"{n * (n + 2)}x^{n}")
#
# x = 0.4
# S = 0
# s = 1
# n = 1
# while s > 10 ** (-5):
#     s = n * (n + 2) * (x ** n)
#     n += 1
#     S += s
#     print(f"S:{S} s:{s}")
# print(f"y={(x*(3-x))/((1-x)**3)}")


import math

a = 0.1
b = 0.55
h = 0.05
e = 10**(-5)
print(a, b, h, e)
x = a
while x <= b:
    S = 1
    s = 1
    k = 0
    # print(x)
    while s > e:
        # print(x)
        s=(3+2*k)*(x**(k+1))
        S+=s
        k += 1
    y = (1+x)/((1-x)**2)
    p = abs((S-y)/y)*100
    print(f"\t{x:.2f}\t{S:.3f}\t{y:.3f}\t{p:.3f}")
    x += h
