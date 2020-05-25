print("This program finds all four-digit numbers whose sum of digits is equal"
      " to a given number.")
val = int(input("Type your number: "))
result = []
for a in range(0, 10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                sum = a + b + c + d
                if sum == val:
                    # print(f"{a} + {b} + {c} + {d} = {sum}")
                    if a == 0:
                        continue
                    result = (str(a)+str(b)+str(c)+str(d))
                    # number_str = str(result)
                    # number_int = "".join(number_str)
                    print(result)
if not result:
    print("There are no numbers")



