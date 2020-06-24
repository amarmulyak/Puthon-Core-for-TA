# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = int(input("Please enter natural number1:\n"))
b = int(input("Please enter natural number2:\n"))

a = a + b
b = a - b
a = a - b

print('number1', a)
print('number2', b)
