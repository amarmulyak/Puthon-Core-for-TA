zen_of_python = "Beautiful is better than ugly.\n " \
                "Explicit is better than implicit.\n" \
                "Simple is better than complex.\n" \
                "Complex is better than complicated.\n" \
                "Flat is better than nested.\n" \
                "Sparse is better than dense.\n" \
                "Readability counts.\n" \
                "Special cases aren't special enough to break the rules.\n" \
                "Although practicality beats purity.\n" \
                "Errors should never pass silently.\n" \
                "Unless explicitly silenced.\n" \
                "In the face of ambiguity, refuse the temptation to guess.\n" \
                "There should be one-- and preferably only one --obvious way to do it.\n" \
                "Although that way may not be obvious at first unless you're Dutch.\n" \
                "Now is better than never.\n" \
                "Although never is often better than *right* now.\n" \
                "If the implementation is hard to explain, it's a bad idea.\n" \
                "If the implementation is easy to explain, it may be a good idea.\n" \
                "Namespaces are one honking great idea -- let's do more of those!"
# print(zen_of_python)
# Знайти в заданій стрічці кількість входжень слів (better, never, is)
better = "better"
never = "never"
substring_is = "is"
count_better = zen_of_python. count(better)
count_never = zen_of_python. count(never)
count = zen_of_python. count(substring_is)

print("The count better:", count_better)
print("The count never:", count_never)
print("The count is:", count)

# Вивести весь текст у верхньому регістрі (всі великі літери)
print(zen_of_python.upper())

# Замінити всі входження символу “і” на “&”
print(zen_of_python.replace("and", "&"))


