# Вводиться ім'я файлу. Потрібно перевірити, що його розширення входить в список допустимих.

extensions = ['png', 'jpg', 'jpeg', 'gif', 'svg']

file = input("Enter file name ").split('.')
print(file)

file_extension = file[- 1]

print("The file format is: ", file_extension)

if file_extension in extensions:
    print("The file format is correct!")
else:
    print("The file format is not allowed")
