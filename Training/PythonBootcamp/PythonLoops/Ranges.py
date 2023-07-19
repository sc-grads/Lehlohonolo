# Using the built-in range() function, create the following lists of numbers
# list1 = [-10, -7, -4, ... , 92, 95, 98]
# list2 = [99, 97, 95, ..., 1, -1, -3]
list1 = list(range(-10, 100, 3))
print(list1)

list2 = list(range(99, -4, -2))
print(list2)

# Check out this one
a = 5
if a < 5:
    for i in range(10):
        print(i, end=' ')
elif a > 5:
    for i in range(5):
        print(i, end=' ')
else:
    for i in range(7):
        print(i, end=' ')
