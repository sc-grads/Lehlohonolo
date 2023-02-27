def sum(number, fn):
    result = 0
    for n in range(1, number + 1):
        result += fn(n)
        return result


def square(x):
    return x ** 2


result = sum(3, square)
print(result)

import math

result = sum(10, math.sqrt())
print(result)


# function that returns a function
def compute(msg):
    if msg == "square":
        return square
    else:
        return math.sqrt()


func = compute("square")
print(func(10))

fn = compute("x")
