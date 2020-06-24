import math

print("enter a b c for (ax^2 + bx + c = 0):")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

d = b ** 2 - 4 * a * c

print("D = %.2f" % d)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("no root")
