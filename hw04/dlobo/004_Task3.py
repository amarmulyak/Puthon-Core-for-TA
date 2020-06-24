# Знайти всі чотирьохзначні числа, сума цифер яких дорівнює заданому числу
# Задане число. перевірити чи дане число є простим
# Задано ціле число N, вивести перші N чисел Фібоначчі

n = int(input("Input number N" + "\n"))
f_list = [0, 1]
if n <= 0:
    print("Incorrect input")
elif n == 1:
    print("First Fibonacci number is", f_list[0])
elif n == 2:
    print("First two Fibonacci numbers are", f_list)
else:
    while len(f_list) < n:
        k = f_list[len(f_list) - 2] + f_list[len(f_list) - 1]
        # k = f_list[-2] + f_list[-1]
        f_list.append(k)
print("First", n, "Fibonacci numbers are", f_list)
