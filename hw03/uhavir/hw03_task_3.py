import math
print("ВВедіть коефіцієнти квадратного рівняння (ax ^ 2 + bx + c = 0): ")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    print("Рівняння лінійне")
    x = c / b
    print(f"Розвязок рівняння x = {x}")
else:
    # визначаємо дискримінант
    d = b ** 2 - 4 * a * c
    print(f"D = {d}")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Рівняння має два дійсних корені x1 = {x1} та x2 = {x2}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"Рівняння має 1 дійсний корінь x = {x}")
    else:
        print("Рівняння немає розв'язку")