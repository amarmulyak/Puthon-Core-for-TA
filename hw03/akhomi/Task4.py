a = int(input('The length of the  first side of the triangle: '))
b = int(input('The length of the  second side of the triangle: '))
c = int(input('The length of the  third side of the triangle: '))
P = a + b + c
p = int(P/2)
s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
if a + b <= c:
    print("It's not triangle")
elif b + c <= a:
    print("It's not triangle")
elif a + c <= b:
    print("It's not triangle")
else:
    print("Perimeter = " + str(P))
    print("Area = " + str(s))





