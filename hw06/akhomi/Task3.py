# Provide full program code of parse_number(num) function which returns the dict with following structure:
# {odd: number of odd digits in input value, even: number of even digits of input value} or false when wrong input value.
# num - input number.
# NOTE: Assume that the "zero" digit also belongs to even numbers
# EXAMPLE OF Inputs/Ouputs when using this function:
#
# >>>print parse_number(34567)
# {'odd': 3, 'even': 2}
#
# >>>print parse_number(100)
# {'odd': 1, 'even': 2}
#
# >>>print parse_number("word")
# False

def parse_number(num):
    """
    Dict with odd and even numbers
    :param: num
    :return: dict
    """
    count = {
    'odd': 0,
    'even': 0
}
    for i in num:
        if int(i) % 2 == 0:
            count['even'] += 1
        elif int(i) % 2 != 0:
            count['odd'] += 1


    return count

try:
    num = input("Please enter number: ")
    print(parse_number(num))
except ValueError:
    print(False)