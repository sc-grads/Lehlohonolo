# def my_func():
# global x
# x = 3
# print(x)
# my_func()
# print(x)
# This one has errors
# x = 2
# def my_func():
#   x = x + 1
#   print(x)
# my_func()
# print(x)

# ------------------------------------------------
# x = 1
# def func(x=0):
#  x += 9
#   return x
# print(x, func(), func(10))

# x = 1

# -----------------------------------------
# Lets see how this one works
# def func(x=None):
# x += 9
# return x
# print(x, func(), func(10))

a = 1
b = ['a', 'b']
c = [10, 20]


def change():
    a = 66
    b.append(10)
    c = [100]

change()
print(a)
print(b)
print(c)
