print("This program prints n-first numbers from the Fibonacci list")
n = int(input("Type n: "))
a = 0
b = 1
fibonacci_list = [a, b]
for i in range(n):
    a, b = b, a + b
    fibonacci_list.append(b)
print(fibonacci_list[0:n])
