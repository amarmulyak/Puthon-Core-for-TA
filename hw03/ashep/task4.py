from math import sqrt

a = int(input("Enter number for side a "))
b = int(input("Enter number for side b "))
c = int(input("Enter number for side c "))

if a > 0 and b > 0 and c > 0:
    p = (a + b + c) / 2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    print("area is {}, square is {}".format(p, s))

else:
    print("it is not possible to build a triangle")
