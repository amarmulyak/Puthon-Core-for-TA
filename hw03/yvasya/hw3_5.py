n = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
while True:
    k = int(input("Enter k number from 1 to 365: "))

    if k > 0 and k <= 365:
        date = k % 7
        print(str(k) + " is " + n[date-1])

