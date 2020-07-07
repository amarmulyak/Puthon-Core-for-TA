
# 1. Записати в стрічку філософію Пайтона

philosophy = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

# 2. Знайти в заданій стрічці кількість входжень слів (better, never, is)
num_better = philosophy.find('better')
num_never = philosophy.find('never')
num_is = philosophy.find('is')

print("Word 'better' is shown " + str(num_better) + " times.")
print("Word 'never' is shown " + str(num_never) + " times.")
print("Word 'is' is shown " + str(num_is) + " times.")
print("")

# 3. Вивести весь текст у верхньому регістрі (всі великі літери)

philosophy_upper = philosophy.upper()
print(philosophy_upper)
print("")

# 4. Замінити всі входження символу “і” на “&”

philosophy_replace = philosophy.replace('i', '&')
print(philosophy_replace)





