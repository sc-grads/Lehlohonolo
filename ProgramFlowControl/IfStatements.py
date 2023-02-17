a = 10
if a >= 10:
    print('A')
    if a // 5 == 2:
        print('A')
else:
    print('B')

version = '3'
if version in 'Python 3.8':
    print('We are using Python 3')
else:
    print('We are using Python 2')
print('We are using Python')
# This one produces syntax error
# age = 20
# if age in '20 years':
# print('He is 20 years old')
# else:
#  print('He is not 20 years old')
a = -1
if a:
    print('message 1')
else:
    print('message 2')

# Exercises
a = 20
if a == 20 and a < 30:
    print('message 1')
elif a == 20 and a > 20:
    print('message 2')
else:
    print('message 3')
# Here more than one condition is true so the first one to be true gets exucuted
a = 1
if a < 2:
    print('a is less than 2')
elif a == 1:
    print('a is equal to 1')
else:
    print('a')
# Another complicated one
my_str = 'I Love Python!'

if my_str[-2].islower() and 'Java' not in my_str:
    print(my_str[2:].upper())
elif my_str[::] != my_str:
    print(my_str.lower())
else:
    print(my_str[::-1])
# Check here as well
s = 'x'
if s:
    print('A')
else:
    print('B')
# Also here
n = 0
if n:
    print('A')
else:
    print('B')
