import numpy
from numpy import *
import scipy
from scipy import linalg
from gaussPivot import *
from gaussElimin import *
from numpy.linalg import solve
from LUdecomp import *
import matplotlib.pylab as plt
from scipy import *



G = array([[2.0,-1.0,0.0,0.0],[0.0,0.0,-1.0,1.0],[0.0,-1.0,2.0,-1.0],[-1.0,2.0,-1.0,1.0]]) #setting up a matrix for G in order to solve system of simultaneous equations
print "G=", G
H = array ([[1.0],[0.0],[0.0],[1.0]])
print "H=", H

I=gaussPivot(G,H)
print "Gauss Pivot solutions are", I
print "x1=1, x2=1, x3=1, x4=1"

J=gaussElimin(G,H) # this gives different solutions. gauss pivot is designed to avoid dividing by zero or dividing by small numbers
print "Gaussian Elimination solutions are", J
