# •	Знайти суму кубів цифер заданого натурального числа.

n = 0
while n <= 0:
    n = int(input("Enter a natural number:"))
n_str = str(n)
i_sum = 0
for i in n_str:
    i_3 = int(i)**3
    i_sum += i_3
print(i_sum)
