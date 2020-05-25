from calendar import monthrange

var_year = int(input("Type the year to found out if it's leap year: "))

february = monthrange(var_year, 2)  # Here 2 means second month in the year
february_days = february[1]

if february_days == 29:
    print("It's a leap year!")
else:
    print("This is not a leap year!")
