x = 4586
x_st = str(x)
x_1 = x_st[0]
x_2 = x_st[1]
x_3 = x_st[2]
x_4 = x_st[3]

multiplication = (int(x_1)* int(x_2)* int(x_3)* int(x_4))
print("Number multiplication is {}".format(multiplication))

num_list=list(x_st)
reverse_order=num_list[::-1]
print("Reverse order - {}".format( ''.join(reverse_order)))

new_order_list=sorted(num_list)
print("New order - {}".format( ''.join(new_order_list)))
