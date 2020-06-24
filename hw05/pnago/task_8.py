# Вводиться ім'я файлу.
# Потрібно перевірити, що його розширення входить в список допустимих.

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file = input("Enter file name:").split('.')
print("Extension is in the list." if file[-1] in extensions else "Extension is NOT in the list.")
