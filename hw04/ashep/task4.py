#Знайти суму кубів цифер заданого натурального числа.

n = int(input("Enter number "))
suma_x = 0

while n > 0:

    x = (n % 10)**3
    suma_x += x
    n //= 10

print(suma_x)
