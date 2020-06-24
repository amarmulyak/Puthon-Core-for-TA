import math
print("Provide three edges of triangle")
a = float(input("Edge a:"))
b = float(input("Edge b:"))
c = float(input("Edge c:"))

if a < b + c and b < a + c and c < a + b:
    perimeter = a + b + c
    print("Perimeter:", perimeter)
    semiPerimeter = float(perimeter/2)
    area = math.sqrt(semiPerimeter*(semiPerimeter-a)*semiPerimeter*(semiPerimeter-b)*semiPerimeter*(semiPerimeter-c))
    print("Area: %.1f" % area)
else:
    print("It is not possible to compose a triangle!")
