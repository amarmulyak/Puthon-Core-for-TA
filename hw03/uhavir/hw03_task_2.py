year = int(input("Enter a year number: "))
month = int(input("Enter a month number: "))
day = int(input("Enter a day number: "))
assert year in range(0, 2021), "Incorrect year"
assert month in range(1, 13), "Incorrect month, try enter correct number of month"
if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        assert day in range(1, 30)
    else:
        assert day in range(1, 29)
elif month in [1, 3, 5, 7, 8, 10, 12]:
    assert day in range(1, 32)
else:
    assert day in range(1, 31)
