# Знайти всі чотирьохзначні числа, сума цифер яких дорівнює заданому числу

number = (input("Input number" + "\n"))
number_int = int(number)
sum = 0
number_list = []
if number_int <= 0 or number_int > 36:
    print("Incorrect number")
else:
    for i in range(1000, 10000):
        i_str = str(i)
        for j in i_str:
            j = int(j)
            sum += j
        if sum == number_int:
            number_list.append(i)
        sum = 0
        # else:
        #     sum = 0
print("Sum of digits in numbers", number_list, "equals", number)
