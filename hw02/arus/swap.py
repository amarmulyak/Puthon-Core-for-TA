a = 'abc'
b = 'xyz'
a += b
b = a[:3]
a = a[3:]
print(a)
print(b)
