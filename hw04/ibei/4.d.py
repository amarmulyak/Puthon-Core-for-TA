# •	Знайти суму кубів цифер заданого натурального числа.

n = int(input("n: "))
sum = 0
for i in range(1, n + 1):
    sum += i * i * i
print (sum)

