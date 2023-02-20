# Before you use a module,you must import it.

import math

print(dir(math))
print(math.sqrt(100))



print(math.pi)
import MyPythonModule

print(f'a in MyPythonModule is {MyPythonModule}.')
s = MyPythonModule.my_sum(1, 2, 3)
print(f'sum is {s}')
