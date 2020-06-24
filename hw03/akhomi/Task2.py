year = int(input('year: '))
month = int(input('month: '))
day = int(input('day: '))
if year <= 2020 and month <= 12 and day <= 31:
    print('Correct date format')
else:
    print('Incorrect date format')


