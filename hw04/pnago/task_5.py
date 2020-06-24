# •	Заданий текст, вивести всі слова які починаються на певну послідовність символів.
import re
your_text = input("Enter some text:")
seq = input("Enter the search phrase:")
text_arr = re.split(', |_|-|!|\.| |\"| \(|\)', your_text)
words = []
for i in text_arr:
    if i.startswith(seq):
        if i not in words:
            words.append(i)
for word in words:
    print(word)
