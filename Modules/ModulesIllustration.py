# Before you use a module,you must import it.
# dir method prints all the functionalities of a module
import math

print(dir(math))
print(math.sqrt(100))

# If you wanna import a certain modules
from math import pi, sqrt, factorial

print(math.pi)
import MyPythonModule

print(f'a in MyPythonModule is {MyPythonModule}.')
s = MyPythonModule.my_sum(1, 2, 3)
print(f'sum is {s}')
