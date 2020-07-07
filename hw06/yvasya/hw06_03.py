"""
Provide full program code of parse_number(num) function which returns the dict with following structure:
{odd: number of odd digits in input value, even: number of even digits of input value} or false when wrong input value.
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
d = {}
def parse_number(num):
    if str(num).isnumeric():
        num_to_parse = [int(i) for i in str(num)]
        odd_count = 0
        even_count = 0
        for i in range(len(num_to_parse)):

            if num_to_parse[i] % 2 == 0:
                even_count +=1
            else:
                odd_count +=1
        d['even'] = even_count
        d['odd'] = odd_count
        return d
    else:
        return False

print(parse_number(100))