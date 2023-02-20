user = {'username': 'js', 'level': 'admin'}

def user_has_permission(func):
    if user['level'] == 'admin':
        return func
    else:
        return None


def show_pass():
    return 'dkjsd37sh,.s'

my_function = user_has_permission(show_pass)
print(my_function)
