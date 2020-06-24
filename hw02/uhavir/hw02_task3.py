# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
x = input("Type some value x: ")
y = input("Type some value y: ")
x, y = y, x
print("x =", x)
print("y =", y)
