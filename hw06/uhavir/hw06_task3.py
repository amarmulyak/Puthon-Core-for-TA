# Provide full program code of parse_number(num) function which returns the dict with following structure:
# {odd: number of odd digits in input value, even: number of even digits of input value}
# or false when wrong input value.
# num - input number.
#
# NOTE: Assume that the "zero" digit also belongs to even numbers
# EXAMPLE OF Inputs/Ouputs when using this function:
# ```
# >>>print parse_number(34567)
# {'odd': 3, 'even': 2}
#
# >>>print parse_number(100)
# {'odd': 1, 'even': 2}
#
# >>>print parse_number("word")
# False
# ```


def parse_number(num):
    # assert type(num) is int
    if not isinstance(num, int):
        return False
    # num = int(num)
    # # ns = [int(x) for x in str(num)]
    # odd = []
    # even = []
    # for i in str(num):
    #     if i % 2:
    #         odd.append(i)
    #     else:
    #         even.append(i)
    # d = {'odd': len(odd), 'even': len(even)}
    d = {'odd': 0, 'even': 0}
    for i in str(num):
        i = int(i)
        if i % 2:
            d['odd'] += 1
        else:
            d['even'] += 1
    return d


# print(parse_number((input("Please enter a number: "))))
print(parse_number(34567))
print(parse_number(100))
print(parse_number("word"))