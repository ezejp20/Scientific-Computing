import matplotlib.pyplot as plt
from numpy import *


x = linspace(0,2*pi,50)
plt.plot((x, sin(x))(x, sin(2*x)))
plt.show()
