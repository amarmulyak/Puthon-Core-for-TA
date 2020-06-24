# Задано чотирицифрове натуральне число.
num = 7854

# * Знайти добуток цифр цього числа.
toString = str(num)
n = 1

for i in toString:
    n *= int(i)
print(n)

# * Записати число в реверсному порядку.
print(toString[::-1])

# * Посортувати цифри, що входять в дане число
sortedString = ''.join(sorted(toString))
print(sortedString)
