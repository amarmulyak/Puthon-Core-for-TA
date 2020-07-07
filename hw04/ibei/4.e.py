# •	Заданий текст, вивести всі слова які починаються на певну послідовність символів.

s = input("Please input text: ")
seq = input("Please input some sequance: ")

for i in s.split():
    if i.startswith(seq):
        print(i)


