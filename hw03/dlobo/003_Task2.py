# Вести значення (рік), вивести повідомлення "It's a leap year!" якщо рік високосний і "This is not a leap year!" якщо ні.
# Ввести три значення (рік, місяць, день) у відповідні зміннію Визначити чи введені дані відповідають коректному запису дати.
# Для довільних чисел a, b i c визначти чи має рівняння ax2+bx+c=0 хоча б один дійсний коршнь і якщо так, то видрукувати його
# Задана три довільних числа. Визначити , чи модна побудувати трикутник з такими довжинами сторін. Якщо так, то видрукувати його периметр та площу.
# Нехай k - ціле від 1 до 365. Присвоїти цілій змінній n значення (понеділок, вівторок, ..., субота чи неділя) залежно від того,
# на який день тижня припадає k-й день не високосного року, в якому перше січня - понеділок.

day = int(input("Input a day" + "\n"))
month = int(input("Input a month" + "\n"))
year = int(input("Input a year" + "\n"))
leap=False
str_date=str(day) + "." + str(month) + "." + str(year) + " is correct date"
if year%4 != 0:
    leap=False
elif year%100 !=0:
    leap = True
elif year%400 != 0:
    leap=False
else: leap = True
if year <0 or month <0 or day <0 or month >12 or day >31:
        print("incorrect date")
elif day == 29 and month==2 and leap == False:
    print("incorrect date")
elif day == 30 and month ==2:
    print("incorrect date")
elif day == 31 and month not in (1,3,5,7,8,10,12):
    print("incorrect date")
else:
    print(str_date)