def quad(a,b,c):
    d = (b*b-4*a*c)**.5
    if d == 0:
        x = (-b)/(2*a)
        print("x is {}".format(x))
    elif d > 0:
        x = ((-b)+d)/(2*a)
        print("x is {}".format(x))
    else:
        print("Don't have solution")
quad(1,9,6)
