x = int(input("Please enter positive digit: "))
count = 0
if x <= 1:
    print("It's not prime number")

for i in range(1, x+1):
    # print(x, i)
    if x % i == 0:
        count = count + 1 # count += 1
        #print("count", count)
    #print(a, b)
if count == 2:
    print("Prime number")
else:
    print("Not prime")