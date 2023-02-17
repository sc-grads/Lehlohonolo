class Robot:
    """This class implemensts a robot"""


# Everytime you create an instance of your class this special method will be declare
# It is optional to explicitly declare it

def __init__(self, name, year):
    self.name = name
    self.year = year


r1 = Robot('R1', 2023)
print(r1.__doc__)
print(f'Robot name: {r1.name}')
print(r1.__dict__)


class MyAi:
    """This class implments an algorithm for AI."""
    version = 1.0

    def __init__(self, author) -> object:
        self.author = author


x = MyAi('Your Master')
