def outer():
    msg = 'Python'

    def inner():
        print(f'{msg} is really cool!')
        inner()
#return inner

outer()
#The inner function is only created when calling outer