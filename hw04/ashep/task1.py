# Знайти всі чотирьохзначні числа, сума цифер яких рівна заданому числу
n = int(input("Enter number "))

for x in range(1000,10000):
    digits = [int(x) for x in list(str(x))]
    suma = sum(digits)

    results = []
    if suma == n:
        print("Sum of number {} is {}".format(x, n))
        results.append(x)
