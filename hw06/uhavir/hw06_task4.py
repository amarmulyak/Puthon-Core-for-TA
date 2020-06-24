# Provide full program code of count_symbols(word) function which returns the dict with following structure:
# `{<symbol_1>: <number_in_word>, <symbol_2>: <number_in_word>,.....}` or false when wrong input value.
# word - type str.
#
# EXAMPLE OF Inputs/Ouputs when using this function:
# ```
# >>> print count_symbols("abracadabra")
# {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
#
# >>> print count_symbols("100500")
# {'1': 1, '0': 4, '5': 1}
#
# >>> print count_symbols("##$$aa")
# {'a': 2, '#': 2, '$': 2}
#
# >>> print count_symbols(125)
# False
# ```


def count_symbols(word):
    # assert type(word) is str
    if not isinstance(word, str):
        return False
    w = word.lower().strip()
    d = {}
    for l in w:
        if l in d:
            d[l] += 1
        else:
            d[l] = 1
    return d


# count_symbols(input("Please enter a word: "))
print(count_symbols("abracadabra") )
print(count_symbols("100500"))
print(count_symbols("##$$aa"))
print(count_symbols(125))
