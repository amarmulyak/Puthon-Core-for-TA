k = int(input("k: "))
n = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

if k > 1 and k <= 365:
    z = k % 7
    print(n[z - 1])
else:
    print("Please enter numbers from 1 to 365")