# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.

a = input("Enter the first value: ")
b = input("Enter the second value: ")

a, b = b, a

print(a, b)