year = int(input("Enter a year: "))
if year % 4 != 0:
    print("This is not a leap year!")
elif year % 100 != 0:
    print("It's a leap year!")
elif year % 400 != 0:
    print("This is not a leap year!")
else:
    print("It's a leap year!")
