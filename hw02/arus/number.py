number = 5493
multi = 1
for num in str(number):
    multi *= int(num)
print(multi)

num = str(number)
backwards = num[-1] + num[-2] + num[-3] + num[-4]
print(backwards)

sorted_list = [int(i) for i in str(number)]
sorted_list.sort()
print(sorted_list)
