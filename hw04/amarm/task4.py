print("This program calculates the sum of each number exponented by 3")

number = input("Type your number: ")
result = 0
for digit in number:
    result = result + int(digit) ** 3
print(result)
