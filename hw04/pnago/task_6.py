# З точністью до e = 10ˆ(-5) обчислити наближене значення S для значень аргумента x=a(h)b
# та порівняти з точним значенням y
# Результати оформити у таблиці:
import math
# 1)
print("> #1")
a = 0.1
b = 0.8
h = 0.01

x = a
print(f"|\t\t\tx\t\t\t|\t\t\ts\t\t\t|\t\t\ty\t\t\t|\t\t\tpohybka\t\t\t|")
while x <= b:
    si = 1
    s = 0
    k = 1
    while si > 10 ** (-5):
        si = k * (k + 1) * (x ** k)
        s += si
        k += 1
    y = 2*x/((1-x)**3)
    p = math.fabs((s-y)/y)*100

    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x += h

# 2)
print("> #2", "=" * 50)
a = 1
b = 2
h = 0.01

x = a
print(f"|\t\t\tx\t\t\t|\t\t\ts\t\t\t|\t\t\ty\t\t\t|\t\t\tpohybka\t\t\t|")
while x <= b:
    si = 1
    s = 0
    k = 0
    while si > 10 ** (-5):
        si = (1/(math.factorial(k) * (k+2)))*(x**(k+2))

        s += si
        k += 1
    y = (x-1)*math.exp(x)+1
    p = math.fabs((s-y)/y)*100

    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x += h

# 3)
print("> #3", "=" * 50)
a = 0.1
b = 0.8
h = 0.1

x = a
print(f"|\t\t\tx\t\t\t|\t\t\ts\t\t\t|\t\t\ty\t\t\t|\t\t\tpohybka\t\t\t|")
while x <= b:
    si = 1
    s = 0
    n = 1
    while si > 10 ** (-5):
        si = n*(n+2)*(x**n)
        s += si
        n += 1
    y = x*(3-x)/((1-x)**3)
    p = math.fabs((s-y)/y)*100

    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x += h

# 4)
print("> #4", "=" * 50)
a = 0.1
b = 0.55
h = 0.05

x = a
print(f"|\t\t\tx\t\t\t|\t\t\ts\t\t\t|\t\t\ty\t\t\t|\t\t\tpohybka\t\t\t|")
while x <= b:
    si = 1
    s = 1
    n = 0
    while si > 10 ** (-5):
        si = (3+2*n)*(x**(n+1))
        s += si
        n += 1
    y = (1+x)/((1-x)**2)
    p = math.fabs((s-y)/y)*100

    print(f"|\t{x}\t|\t{s}\t|\t{y}\t|\t{p}\t|")
    x += h
