# This code will give an error
# because tuple does not support assignment,its immutable
my_tuple = tuple('Python')
my_tuple[0] = 'X'
print(my_tuple)
