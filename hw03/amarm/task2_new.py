var_year = input("Type year: ")
var_month = input("Type month: ")
var_day = input("Type day: ")

month_31_days = [1, 3, 5, 7, 8, 10, 12]

print_date = True

# This block of code defines if a year is leap

if int(var_year) % 4 == 0 and int(var_year) % 100:
    leap_year = True
elif int(var_year) % 4 == 0 and int(var_year) % 100 == 0 \
        and int(var_year) % 400 == 0:
    leap_year = True
else:
    leap_year = False

###

if not var_year.isdigit():
    print("Year should contain numbers!")
    print_date = False

if not var_month.isdigit() or int(var_month) < 1 or int(var_month) > 12:
    print("Month is incorrect. Provide month as a number (1-12)!")
    print_date = False

if not var_day.isdigit():
    print("Day is incorrect. Provide day as a number of month!")
    print_date = False

if int(var_month) in month_31_days:
    if int(var_day) < 1 or int(var_day) > 31:
        print(f"Month {var_month} does not have {var_day}")
        print_date = False
else:
    if int(var_day) < 1 or int(var_day) > 30:
        print(f"Month {var_month} does not have {var_day}")
        print_date = False

if leap_year and int(var_month) == 2:
    if int(var_day) < 1 or int(var_day) > 29:
        print(f"Month {var_month} does not have {var_day}")
        print_date = False

if not leap_year and int(var_month) == 2:
    if int(var_day) < 1 or int(var_day) > 28:
        print(f"Month {var_month} does not have day {var_day} in {var_year}")
        print_date = False

if print_date:
    print(f"Your date is {var_year}/{var_month}/{var_day}")
