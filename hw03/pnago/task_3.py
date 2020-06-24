import math
print("Find solution for the next equation: axˆ2 + bx + c = 0")
a = int(input("Enter the value for 'a':"))
b = int(input("Enter the value for 'b':"))
c = int(input("Enter the value for 'c':"))

D = b**2 - 4 * a * c
if a == 0:
    print("a - should not be equal to 0.")
elif c != 0 and b != 0:
    if D > 0:
        print("case1")
        print("x1:", (-b + math.sqrt(D))/(2*a))
        print("x2:", (-b - math.sqrt(D))/(2*a))
    elif D == 0:
        print("case2")
        print("x:", (-b) / (2 * a))
    else:
        print("case3")
        print("There are no real roots!")
else:
    if b == 0 and c == 0:
        print("case4")
        print("x:", 0)
    elif c == 0:
        print("case5")
        print("x1:", 0)
        print("x2:", (-b)/a)
    else:
        if -c/a > 0:
            print("case6")
            print("x1:", math.sqrt(-c/a))
            print("x2:", - math.sqrt(-c/a))
        else:
            print("It doesn't have any solution!")
