import math

print("enter a b c for traingle sides :")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

p = ((a + b + c) / 2)
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print("Invalid size")
else:
    print("Perimetr:", p * 2)
    print("square: %.2f" % s)
