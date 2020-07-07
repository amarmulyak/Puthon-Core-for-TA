# Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації.
# Програма будує список слів, знаки пунктуації виключаються.
# Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації,
# за винятком відкриває дужки (пробіл перед нею).

str = input("Write down or insert some text:\n")
punctuation = ['.',',',':',';','!','?','(',')']

wordList = str.split()
text = []
for word in wordList:
    last = word[-1]
    first = word[0]
    if first and last in punctuation:
        text.append(word[1:-1])
    elif last in punctuation:
        text.append(word[:-1])
    elif first == "(":
        text.append(word[1:])
    else:
        text.append(word)

print("Text: ", text)

