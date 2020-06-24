# Задано чотирицифрове натуральне число.
# Знайти добуток цифр цього числа.
# Записати число в реверсному порядку.
# Посортувати цифри, що входять в дане число

input = (input(("Please enter four-digit natural number.:\n")))

if len(input) == 4 and input.isnumeric():
    result = int(input[0]) * int(input[1]) * int(input[2]) * int(input[3])
    reversed = input[::-1]
    sorted = sorted(input)

    print('multiply:', result)
    print('reversed', reversed)
    print('sorted:', sorted)
else:
    print('Your input was wrong, please try again')
