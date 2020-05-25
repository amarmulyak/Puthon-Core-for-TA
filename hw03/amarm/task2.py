var_year = input("Type year: ")
var_month = input("Type month: ")
var_day = input("Type day: ")

if not var_year.isdigit() or len(var_year) != 4:
    print("Year is incorrect. It should contain 4 numbers!")
elif not var_month.isdigit() or int(var_month) < 1 or int(var_month) > 12:
    print("Month is incorrect. Provide month as a number!")
elif not var_day.isdigit() or int(var_day) < 1 or int(var_day) > 31:
    print("Day is incorrect. Provide day as a number of month!")
else:
    print(f'''Your date is {var_year}/{var_month}/{var_day}.
It has correct format!''')
