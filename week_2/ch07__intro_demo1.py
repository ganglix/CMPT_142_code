# How to import a module
import math
print(math.pi)
print(math.sin(math.pi))  # sin(pi)
print(math.sin(30)) # math.sin accepts rad
print(math.sin(math.radians(30)))
print(math.pow(10,2))   # return a float

# alias
import math as m
print(m.pow(10,2))


# real world engineering (my experience)
# scientific computing, matrix, array
import numpy as np   # for matrix, array high performance computing
import scipy

# visualization
import matplotlib.pyplot as plt
# plt.plot(x, y, ...)



# Things I want to mention
# import one or *all

# import just one function from a module
from math import sin, pi
print(sin(pi))
from math import *   # import all (more than 1000) function names in that module, not good

# to avoid name collision with your own variables, always import module and use module.function()

