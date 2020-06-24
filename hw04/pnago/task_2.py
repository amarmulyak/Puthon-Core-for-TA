# •	Здано число, перевірити чи дане число являється простим числом.

num = int(input("Enter the number to check if it is a prime number:"))
is_prime = True
for i in range(2, num - 1):
    if num % i == 0:
        is_prime = False
        break
    else:
        is_prime = True
if is_prime:
    print("The number is prime.")
else:
    print("The number you've entered is not prime.")
