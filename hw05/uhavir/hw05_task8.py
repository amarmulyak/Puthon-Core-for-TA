#  Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file = input().split('.')
if len(file) >= 2:
    fileExtension = file[-1].lower()
    if fileExtension in extensions:
        print("Розширення файлу правильне")
    else:
        print("Розширення не вірне")
else:
    print("Це не файл")
