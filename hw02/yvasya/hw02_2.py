# Задано чотирицифрове натуральне число.

real_num = input("Enter 4-digit real number: ")

# Знайти добуток цифр цього числа.

real_num_mult = int(real_num[0]) * int(real_num[1]) * int(real_num[2]) * int(real_num[3])
print("The multiplication result is: " + str(real_num_mult))
print("")

# Записати число в реверсному порядку.

real_num_rev = real_num[::-1]
print("The reversed number is: " + real_num_rev )
print("")

# Посортувати цифри, що входять в дане число
real_num_sort = sorted(real_num)
print("Descending order: " + str(real_num_sort))