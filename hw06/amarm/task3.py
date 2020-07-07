"""
Provide full program code of parse_number(num) function which returns the dict
with following structure: {odd: number of odd digits in input value,
even: number of even digits of input value} or false when wrong input value.

num - input number.

NOTE: Assume that the "zero" digit also belongs to even numbers

EXAMPLE OF Inputs/Ouputs when using this function:

print parse_number(34567)
{'odd': 3, 'even': 2}

print parse_number(100)
{'odd': 1, 'even': 2}

print parse_number("word")
False
"""


def parse_number(numbers):
    str_numbers = str(numbers)
    odds = 0
    evens = 0
    for number in str_numbers:
        if number.isalpha():
            return False
        elif int(number) == 0 or int(number) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return {
        "evens": evens,
        "odds": odds
    }


print(parse_number(123456))

