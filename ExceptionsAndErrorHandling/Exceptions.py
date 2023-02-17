a = 2
b = 10
try:
    c = a / b
except Exception as e:
    print('This is the except block of code')
else:
    print('This is the else block of code')
finally:
    print('This is the finally block of code')