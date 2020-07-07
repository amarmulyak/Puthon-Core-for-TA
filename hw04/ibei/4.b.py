#•	Здано число, перевірити чи дане число являється простим числом.

import math

n = int(input("Please input:"))

if n < 2:
    print("please input > 1")
    quit()
elif n == 2:
    print("Prime")
    quit()

i = 2

limit = int(math.sqrt(n))

while i <= limit:
    if n % i == 0:
        print("Not prime")
        quit()
    i += 1

print("Prime")

