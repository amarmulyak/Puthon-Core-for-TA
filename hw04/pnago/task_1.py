# •	Знайти всі чотирьохзначні числа, сума цифер яких рівна заданому числу.

# Задаємо число:
num = int(input("Provide a number:"))

for a in range(1, 9):
    for b in range(9):
        for c in range(9):
            for d in range(9):
                if a+b+c+d == num:
                    print(int(str(a)+str(b)+str(c)+str(d)))
