text = "Hello boys and girls. Hey! Let's go and play. Don't be board. We " \
       "will have fun here!"
pattern = input("Type pattern to search words: ")
pattern_length = len(pattern)
words = text.split(" ")
for word in words:
    if word[0:pattern_length].lower() == pattern.lower():
        print(word)

# Solution 2. Produces list of unique words.
# text = "Hello boys and girls. Hey! Let's go and play. Don't be board. We  " \
#        "will have fun here!"
# pattern = input("Type pattern to search words: ")
# pattern_length = len(pattern)
# list_unique = []
# words = text.split(" ")
# for word in words:
#     if word[0:pattern_length].lower() == pattern.lower():
#         if word not in list_unique:
#             list_unique.append(word)
# print(list_unique)
