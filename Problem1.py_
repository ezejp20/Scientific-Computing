import numpy
from gaussElimin import *
from numpy.linalg import solve
from LUdecomp import *
import scipy
import matplotlib.pylab as plt
from scipy import *


#Question 1(a)
a="4V1-V2-V3-V4=V(+)"
b="-V1+3V2-V4=0"
c="-V1+3V3-V4=V(+)"
d="-V1-V2-V3+4V4=0"

print 'The 4 equations for the voltages are:',a,b,c,d

#Question 1(b)
print 'Since these are simultaneous equations, we can solve them by writing them in matrix form; Ax=B. Matrix A will display the left-hand sides of the equations; B will be a vector consisting of the right-hand sides of the equations. V+=5V.'

A=numpy.array([[4.0,-1.0,-1.0,-1.0],[-1.0,3.0,0.0,-1.0],[-1.0,0.0,3.0,-1.0],[-1.0,-1.0,-1.0,4.0]])
B=numpy.array([[5.0],[0.0],[5.0],[0.0]])
print 'A=',A
print 'B=',B
print 'We are now looking for the vector x, which contains the solutions to our equations. We can find x using the gaussElimin package.'
x=gaussElimin(A,B)
print x
print 'From x we can see that V1=3;V2=1.66666667; V3=3.33333333; V4=2'
#Question 1(c)
C=LUdecomp(A)
print 'This is the LU-Decomposition of matrix A:',C

#Question 1(d)
print 'Below are vectors B, as before, and D, where V0=1 instead of 0'
B=numpy.array([[5.0],[0.0],[5.0],[0.0]])
D=numpy.array([[5.0],[1.0],[5.0],[1.0]])
print 'B=',B
print 'D=',D 
e=A.copy()
f=solve(A,B)
g=solve(e,D)
print 'Using LU decomposition, and the original value of V0=0; solutions are:',f, 'Using LU decomposition,and V0=1; solutions are:',g
