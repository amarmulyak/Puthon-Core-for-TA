# Знайти всі чотирьохзначні числа, сума цифер яких дорівнює заданому числу
# Задане число. перевірити чи дане число є простим
# Задано ціле число N, вивести перші N чисел Фібоначчі
# Знайти сумі кубів цифер аданого натурального числа

n_str = input('Input number' + '\n')
n_int = int(n_str)
sum = 0
if n_int < 1:
    print('Incorrect number')
else:
    # n_str = list(n_str)
    for i in n_str:
        i = int(i)
        sum += i ** 3
    print("Sum of number's digit's in cube is", sum)
