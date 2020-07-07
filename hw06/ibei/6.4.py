"""
Provide full program code of count_symbols(word) function which returns the
dict with following structure: `{<symbol_1>: <number_in_word>, <symbol_2>:
<number_in_word>,.....}` or false when wrong input value.
word - type str. EXAMPLE OF Inputs/Ouputs when using this function:
print count_symbols("abracadabra") {'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
print count_symbols("100500") {'1': 1, '0': 4, '5': 1}
print count_symbols("##$$aa") {'a': 2, '#': 2, '$': 2}
print count_symbols(125) False
"""

def count_symbols(word):
    if type(word) is int:
        return False
    d = {}
    for i in word:
        count = 0
        for k in word:
            if i == k:
                count += 1
        if i not in d:
            d[i] = count
    return d

print(count_symbols("2222444ggg"))
print(count_symbols(123))


