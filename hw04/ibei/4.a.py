#•	Знайти всі чотирьохзначні числа, сума цифер яких рівна заданому числу.

n = (int(input("Input n" + "\n")))

l = []
s = 0


for i in range(1000, 10000):
    st = str(i)
    for k in st:
        k = int(k)
        s += k
    if s == n:
        l.append(i)
        s = 0

    else:
        s = 0
for el in l:
    print ("sum is:", el)

