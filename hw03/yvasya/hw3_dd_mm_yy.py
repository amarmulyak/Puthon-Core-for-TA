import datetime

user_date = input("Enter the date in the formal yy-mm-dd: ")

yy, mm, dd = user_date.split('-')


valid_date = True
try:
    datetime.datetime(int(yy), int(mm), int(dd))
except ValueError:
    valid_date = False

if valid_date:

    x = datetime.datetime(int(yy), int(mm), int(dd))
    x = x.strftime("%Y-%m-%d")
    print("The date format is correct")
    print(x)
else:
    print("The date format is incorrect")





