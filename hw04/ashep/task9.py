a = 0.1
b = 0.55
h = 0.05

x = 0.5

import math
while x <=b:
    si = 1
    s = 1
    n = 0
    while si > 10 ** (-5):
        si = (3+2*n)*(x**(n+1))
        #print(si)
        s+=si
        n+=1
    y = (1+x)/((1-x)**2)
    p = math.fabs((s-y)/y)*100
    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x+=h