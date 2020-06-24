def user_info():
    name = input("What is your name?")
    age = input("How old are you?")
    place = input("Where are you from?")
    print ("Hello, {}! Your age is {}. You live in {}.".format(name, age, place))


user_info()