k = int(input("k: "))

n = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

if k > 1 and k <= 365:
    a = k % 7
    print(n[a - 1])
else:
    print('Wrong date, please try again')
