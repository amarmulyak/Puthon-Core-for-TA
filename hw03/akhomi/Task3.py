a = (float(input('a = ')))
b = (float(input('b = ')))
c = (float(input('c = ')))
d = b ** 2 - 4 * a * c
x = float()
if d == 0:
    x = (-b) / (2 * a)
    print(x)
elif d > 0:
    x = ((-b) + d ** 0.5) / 2 * a
    print(d)
elif d < 0:
    print("There are no solution for D")
else:
    print("No root")







