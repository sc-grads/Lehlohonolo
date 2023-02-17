# Global variable x
x = 10


def increment():
    global x  # this is the global variable x, not a local copy
    x += 1  # incrementing the global variable x

# Calling the function
increment()

# Printing the value of x after calling the function (x is 11)
print(x)
