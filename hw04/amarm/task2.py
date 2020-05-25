print("This program evaluates if the number is simple.")
set_numb = int(input("Type your number: "))
i = 0
for numb in range(1, set_numb + 1):
    if set_numb % numb == 0:
        i += 1
if i > 2:
    print(f"{set_numb} is not simple")
else:
    print(f"{set_numb} is simple")
