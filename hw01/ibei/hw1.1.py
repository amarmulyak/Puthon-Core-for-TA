#Output question “What is your name?“, “How old are you?“, Where do you live?“.
#Read the answer of user and output next information: “Hello, (answer(name))“, “Your age is (answer(age))“, “You live in (answer(city))“

a = str(input("What is your name?:\n"))
b = str(input("How old are you?:\n"))
c = str(input("Where do you live?:\n"))

print('"Hello, {}", "Your age is {}", "You live in {}" '.format(a, b, c))


