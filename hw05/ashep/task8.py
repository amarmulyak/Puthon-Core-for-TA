# Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.
extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file = input().split('.')
if file[1] in extensions:
    print("File exe is in the allowed list ")
elif file[1] not in extensions:
    print("File exe is not in the allowed list ")

