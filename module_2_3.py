my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = my_list[0]
while x >= 0 and len(my_list) > 0:
    if x == 0:
        del my_list[0]
        x = my_list[0]
    print(x)
    del my_list[0]
    if len(my_list) > 0:
        x = my_list[0]
    else:
        break
