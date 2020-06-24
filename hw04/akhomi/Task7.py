a = 1
b = 2
h = 0.1

x = 0.5

import math
while x <=b:
    si = 1
    s = 0
    k = 0
    while si > 10 ** (-5):
        si = (1/(math.factorial(k)*(k+2)))*(x**(k+2))
        #print(si)
        s+=si
        k+=1
    y = (x-1)*math.exp(x)+1
    p = math.fabs((s-y)/y)*100
    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x+=h