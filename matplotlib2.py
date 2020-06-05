#matplotlib tutorial

from numpy import *
from pylab import *
import matplotlib.mlab as mlab
x=linspace(0,2*pi,50)

mlab.plot (x, sin(x), 'r-^') #red, dot dash, triangles
mlab.show()
