import math
print("Задано 3 довільні числа a, b and c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
triangle = True if (a + b > c or a + c > b or b + c > a) or (
        (a ** 2 + b ** 2) == c ** 2 or (b ** 2 + c ** 2) == a ** 2 or (c ** 2 + a ** 2) == b ** 2) or (
        a + b > c or a + c > b or b + c > a) else False
if triangle is True:
    p = a + b + c
    pp = p / 2
    s = math.sqrt(pp * (pp - a) * (pp - b) * (pp - c))
    print(f"периметр трикутника = {p}, а площа = {s}")
else:
    print("This is not triangle")
