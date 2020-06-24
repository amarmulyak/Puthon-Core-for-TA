#Please create a console script in Python:
#write code for solving next tasks:
#Task1
#Define variables a and b. Read values a and b from console and calculate:
#a + b
#a - b
#a * b
#a / b.
#Output obtained results.



a = int(input("Please enter a:\n"))
b = int(input("Please enter b:\n"))
c = input("Please enter math operation: + or - or * or / \n")

if c == ('+'):
    print('Your result is:', a + b)
elif c == ('-'):
    print('Your result is:', a - b)
elif c == ('*'):
   print('Your result is:', a * b)
elif b == 0 and c == '/':
    print ('We cant make devision operation by zero')
elif c == ('/'):
   print('Your result is:', a / b)
else:
    print('Your input was invalid, please try again')

