str = """Water hollows stone,
wind scatters water,
stone stops the wind.
Water, wind, stone.

Wind carves stone,
stone's a cup of water,
water escapes and is wind.
Stone, wind, water."""
#print(str)
word = 'wind'
poem = str.split()
#print(poem)

for words in poem:
    if word in words.lower():
        print(word)




