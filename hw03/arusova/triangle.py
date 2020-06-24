from math import sqrt

a = int(input("Enter number "))
b = int(input("Enter number "))
c = int(input("Enter number "))
if a <= 0 or b <= 0 or c <= 0:
    print("Can't build a triangle")
elif a + b > c or a + c > b or b + c > a:
    perimeter = a + b + c
    p = (a+b+c)/2
    square = sqrt(p*(p-a)*(p-b)*(p-c))
    print(perimeter)
    print(square)
else:
    print("Can't build a triangle")