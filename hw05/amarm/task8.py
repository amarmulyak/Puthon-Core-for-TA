"""
Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список
допустимих.

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
file = input().split('.')

"""

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']
file = input("Type file name: ").split('.')

extension_index = len(file) - 1

if file[extension_index] in extensions:
    print("Your file is supported")
else:
    print("Sorry, your file is not supported")
