import math

print('''This program evaluates if the triangle can be
created from the 3 sides a, b and c provided by
you and finds its area
''')

a = float(input("Type value for side a: "))
b = float(input("Type value for side b: "))
c = float(input("Type value for side c: "))

triangle = False
msg_positive = "Triangle can be created from the sides provided by you"
msg_negative = "Triangle can not be created from the sides provided by you"

if a >= b and a >= c:  # side a is the biggest
    if a < b + c:
        print(msg_positive)
        triangle = True
    else:
        print(msg_negative)
elif b >= a and b >= c:  # side b is the biggest
    if b < a + c:
        print(msg_positive)
        triangle = True
    else:
        print(msg_negative)
else:  # side c is the biggest
    if c < a + b:
        print(msg_positive)
        triangle = True
    else:
        print(msg_negative)

if triangle:
    p = (a + b + c) / 2  # Half-perimeter
    # S gets rounded value with 2 decimals
    S = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    print(f'''Area:
S = {S}''')
