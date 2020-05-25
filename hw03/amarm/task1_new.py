var_year = int(input("Type the year to found out if it's leap year: "))

if var_year % 4 == 0 and var_year % 100:
    print("It's a leap year!")
elif var_year % 4 == 0 and var_year % 100 == 0 and var_year % 400 == 0:
    print("It's a leap year!")
else:
    print("This is not a leap year!")
