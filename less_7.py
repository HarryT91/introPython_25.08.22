1 ###
my_list =














3  ###

my_list = [1, 2, 3,]
symbol = len(my_list)
my_slice = my_list[-2:]
my_total = sum(my_slice)
for symbol in my_list:
     if symbol > 2:
         my_list.append(0)
     elif symbol <= 2:
         my_list.append(my_total)
    print(my_list)
