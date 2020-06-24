# This program resolves quadratic equation ax^2 + bx + c = 0

import math

print("This program solves quadratic equation 'ax^2 + bx + c = 0'")
a = float(input("Type value for variable 'a': "))
b = float(input("Type value for variable 'b': "))
c = float(input("Type value for variable 'c': "))

D = b**2 - 4 * a * c  # Discriminant

if D > 0:
    print("Equation has 2 solutions:")
    x1 = round((-b - math.sqrt(D)) / (2 * a), 2)
    x2 = round((-b + math.sqrt(D)) / (2 * a), 2)

    try:
        x1 = round((-b - math.sqrt(D)) / (2 * a), 2)
        x2 = round((-b + math.sqrt(D)) / (2 * a), 2)
    except:
        print("a = 0")
        x1 = None
        x2 = None
        # x1 gets rounded value with 2 decimals
    print(f"x1 = {x1} \nx2 = {x2}")
elif D == 0:
    print("Equation has 1 solution:")
    x = round(-(b / (2 * a)), 2)
    print(f"x = {x}")
else:
    print("Equation doesn't have the solution")
