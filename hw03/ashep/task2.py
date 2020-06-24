a=1
b=1
c=1
while a==1:
    try:
        year = int(input("Please enter year "))
        if len(str(year))!=4 :
            print('Year is not correct')
            a=1
        else:
            a=0
    except ValueError:
        print('Year is not correct')
while b==1:
    try:
        month = int(input("Please enter month "))
        if 0>month or month >= 13:
            print('Month is not correct')
            b=1
        else:
            b=0
    except ValueError:
        print('Month is not correct')
while c == 1:
    try:
        day = int(input("Please enter day "))
        if 0>day or day >= 32:
            print('Day is not correct')
            c=1
        else:
            c=0
    except ValueError:
        print('Day is not correct')
