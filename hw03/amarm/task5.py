print('''This program calculates which day of the week "k" is.
''')

day_of_week = {
    "0": "Sunday",
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday"
}

k = int(input("Provide k value. It should be between 1 and 365: "))

if k >= 1 and k <= 365:
    n = day_of_week[str(k % 7)]
    print(f"'k' day is {n}")
else:
    print("k should be between 1 and 365")
