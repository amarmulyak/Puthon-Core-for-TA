check_year = int(input("Enter year "))

if check_year % 4 != 0:
    print("It's not a leap year")
elif check_year % 400 == 0:
    print("It's a leap year")
elif check_year % 100 == 0:
    print("It's a leap year")
else: 
    print("It's a leap year")
    
