#Заданий текст, вивести всі слова які починаються на певну послідовність символів

text = """Python is an interpreted, high-level, general-purpose programming language. 
       Created by Guido van Rossum and first released in 1991, Python's design philosophy 
       emphasizes code readability with its notable use of significant whitespace. 
       Its language constructs and object-oriented approach aim to help programmers 
       write clear, logical code for small and large-scale projects Python is dynamically 
       typed and garbage-collected. It supports multiple programming paradigms,
        including structured (particularly, procedural), object-oriented, 
       and functional programming. Python is often described as a "batteries included
       language due to its comprehensive standard library"""

search_request = input("Enter search word ")

words = text.split()
search_result = [word for word in words if word.startswith(search_request)]

print(search_result)
