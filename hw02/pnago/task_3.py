# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
x = 23
y = 72

print("initial values:\n", "x:", x, "y:", y)

x = x + y
y = x - y
x = x - y

print("substituted values:\n", "x:", x, "y:", y)
