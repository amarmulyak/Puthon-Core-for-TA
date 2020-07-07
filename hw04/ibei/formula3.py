import math
a = 0.1
b = 0.8
h = 0.1

x=a

for n in range (1, 6):
    print(f"{n * (n + 2)}x^{n}")

x = 0.4
S = 0
s = 1
n = 1

while s > 10 ** (-5):
    s = n * (n + 2) * (x ** n)
    n += 1
    S += s
    y=(x*(3-x))/((1-x)**3)
    p = math.fabs((s - y) / y) * 100
    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x+=h






