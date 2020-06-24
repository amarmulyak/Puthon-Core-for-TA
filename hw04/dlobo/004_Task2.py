# Знайти всі чотирьохзначні числа, сума цифер яких дорівнює заданому числу
# Задане число. перевірити чи дане число є простим

number = int(input("Input number" + "\n"))
if number <= 0:
    print("Incorrect number")
elif number == 1:
    print("1 is prime")
else:
    for i in range(2, number):
        if number % i == 0:
            print(number, "is not prime, divided by", i)
            break
    else:
        print(number, "is prime")
