#Вводиться нормалізований текст, який крім слів може містити певні знаки пунктуації.
#Програма будує список слів, знаки пунктуації виключаються.
#Під нормалізованим текстом будемо розуміти текст, в якому пробіл ставиться після знаків пунктуації, за винятком відкриває дужки (пробіл перед нею).

str = input("Write down or insert some text:\n")

punctuation = ['.',',',':',';','!','?','(',')']

wordList = str.split()

c = 0
for i in wordList:
    if i[-1] in punctuation:
        wordList[c] = i[:-1]
        i = wordList[c]
    if i[0] in punctuation:
        wordList[c] = i[1:]
    c += 1

print(wordList)

