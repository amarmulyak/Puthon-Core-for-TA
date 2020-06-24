year = input("Please enter year ")

if int(year)%4 == 0:
    if int(year)%100 == 0:
        if int(year)%400 == 0:
            print("It's a leap year!")
        else:
            print("This is not a leap year!")
    else:
        print("It's a leap year!")
else:
    print("This is not a leap year!")
