"""Provide full program code of parse_number(num) function which
returns the dict with following structure:
{odd: number of odd digits in input value,
even: number of even digits of input value}
or false when wrong input value.
num - input number.
NOTE: Assume that the "zero" digit also belongs to even numbers
EXAMPLE- OF Inputs/Ouputs when using this function:"""


def parse_number(num):
    if type(num)==int:
        num = str(num)
        new_dictionary = {'odd': 'number', 'even': 'number', }
        a = 0
        b = 0
        for i in num:

            if int(i) % 2 != 0 :
              a += 1

            else:
               b += 1

        new_dictionary.update({'odd': a, 'even': b})

        return new_dictionary

    else:
        return False

