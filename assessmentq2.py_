import numpy
from gaussElimin import *
from numpy.linalg import solve
from LUdecomp import *
import scipy
import matplotlib.pylab as plt
from scipy import *
from scipy import interpolate
import polyFit
from polyFit import *


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

#Question2
from numpy import *
import scipy
from scipy import linalg
from gaussPivot import *
from gaussElimin import *

G = array([[2.0,-1.0,0.0,0.0],[0.0,0.0,-1.0,1.0],[0.0,-1.0,2.0,-1.0],[-1.0,2.0,-1.0,1.0]]) #setting up a matrix for G in order to solve system of simultaneous equations
print "G=", G
H = array ([[1.0],[0.0],[0.0],[1.0]])
print "H=", H

I=gaussPivot(G,H)
print "Gauss Pivot solutions are", I
print "x1=1, x2=1, x3=1, x4=1"

J=gaussElimin(G,H) # this gives different solutions. gauss pivot is designed to avoid dividing by zero or dividing by small numbers
print "Gaussian Elimination solutions are", J

#Question 3
import scipy
import numpy
import matplotlib.pylab as plt
from scipy import *
Pi=numpy.array([1.0000,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])
hi=numpy.array([0.0000,1.5250,3.0500,4.5750,6.1000,7.6250,9.1500])
h=numpy.linspace(0,9.15,100)
P=scipy.interpolate.barycentric_interpolate(hi,Pi,h)
f=scipy.interpolate.interp1d(hi,Pi, kind='cubic')
Pnew=f(h)

plt.plot(h, Pnew, 'r-',label='Cubic')
plt.plot(h,P,'b--',label='Polynomial fit')
plt.plot(hi,Pi,'go',label='Data Points')
L=polyFit(hi,Pi,2)

Pnew2=L[0]+L[1]*h+L[2]*h**2
plt.plot(h,Pnew2,'y--',label='Quadratic least-squares fit')

plt.title('Relative density of air at various altitudes')
plt.xlabel('Altitude, h, (Km)')
plt.ylabel('Relative density of air, rho')
plt.legend()
plt.show()
h2=2.0000
h5=5.0000
rho2p=scipy.interpolate.barycentric_interpolate(hi,Pi,h2)
rho5p=scipy.interpolate.barycentric_interpolate(hi,Pi,h5)
rho2c=f(h2)
rho5c=f(h5)
PLS2=L[0]+L[1]*2+L[2]*2**2
PLS5=L[0]+L[1]*5+L[2]*5**2
print ("Relative density of air at 2km according to polynomial interpolation=",rho2p)
print ("Relative density of air at 5km according to polynomial interpolation=",rho5p)
print ("Relative density of air at 2km according to cubic spline interpolation=",rho2c)
print ("Relative density of air at 5km according to cubic spline interpolation=",rho5c)
print ("Relative density of air at 2km according to Least-Squares Quadratic=",PLS2)
print ("Relative density of air at 5km according to Least-Squares Quadratic=",PLS5)


