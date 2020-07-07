"""Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації. Програма будує список слів, знаки пунктуації виключаються. Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації, за винятком відкриває дужки (пробіл перед нею)"""
str = input("Write down or insert some text:\n")

punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']

wordList = str.split()

i = 0
for word in wordList:
    if word[-1] in punctuation:
     wordList[i] = word[:-1]
     word = wordList[i]
    if word[0] in punctuation:
     wordList[i] = word[1:]
    i += 1

print(wordList)
