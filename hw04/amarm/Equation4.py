import math

a = 0.1
b = 0.55
h = 0.05

x = a

while x <= b:
    si = 1
    s = 0
    n = 0
    while si > 10 ** (-5):
        si = (3 + 2 * n) * x**(n + 1)
        # print(si)
        s += si
        n += 1
    s_1 = 1 + s
    y = (1 + x) / (1 - x)**2
    p = math.fabs((s_1 - y) / y) * 100
    print(f"|\t{x}\t|\t{s_1}\t|\t{y}\t|\t{p}\t|")
    x += h
