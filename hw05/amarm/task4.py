"""
Вводиться нормалізований текст, який крім слів може містити певні знаки
пунктуації. Програма будує список слів, знаки пунктуації виключаються.
Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться
після знаків пунктуації, за винятком відкриває дужки (пробіл перед нею).

str = input("Write down or insert some text:\n")
punctuation = ['.',',',':',';','!','?','(',')']
wordList = str.split()
"""

text = ("""Вводиться нормалізований текст! Крім слів може містити
певні знаки пунктуації. Програма будує список слів? Знаки
пунктуації виключаються; Під нормалізованим текстом будемо
розуміти: текст, в якому пробіл ставиться після знаків
пунктуації, за винятком відкриває дужки (пробіл перед нею)?""")

punctuations = ['.', ',', ':', ';', '!', '?', '(', ')']

wordList = text.split()

word_no_punctuation = []
for word in wordList:
    if word[-1] in punctuations and word[-2] in punctuations:
        new_word = word[0:-2]
        word_no_punctuation.append(new_word)
    elif word[-1] in punctuations:
        new_word = word[0:-1]
        word_no_punctuation.append(new_word)
    elif word[0] in punctuations:
        new_word = word[1:]
        word_no_punctuation.append(new_word)
    else:
        word_no_punctuation.append(word)
print(word_no_punctuation)
