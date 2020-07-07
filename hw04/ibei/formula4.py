import math
a = 0.1
b = 0.55
h = 0.05

x=a

for n in range (1, 6):
    print(f"{n * (n + 2)}x^{n}")

x = 0.4
S = 0
s = 1
n = 0

while s > 10 ** (-5):
    s = (3+2*n)*(x**n)
    n += 1
    S += s
    s1=s+1
    y = (1 + x) / (1 - x) ** 2
    p = math.fabs((s1 - y) / y) * 100
    print(f"|\t{x}\t|\t{s1}\t|\t{y}\t|\t{p}\t|")
    x+=h


