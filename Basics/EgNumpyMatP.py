'''
Examples from: https://new.pythonforengineers.com/blog/an-introduction-to-numpy-and-matplotlib/

Objective: learn List Comprehension, NumPy basics and Matplotlib basics
'''

import numpy as np
import matplotlib.pyplot as plt # note: Matplotlib is huge, hence import small part 


## Using List comprehension
x = [5, 10 ,15 ,20 ,25]
y = [n/5 for n in x] # use of list comprehension
print("The valus are X = {}, Y = {}".format(x,y)) # use of FORMAT function


## Using Numpy
m = np.array(x)
n = m/5
print("The values with numpy are M = {}, N = {}".format(m,n))


## Using MatplotLib
# plotting Sin wave
x = np.linspace(0, 20, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "-g", label="sine")
plt.plot(x, y2, "-b", label ="cos")
plt.legend(loc="lower right")
plt.show()




