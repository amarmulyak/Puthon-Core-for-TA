# Multiplication of digits in the number
number = 9567
number_to_string = str(number)

numb_1 = int(number_to_string[0])
numb_2 = int(number_to_string[1])
numb_3 = int(number_to_string[2])
numb_4 = int(number_to_string[3])

multiplication = numb_1 * numb_2 * numb_3 * numb_4
print(f'''We have number: {number}
{numb_1} * {numb_2} * {numb_3} * {numb_4} = {multiplication}
''')

# Printing digits in the number reversed
number_to_list = list(number_to_string)
number_to_list.reverse()
print(f'''Our number is: {number}
This number in reverse is: {"".join(number_to_list)}
''')

# Printing digits in the number sorted
number_to_list = list(number_to_string)
number_to_list.sort()
print(f'''Our number is: {number}
Sorted digits in number: {"".join(number_to_list)}
''')

