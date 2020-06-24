#Task1
#Define variables a and b. Read values a and b from console and calculate:
#a + b
#a - b
#a * b
#a / b.
#Output obtained results.


a = float(input('Input two numbers:' + '\n' + 'Input a' + '\n'))
b = float(input('Input b' + '\n'))
print('You have entered values a=', a, ' b=', b)
print('a+b=', a + b)
print('a-b=', a - b)
print('a*b=', a * b)
if b==0:
    print('Cannot calculate a/b')
else:
    print('a/b=', a / b)
