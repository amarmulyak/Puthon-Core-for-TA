k = int(input("Enter a value from 1 to 365:"))

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if 0 < k < 365:
    n = (k % 7) - 1
    print(days[n])
else:
    print("Out of range")
