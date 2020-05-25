# Change values of variables between each other

a = 1
b = 2
print(f'''Before change:
a = {a}, b = {b}''')

a, b = b, a
print(f'''After change:
a = {a}, b = {b}''')
