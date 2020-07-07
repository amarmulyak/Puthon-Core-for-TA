
# https://en.wikipedia.org/wiki/Leap_year

while True:

    year = input("Please enter a year: ")
    year = int(year)

# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100,
# but these centurial years are leap years if they are exactly divisible by 400.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("It's a leap year!")
    else:
        print("This is not a leap year year")


