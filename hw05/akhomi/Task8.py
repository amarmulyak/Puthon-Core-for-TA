# Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
#
file = input().split('.')
print(file[1])

if file[1] in extensions:
    print('Correct extension')
else:
    print('Incorrect extension')