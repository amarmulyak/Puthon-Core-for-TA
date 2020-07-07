"""Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації.
Програма будує список слів, знаки пунктуації виключаються.
Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації,
за винятком відкриває дужки (пробіл перед нею)."""

str = input("Write down or insert some text:\n")

punctuation = ['.',',',':',';','!','?','(',')']

wordList = str.split()


wordList_update = []
for word in wordList:
    new_word = word
    for character in punctuation:
        if character in new_word:
            new_word = new_word.replace(character, '')

    wordList_update.append(new_word)

print(wordList)
print(wordList_update)