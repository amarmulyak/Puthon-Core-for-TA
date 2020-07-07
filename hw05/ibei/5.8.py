#Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file = input().split('.')

##
if len(file) >= 2:
    fileExt = file[-1].lower()
    if fileExt in extensions:
        print("Yes")
    else:
        print("No")
else:
    print("The file doesn't have extention")

