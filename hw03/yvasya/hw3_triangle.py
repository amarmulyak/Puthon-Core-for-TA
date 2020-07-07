import cmath

print("Please, enter values for triangle sides")
side_a = float(input("Side a: "))
side_b = float(input("Side b: "))
side_c = float(input("Side c: "))

thp  = (side_a + side_b + side_c) / 2 # triangle half perimeter

ts = cmath.sqrt(thp * (thp - side_a) * (thp - side_b) * (thp - side_c)) # triangle square

if side_a > 0 and side_b > 0 and side_c > 0:
    print("Perimeter of the triangle is: " + str(thp * 2) )
    print("Square of the triangle is: " + str(ts))
else:
    print("Impossible to build a triangle with provided values of the sides")
