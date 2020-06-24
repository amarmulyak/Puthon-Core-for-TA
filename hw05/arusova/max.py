#№8. Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.
#```
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
file = input().split('.')
if file[1] in extensions:
        print("File format is correct")
else:
        print("Check file format")


