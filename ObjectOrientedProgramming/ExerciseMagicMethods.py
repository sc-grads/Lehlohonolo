# Consider the Circle class defined below.


# Add a magic method that will automatically be called when printing instance so fthe class


# The magic method should only return the radius as a string.
# Then, print the moon object!

class Circle:
    def __init__(self, radius):
        self.radius = radius


# moon = Circle(1737)
## Defining a class
class Circle:
    def __init__(self, radius):  # instance attribute
        self.radius = radius

    ## Magic Method that is automatically called when printing an object
    def __str__(self):
        return str(self.radius)  # returning the radius as a string


## Creating an instance called moon with a radius of 1737
moon = Circle(1737)

## Printing the object
print(moon)
