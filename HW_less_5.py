values = (1, 2, 3, 4, 5)

values = list(values)

print(type(values))


values = (1, 2, 3, 4, 5)

result = []

for value in values:

.... result.append(value)

print(result)


values = (1, 2, 3, 4, 5)

result = []

for value in values[::-1]:

    result.append(value)

print(result)


values = [1, 2, 3, 4, 5]

new_values = values + values[::-1]

print(new_values)





values = [1, 2, 3, 4, 5]

new_values = values[::-1] * 2

print(new_values)


values = [1, 2, 3, 4, 5]

new_values = values

new_values.append(6)

print(values)



values = [1, 2, 3, 4, 5]

new_values = values.copy()

new_values.append(6)

print(values)

my_list = list("qwerty")

my_str = " ".join(my_list)

print(my_str)


my_list = list("qwerty")

my_str = "_".join(my_list[::-1])

print(my_str)


my_list = list("qwerty")

my_str = "".join(my_list[::-1])

print(my_str[::-1])





values = [1, 2, 3, 4, 5]

new_values = values

new_values.append(6)

print(values)
values = [1, 2, 3, 4, 5]

new_values = values.copy()

new_values.append(6)

print(values)
my_list = list("qwerty")

my_str = " ".join(my_list)

print(my_str)
my_list = list("qwerty")

my_str = "_".join(my_list[::-1])

print(my_str)
my_list = list("qwerty")

my_str = "".join(my_list[::-1])

print(my_str[::-1])