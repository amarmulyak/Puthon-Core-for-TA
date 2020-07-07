k = int(input("Please enter a day number from 1 to 365: "))
n = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 1 <= k <= 365:
    day_num = k % 7
    print(n[day_num - 1])
else:
    print("Incorrect day number")
