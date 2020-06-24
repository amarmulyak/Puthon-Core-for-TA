# Записати в стрічку філософію Пайтона
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
# Вивести весь текст у верхньому регістрі (всі великі літери)
# Замінити всі входження символу “і” на “&”

# Задано чотирицифрове натуральне число.
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число

# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

n_str = input('Input 4-digit number' + '\n')
n_int = int(n_str)
mult = 1
if n_int>9999 or n_int<1000 :
    print ('Incorrect number')
else :
    n_str = list(n_str)
    for i in n_str:
        i = int(i)
        mult *= i
    print('Product of numbers is', mult)
    n_str = n_str[::-1]
    print('Reversed number is %s' % ''.join(n_str))
    n_str.sort()
    print('Sorted number is %s' % ''.join(n_str))
