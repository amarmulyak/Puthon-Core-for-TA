year = int(input("Enter year: "))

if year % 4 == 0 and year % 100 != 0:
    print(year, "It's a leap year")
elif year % 100 == 0:
    print(year, "This is not a leap year")
elif year % 400 == 0:
    print(year, "It's a leap year")
else:
    print(year, "This is not a leap year")
