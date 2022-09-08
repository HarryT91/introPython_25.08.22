1###
value = 88
result = value/2 if value <100 else value*-1


2###
value = 90
result = 1 if value < 100 else 0

3###
value = 101
result = True if value < 100 else  False

4  ###
my_str = "putinkaput"
new_str = my_str
symbol_count = len(my_str)
if symbol_count < 5:
    new_str = my_str[0:] + my_str[0:]
elif symbol_count > 5:
    new_str = my_str

5###
my_str = "putinkaput"
new_str = my_str
symbol_count = len(my_str)
if symbol_count < 20:
    new_str = my_str[::-1] + my_str[1:]
elif symbol_count > 5:
    new_str = my_str
