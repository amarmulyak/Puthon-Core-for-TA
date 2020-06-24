y = int(input("Enter year: "))
m = str(input("Enter month: "))
d = str(input("Enter day: "))

day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
         'December']

a = []

a.append(y)
a.append(m)
a.append(d)

if a[0] == y and a[1] == m and a[2] == d:
    if m in month and d in day and y:
        print('Your input is corrent: ''{}, {}, {} '.format(y, m, d))
    else:
        print('Wrong format, please try again')
else:
    print('Wrong format, please try again')
