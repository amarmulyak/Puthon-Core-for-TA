year = int(input("Enter a year "))
month = int(input("Enter a month "))
day = int(input("Enter a day "))
if year >= 0:
    print("Check year format")
#else:
#    print("Year format is Ok")
if month > 12 or month == 0:
    print("Check month format")
else:
    print("Month format is Ok")
if day > 31 or day == 0:
    print("Check day format")
elif day > 30 and month in (4, 6, 9, 11):
    print("Day and month doesn't match")
elif day >= 30 and month == 2:
    print("Day and month doesn't match")
elif day <= 29 and month == 2:
    if year % 4 != 0:
        print("It's not a leap year")
    elif year % 400 == 0 or year % 100 == 0:
        print("Year, month and day are ok")
    else:
        print("Year, month and day are ok")
else:
    print("Year, month and day are ok")
