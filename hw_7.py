1###

my_list = [11, 105, 87]
for symbol in my_list:
    if symbol > 100:
        print(symbol)

2###

my_list = [11, 105, 87]
my_results = []
for symbol in my_list:
    if symbol > 100:
        my_results.append(symbol)
        print(my_results)

3###
my_list = [11, 105, 87]
symbol = len(my_list)
my_slice = my_list[-2:]
for symbol in my_list:
    if symbol < 2:
        my_list.append(0)
    if symbol >= 2:
        my_list.append(sum(my_slice))
        print(my_list)



