import imp
import os 
print(os.listdir('./'))
print(os.listdir('./demo'))

import sys
print("Path is: ")
print(sys.path)
print("Modules in the system:")
print(sys.modules)

import math 
print(math.sqrt(144))
print(math.floor(10.5))
print(math.ceil(2.4))
print(math.ceil(-3.5))
print(math.factorial(4))

import statistics
print(statistics.mean([2,3,4,5,6,7,8]))
print(statistics.median([2,3,4,5,6,7,8]))
print(statistics.mode([2,3,4,5,6,7,8]))
