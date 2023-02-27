def my_func(x, fn):
    return fn(x)

result = my_func('5', lambda x: x * 3)
print(result)

#*********************************************************
#Exercise
def my_func(x, fn):
    return fn(x)


result = my_func('a:b:c', lambda x: x.split(':'))
print(result)

#--------------------------------------------------
#Another exercise
r = (lambda a, b: min(a, b) * max(a, b))(10, 20)
print(r)