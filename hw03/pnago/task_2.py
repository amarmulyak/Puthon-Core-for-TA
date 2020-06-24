year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

short_months = [4, 6, 9, 11]

# Check if it is a leap year
is_leap = False
if year % 4 != 0:
    is_leap
elif year % 100 != 0:
    is_leap = True
elif year % 400 != 0:
    is_leap
else:
    is_leap = True

# Date validation
if year < 0 or month < 1 or month > 12 or day > 31:
    print("The date you have entered is invalid!")
elif month in short_months and day > 30:
    print("The date you have entered is invalid!")
elif month == 2:
    if day > 29:
        print("The date you have entered is invalid!")
    elif day == 29 and not is_leap:
        print("The date you have entered is invalid!")
    else:
        print("year:", year, "month:", month, "day:", day)
