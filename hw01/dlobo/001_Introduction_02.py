#Task2
#Output question “What is your name?“, “How old are you?“, Where do you live?“.
# Read the answer of user and output next information: “Hello, (answer(name))“, “Your age is  (answer(age))“, “You live in  (answer(city))“

name = (input('What is your name?' + '\n'))
age = int(input('How old are you?' + '\n'))
city = (input('Where do you live?' + '\n'))
print('Hello, ' + name)
print('Your age is ', age)
print('You live in ' + city)
