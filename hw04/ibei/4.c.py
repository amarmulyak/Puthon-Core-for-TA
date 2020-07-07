# •	Задано ціле число N, вивести перші N чисел фібоначі.

n = int(input("please enter n "))

n1 = 0
n2 = 1
count = 0

if n <= 0:
   print("Please enter n again")
elif n == 1:
   print("Fib seq is",n,":")
   print(n1)
else:
   print("Fib seq:")
   while count < n:
       print(n1)
       m = n1 + n2
       n1 = n2
       n2 = m
       count += 1

