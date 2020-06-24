a = 0.1
b = 0.8
h = 0.1

x = 0.5

import math
while x <=b:
    si = 1
    s = 0
    n = 1
    while si > 10 ** (-5):
        si = n*(n+2)*(x**n)
        #print(si)
        s+=si
        n+=1
    y = (x*(3-x))/((1-x)**3)
    p = math.fabs((s-y)/y)*100
    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x+=h



