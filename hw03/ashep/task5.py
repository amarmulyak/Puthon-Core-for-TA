day_of_week = ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]

k = int(input("Enter number "))

if 0 < k <= 365:
    n = day_of_week[(k % 7)-1]
    print("The weekday is {}".format(n))
else:
    print("k should be between 1 and 365")

