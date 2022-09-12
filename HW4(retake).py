4  ###
my_str = "putinkaput"
symbol_count = len(my_str)
result = my_str if symbol_count < 5 else my_str[:] + my_str[:]

5  ###
my_str = "putinkaput"
symbol_count = len(my_str)
result = my_str if symbol_count < 5 else my_str[::-1] + my_str[1:]